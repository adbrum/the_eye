from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(reqyest):
    return HttpResponse("<h1>Hello, world. You're at the events index.</h1>")
