from django.urls import path
from . import views
from .views import (EventListView,
                    EventDetailView,
                    EventCreateView,
                    EventUpdateView,
                    EventDeleteView,
                    UserEventListView)


urlpatterns = [
    path('event/', EventListView.as_view(), name='event-home'),
    path('event/user/<str:username>', EventListView.as_view(), name='event-home'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/<str:username>', UserEventListView.as_view(), name='user-events'),
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
    path('event/new/', EventCreateView.as_view(), name='event-create'),
    path('event/about/', views.about, name='event-about')
]
