
from drinks.models import Drink
from drinks.serializers import DrinkSerializer
from rest_framework import generics


class DrinkList(generics.ListCreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer


class DrinkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer