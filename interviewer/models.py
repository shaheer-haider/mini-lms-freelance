from django.db import models
from  authy.models import Profile
# Create your models here.
class Interviewer(models.Model):
    email = models.ForeignKey(Profile, models.CASCADE)


class Link(models.Model):
    meeting_name = models.CharField(max_length=100)
    meeting_url = models.URLField(max_length=2000)
    start_time = models.TimeField(default='12:00:0')
    end_time = models.TimeField(default='12:00:0')
    mondey = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)

    def __str__(self):
        return self.meeting_name