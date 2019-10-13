from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Donation(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=512)
    date_posted = models.DateTimeField(default=timezone.now)
    address = models.CharField(max_length=256)
    contact = models.CharField(max_length=64, default="")
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE, blank=True, null=True)
    taken = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('donation-detail', kwargs={'pk': self.pk})
