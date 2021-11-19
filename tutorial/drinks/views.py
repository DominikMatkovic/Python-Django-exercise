
from drinks.models import Drink
from drinks.serializers import DrinkSerializer
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class DrinkList(generics.ListCreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer


class DrinkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer


def index(request):

    drinks = Drink.objects.all()

    if request.method == 'POST':
        serializer = DrinkSerializer(drinks, many=True)
        return JsonResponse(serializer.data, status=201, safe=False)
    
    context = {'drinks': drinks }
    return render(request, 'drinks/drinkList.html', context)
