from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse

# Create your views here.

@api_view()
def index(request):
    c = {}
    return render(request, 'index.html', c)