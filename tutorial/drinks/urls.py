from django.urls import path
from drinks import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('drinks/', views.DrinkList.as_view()),
    path('drinks/<int:pk>/', views.DrinkDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)