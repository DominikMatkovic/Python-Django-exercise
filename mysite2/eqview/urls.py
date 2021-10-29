from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('people/<int:id>/', views.peopleDetail, name='peopleDetail'),
    path('addPersonForm/', views.addPersonForm, name='addPersonForm'),
    path('addEquipmentForm/', views.addEquipmentForm, name='addEquipmentForm'),
]