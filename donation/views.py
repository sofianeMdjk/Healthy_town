from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Donation
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)

from django.contrib.auth.models import User


def home(request):
    context = {
        'donations': Donation.objects.all()
    }
    return render(request, 'donation/home.html', context)


class DonationListViewPageLess(ListView):
    model = Donation
    template_name = 'donation/home.html'
    context_object_name = 'donations'
    ordering = ['-date_posted']


class DonationListView(ListView):
    model = Donation
    template_name = 'donation/home.html'
    context_object_name = 'donations'
    ordering = ['-date_posted']
    paginate_by = 5


class UserDonationListView(ListView):
    model = Donation
    template_name = 'donation/user_donations.html'
    context_object_name = 'donation'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Donation.objects.filter(author=user).order_by('-date_posted')


class DonationDetailView(DetailView):
    model = Donation
    template_name = 'donation/donation_detail.html'


class DonationCreateView(LoginRequiredMixin, CreateView):
    model = Donation
    fields = ['title', 'description', 'address', 'contact']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DonationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Donation
    fields = ['title', 'description', 'address', 'contact']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class DonationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Donation
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
    return render(request, 'donation/about.html', context)
