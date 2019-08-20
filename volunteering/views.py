from django.shortcuts import render
from .models import Volunteering

def volunteering(request):
    volunteering = Volunteering.objects
    return render(request, 'volunteering/volunteering.html', {'volunteering': volunteering})