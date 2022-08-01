# from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    # return HttpResponse('Hello World!')
    return render(request, 'home.html')

def contact_view(request):
    # return HttpResponse('contactez nous')
    return render(request, 'contact.html')

def resultats_view(request):
    return render(request, 'resultats.html')

def aliment_view(request):
    return render(request, 'aliment.html')

def compte_view(request):
    return render(request, 'compte.html')