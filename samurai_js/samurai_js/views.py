from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return render(request, 'index.html', {'title': 'Main page'})


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1> pageNotFound:</h1><p> {exception} </p>')
