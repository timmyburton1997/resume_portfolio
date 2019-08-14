from django.shortcuts import render
from .models import Job

def jobs(request):
    jobs = Job.objects
    return render(request, 'jobs/jobs.html', {'jobs': jobs})