# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Welcome to 먹이보고!")
