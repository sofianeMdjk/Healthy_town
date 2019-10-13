from django.urls import path
from . import views
from .views import (DonationListView,
                    DonationDetailView,
                    DonationCreateView,
                    DonationUpdateView,
                    DonationDeleteView,
                    UserDonationListView)


urlpatterns = [
    path('donation/', DonationListView.as_view(), name='donation-home'),
    path('donation/user/<str:username>', DonationListView.as_view(), name='donation-home'),
    path('donation/<int:pk>/', DonationDetailView.as_view(), name='donation-detail'),
    path('donation/<str:username>', UserDonationListView.as_view(), name='user-donations'),
    path('donation/<int:pk>/update/', DonationUpdateView.as_view(), name='donation-update'),
    path('donation/<int:pk>/delete/', DonationDeleteView.as_view(), name='donation-delete'),
    path('donation/new/', DonationCreateView.as_view(), name='donation-create'),
    path('donation/about/', views.about, name='donation-about')
]
