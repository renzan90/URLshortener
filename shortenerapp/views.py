from django.shortcuts import render
from rest_framework.decorators import api_view
from . models import URL
from django.http import HttpResponse
import json
import random
import string
from django.conf import settings

# Create your views here.

@api_view()
def index(request):
    c = {}
    return render(request, 'index.html', c)

@api_view()
def shortening(request):
    url = request.Post.get("")
    if not (url == ''):
        try:
            current_url = URL.objects.get(original_url = url)
            shorter = current_url.shorter
        except(URL.DoesNotExist):
            shorter = generate_code()
        URL_object = URL(original_url = url, shorter = shorter)
        URL_object.save()

        result = {}
        result["url"] = settings.SITE_URL + "/" + shorter
        return HttpResponse(json.dumps(result), content_type = "application/json")
    else:
        return HttpResponse(json.dumps({"error": "it errored"}), content_type = "application.json")

def generate_code():
    size = 6
    char = string.ascii_uppercase + string.ascii_lowercase + string.digits

    shorter = "".join(random.choice(char) for times in range(size))
    return shorter

