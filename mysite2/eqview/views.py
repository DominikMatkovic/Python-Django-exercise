from typing import ContextManager, Counter
from django.http import HttpResponse
from django.shortcuts import redirect, render

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

            if Person.objects.filter(OIB = request.POST.get('OIB')).exists():
                context = {'alert': 1 }
                return render(request,'eqview/addPersonForm.html',context) 

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

            if Equipment.objects.filter(serialNum = request.POST.get('serialNum')).exists():
                context = {'alert': 1, 'people_list': people_list }
                return render(request,'eqview/addEquipmentForm.html',context) 

            if request.POST.get('OIB') != "None":
                equipment.borrowedBy = Person.objects.get(OIB = request.POST.get('OIB'))
            equipment.save()

    return render(request,'eqview/addEquipmentForm.html',context) 

def deleteEquipment(request, id):
    equipment = Equipment.objects.get(pk=id)
    equipment.delete()
    return redirect('../../')

def deletePerson(request, id):
    person = Person.objects.get(pk=id)
    person.delete()
    return redirect('../../')

def updatePersonForm(request,id):

    PersonById = Person.objects.get(pk = id)
    context = {'PersonById': PersonById}

    if request.method == 'POST':
        if request.POST.get('OIB'):
            
            if Person.objects.filter(OIB = request.POST.get('OIB')).exists():
                context = {'alert': 1 ,'PersonById': PersonById}
                return render(request,'eqview/updatePersonForm.html',context) 
            
            PersonById.OIB= request.POST.get('OIB')
            PersonById.save()
    return render(request,'eqview/updatePersonForm.html',context) 
