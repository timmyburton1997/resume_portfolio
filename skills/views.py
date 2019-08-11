from django.shortcuts import render
from .models import Skills

def skills(request):
    skills = Skills.objects
    return render(request, 'skills/skills.html', {'skills': skills})
