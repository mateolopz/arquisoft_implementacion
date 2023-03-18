import datetime
from django.shortcuts import render

from manejadorhistorias.forms import HistoriaForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from manejadorhistorias.models import Historia
from .logic import manejadorhistorias_logic as ml
from .forms import HistoriaForm
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt


def consultaHistorias_view(request):
    if request.method == 'GET':
        form = HistoriaForm(request.GET)
        if form.is_valid():
            historias = ml.get_HistoriasUltimoLustro(form)
            context = {
            'historias_list': historias
            }
        return render(request, 'ManejadorHistorias/historias.html', context)

def historias_list(request):
    historias = ml.get_historias()
    context = {
        'historias_list': historias
    }
    return render(request, 'ManejadorHistorias/historias.html', context)

def consulta(request):
    anioActual = datetime.date.today().year
    diaActual = datetime.datetime.now().day
    mesActual = datetime.datetime.now().month
    lustro = datetime.date(anioActual-5,mesActual,diaActual)
    fecha = datetime.date.today()
    if request.method == 'POST':
        query = str(request.POST.get('query'))
        print(query)
        resultados = Historia.objects.all().exclude(fecha__gte=fecha).filter(fecha__gte=lustro).filter(motivo__icontains=query)
        return render(request, 'ManejadorHistorias/resultados.html', {'resultados': resultados})
    else:
        return render(request, 'ManejadorHistorias/consulta.html')
    
def actualizar(request):
    if request.method == 'POST':
        form = HistoriaForm(request.POST)
        if form.is_valid():
            historia = Historia.objects.get(id_historia=form.cleaned_data['id_historia'])
            
            historia.id_paciente = form.cleaned_data['id_paciente']
            historia.apellidos = form.cleaned_data['apellidos']
            historia.nombres = form.cleaned_data['nombres']
            historia.edad = form.cleaned_data['edad']
            historia.anio_nacimiento = form.cleaned_data['anio_nacimiento']
            historia.motivo = form.cleaned_data['motivo']
            historia.fecha = form.cleaned_data['fecha']
            historia.save()

            return render(request, 'ManejadorHistorias/actualizacion.html')
    else:
        form = HistoriaForm()
    return render(request, 'ManejadorHistorias/actualizacion.html', {'form': form})