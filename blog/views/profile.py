from django.http import HttpResponse
from django.shortcuts import render

def profile(request):
    return render (request, 'flatpages/profile/profile.html')
