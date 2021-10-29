from typing import ContextManager
from django.http import HttpResponse
from django.shortcuts import render
from .models import Equipment
from .models import Person


def index(request):
    eq_list  = Equipment.objects.all()
    people_list  = Person.objects.all()
    context = {'eq_list': eq_list, 'people_list': people_list }
    return render(request, 'eqview/index.html', context)


def detail(request, id):
    EquipmentById = Equipment.objects.get(pk = id)
    context = {'EquipmentById': EquipmentById}
    return render(request, 'eqview/eqDetails.html', context)

def peopleDetail(request, id):
    PersonById = Person.objects.get(pk = id)
    context = {'PersonById': PersonById}
    return render(request, 'eqview/peopleDetails.html', context)


def addPersonForm(request):
    if request.method == 'POST':
        if request.POST.get('OIB'):
            person=Person()
            person.OIB= request.POST.get('OIB')
            person.save()


    return render(request,'eqview/addPersonForm.html') 


def addEquipmentForm(request):
    people_list  = Person.objects.all()
    context = {'people_list': people_list }

    if request.method == 'POST':
        if request.POST.get('serialNum') and request.POST.get('OIB'):
            equipment=Equipment()
            equipment.serialNum= request.POST.get('serialNum')
            #equipment.borrowedBy= request.POST.get('OIB')

            if request.POST.get('OIB') != "None":
                equipment.borrowedBy = Person.objects.get(OIB = request.POST.get('OIB'))



            equipment.save()


    return render(request,'eqview/addEquipmentForm.html',context) 
