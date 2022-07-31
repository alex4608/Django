from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    a = 5 + 5
    return render(request, "about.html")

def home (request):
    return HttpResponse("Это домашняя страница!!!")