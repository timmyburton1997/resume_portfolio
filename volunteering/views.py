from django.shortcuts import render
from .models import Volunteering

def education(request):
    volunteering = Volunteering.objects
    return render(request, 'volunteering/ducation.html', {'volunteering': volunteering})