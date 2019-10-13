from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Event
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)

from django.contrib.auth.models import User
from .manage_locations import load_dataset


def home(request):
    data1, data2, data3 = load_dataset(path="data/pollution_dataset.csv")
    context = {
        'data1': data1,
        'data2': data2,
        'data3': data3,
        'events': Event.objects.all()
    }
    return render(request, 'event/home.html', context)


class EventListViewPageLess(ListView):
    model = Event
    template_name = 'event/home.html'
    context_object_name = 'events'
    ordering = ['-event_date']


class EventListView(ListView):
    model = Event
    template_name = 'event/home.html'
    context_object_name = 'events'
    ordering = ['-event_date']
    paginate_by = 5


class UserEventListView(ListView):
    model = Event
    template_name = 'event/user_posts.html'
    context_object_name = 'events'
    ordering = ['-event_date']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Event.objects.filter(author=user).order_by('-event_date')


class EventDetailView(DetailView):
    model = Event
    template_name = 'event/event_detail.html'


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['title', 'content', 'event_date', 'address']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['title', 'content', 'event_date', 'address']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'event/about.html', context)
