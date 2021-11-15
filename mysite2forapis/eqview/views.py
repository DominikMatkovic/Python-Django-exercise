from typing import ContextManager, Counter
from django.http import HttpResponse
from django.shortcuts import redirect, render
import urllib, json
from .models import Equipment
from .models import Person

def index(request):

    url = "http://10.30.10.55:5000/drinks"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    
    context = {'data':data["drinks"]}




    return render(request, 'eqview/index.html', context)
