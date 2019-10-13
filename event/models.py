from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Event(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    event_date = models.DateTimeField(null=False)
    address = models.CharField(max_length=256)
    author = models.ForeignKey(User, related_name='eventauthor', on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='participants')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})

