from django.shortcuts import render
from django.contrib.auth.models import User
from .models import  Interviewer
import jwt
import requests
import json
from time import time
from django.http import HttpResponse
from authy.models import Profile
from .models import Link
from datetime import datetime

# Create your views here.
def interview(request):
    inter = Interviewer.objects.all()

    return render(request, 'interviewer/myiinterview.html', {'inr': inter})
def startInterview(request):
    return render(request, 'interviewer/index.html')


def create_meeting(request):
    current_time = datetime.now()
    meting_list = list(Link.objects.all)
