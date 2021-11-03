from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('people/<int:id>/', views.peopleDetail, name='peopleDetail'),
    path('deleteEquipment/<int:id>/', views.deleteEquipment, name='deleteEquipment'),
    path('deletePerson/<int:id>/', views.deletePerson, name='deletePerson'),
    path('addPersonForm/', views.addPersonForm, name='addPersonForm'),
    path('addEquipmentForm/', views.addEquipmentForm, name='addEquipmentForm'),
    path('updatePersonForm/<int:id>/', views.updatePersonForm, name='updatePersonForm'),
    path('updateEquipmentForm/<int:id>/', views.updateEquipmentForm, name='updateEquipmentForm'),

]