from django.http import HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'title': 'Main page'})


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1> pageNotFound:</h1><p> {exception} </p>')
