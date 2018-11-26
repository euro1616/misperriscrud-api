from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Adoptante
from datetime import datetime
from django.utils.dateparse import parse_date
import requests


# Create your views here.
def index(request):
    response = requests.get('http://api.ipstack.com/200.14.248.139?access_key=a1d15d6d4c7f24c774434c2af12a642a')
    data = response.json()
    locationl = data['location']

    return render(request,'index.html',{'lista_adoptantes':Adoptante.objects.all(), 'ip': data['ip'], 'pais': data['country_name'], 'region': data['region_name'],'ciudad': data['city'],'rcode': data['region_code'], 'bandera': locationl['country_flag'] })
    

def registro(request):
    return render(request,'registro.html',{})    

def crear(request):
    run = request.POST.get('run','')
    email = request.POST.get('email','')
    nombre = request.POST.get('nombre','')
    fecha_nacimiento = request.POST.get('fecha_nacimiento',default=None)
    telefono = request.POST.get('telefono',0)
    region = request.POST.get('region','')
    ciudad = request.POST.get('ciudad','')
    tipo_vivienda = request.POST.get('tipo_vivienda','')
    adoptante = Adoptante(run = run, email = email, nombre = nombre, fecha_nacimiento = fecha_nacimiento, telefono = telefono, region = region, ciudad = ciudad, tipo_vivienda = tipo_vivienda)
    adoptante.save()
    return HttpResponse('<h2>Registro exitoso!'+'<br>run :' + run  + '<br> email:' + email)   

def buscar(request, run):
    adoptante = Adoptante.objects.get(pk=run)
    return HttpResponse('RUN:' + adoptante.run + '<br> Nombre :' + adoptante.nombre ) 

def eliminar(request, run):
    adoptante = Adoptante.objects.get(pk=run)
    adoptante.delete()
    return HttpResponse('Adoptante eliminado')

def editar(request, run):
    adoptante =Adoptante.objects.get(pk=run)
    return render(request, 'editar.html',{'adoptante': adoptante})

def edicion(request, run):
    adoptante = Adoptante.objects.get(pk=run)
    run = request.POST.get('run','')
    email = request.POST.get('email','')
    nombre = request.POST.get('nombre','')
    fecha_nacimiento = request.POST.get('fecha_nacimiento',default=None)
    telefono = request.POST.get('telefono',0)
    region = request.POST.get('region','')
    ciudad = request.POST.get('ciudad','')
    tipo_vivienda = request.POST.get('tipo_vivienda','')
    adoptante = Adoptante(run = run, email = email, nombre = nombre, fecha_nacimiento = fecha_nacimiento, telefono = telefono, region = region, ciudad = ciudad, tipo_vivienda = tipo_vivienda)
    remedio.save()
    return HttpResponse('Adotante Actualizado!')     

def test(request):
    ...
    return HttpResponseRedirect('index')