from django.shortcuts import render
from .models import Job
# Create your views here.

def home(request):
    jobs = Job.objects  # this fetches all the Job objects from the DB and converts them into Python objects
    return render(request, 'jobs/home.html', {'jobs': jobs})