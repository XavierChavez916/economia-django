
from django.shortcuts import render, redirect
from django.http import HttpResponse
import plotly.express as px
from django.shortcuts import render
import numpy as np
from django.shortcuts import render
from .models import IndicadorAmbiental
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from django.contrib import messages

import plotly.offline as pyo
from .forms import MunicipalitySelectionForm, IndicadorSocialForm,IndicadorEconomicoForm, IndicadorAmbientalForm, IndicadorInstitucionalForm
from .models import Municipio, IndicadorAmbiental,IndicadorInstitucional, IndicadorEconomico, IndicadorSocial



# views.py

def agregar_indicador_ambiental(request):
    if request.method == 'POST':
        form = IndicadorAmbientalForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)  # agrega esta impresión
            return redirect('/ambiental/')
        else:
            messages.error(request, 'El formulario no es válido. Por favor verifique los datos ingresados.')
    else:
        form = IndicadorAmbientalForm()
        
    return render(request, 'pages/indicadores/tipo_calculo/formularios/ambiental.html', {'form': form})


def agregar_indicador_institucional(request):
    if request.method == 'POST':
        form = IndicadorInstitucionalForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)  # agrega esta impresión
            return redirect('/institucional/')
        else:
            messages.error(request, 'El formulario no es válido. Por favor verifique los datos ingresados.')
    else:
        form = IndicadorInstitucionalForm()
        
    return render(request, 'pages/indicadores/tipo_calculo/formularios/institucional.html', {'form': form})

def agregar_indicador_economico(request):
    if request.method == 'POST':
        form = IndicadorEconomicoForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)  # agrega esta impresión
            return redirect('/economico/')
        else:
            messages.error(request, 'El formulario no es válido. Por favor verifique los datos ingresados.')
    else:
        form = IndicadorEconomicoForm()
        
    return render(request, 'pages/indicadores/tipo_calculo/formularios/economico.html', {'form': form})


def agregar_indicador_social(request):
    if request.method == 'POST':
        form = IndicadorSocialForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)  # agrega esta impresión
            return redirect('/social/')
        else:
            messages.error(request, 'El formulario no es válido. Por favor verifique los datos ingresados.')
    else:
        form = IndicadorSocialForm()
        
    return render(request, 'pages/indicadores/tipo_calculo/formularios/social.html', {'form': form})


    
def home(request):
    return render(request, 'home.html')

def nuevo_formulario(request):
    municipios = Municipio.objects.all()
    context = {'municipios': municipios}
    return render(request, "pages/tipo_calculo/formularios/ambiental.html", context)

def login(request):
    return render(request, 'auth/login.html')

# Create your views here.

def quienes(request):
    return render(request, "pages/quienes.html")

def contactos(request):
    return render(request, "pages/contactos.html")

# def indicadores(request):
    
#     return render(request, "pages/indicadores/tipo_calculo/forms.html")


def tipoCalculo(request):
    return render(request, "pages/indicadores/tipo_calculo/tipoCalculo.html")

def grafica( request ):
    return render(request, "pages/grafica.html")

# TODO: Formularios

def ambiental(request):
    return render(request, "pages/indicadores/tipo_calculo/formularios/ambiental.html")
def economico(request):
    return render(request, "pages/indicadores/tipo_calculo/formularios/economico.html")
def institucional(request):
    return render(request, "pages/indicadores/tipo_calculo/formularios/institucional.html")
def social(request):
    return render(request, "pages/indicadores/tipo_calculo/formularios/social.html")





def mostrar_subindice(request):
    indicadores = IndicadorAmbiental.objects.all()

    for indicador in indicadores:
        indicador.calculate_subindice()
        
    return render(request, 'template.html', {'indicadores': indicadores})


# TODO: Upload
def upload( request ):
    return render(request, "pages/indicadores/tipo_calculo/upload/upload.html")

# TODO: Subida de los formularios
def guardar_formulario_ambiental(request):
    if request.method == "POST":
        municipio_id = request.POST.get("municipio")
        municipio = Municipio.objects.get(id=municipio_id)
        anio = request.POST.get("anio")
        area_sanitarios = request.POST.get("area_sanitarios")
        num_botaderos = request.POST.get("num_botaderos")
        area_botaderos = request.POST.get("area_botaderos")
        total_residuos_tone = request.POST.get("total_residuos_tone")
        total_residuos_solidos = request.POST.get("total_residuos_solidos")
        total_residuos_peligroso_ton = request.POST.get("total_residuos_peligroso_ton")
        total_residuos_organicos_ton = request.POST.get("total_residuos_organicos_ton")
        total_residuos_inorganicos_ton = request.POST.get("total_residuos_inorganicos_ton")
        total_residuos = request.POST.get("total_residuos")
        residuos_urbanos_reciclaje = request.POST.get("residuos_urbanos_reciclaje")

        indicador_ambiental = IndicadorAmbiental(
            municipio=municipio,
            anio=anio,
            area_sanitarios=area_sanitarios,
            num_botaderos=num_botaderos,
            area_botaderos=area_botaderos,
            total_residuos_tone=total_residuos_tone,
            total_residuos_solidos=total_residuos_solidos,
            total_residuos_peligroso_ton=total_residuos_peligroso_ton,
            total_residuos_organicos_ton=total_residuos_organicos_ton,
            total_residuos_inorganicos_ton=total_residuos_inorganicos_ton,
            total_residuos=total_residuos,
            residuos_urbanos_reciclaje=residuos_urbanos_reciclaje,
        )
        indicador_ambiental.save()
        return redirect("listar_formularios")
    else:
        municipios = Municipio.objects.all()
        return render(request, "pages/indicadores/tipo_calculo/formularios/ambiental.html", {"municipios": municipios})




# TODO: Mostrar Graficas
# vista de Django
def grafico_municipios(request):

    
    # Obtener el indicador seleccionado por el usuario
    if 'indicador' in request.GET:
        indicador = request.GET.get('indicador')
    else:
        # Asignar un valor predeterminado para 'indicador' si no está definido
        indicador = 'economico'

    # Obtener el año seleccionado por el usuario
    if 'anio' in request.GET:
        anio = request.GET.get('anio')
    else:
        # Asignar un valor predeterminado para 'year' si no está definido
        anio = 2020
    
    # Obtener todos los municipios
    municipios = Municipio.objects.all()
    data = []
    
    # Recorrer los municipios y obtener el indicador específico
    for municipio in municipios:
        if indicador == 'economico':
            try:
                indicador_seleccionado = IndicadorEconomico.objects.get(municipio=municipio, anio=anio)
            except IndicadorEconomico.DoesNotExist:
                continue
        elif indicador == 'social':
            try:
                indicador_seleccionado = IndicadorSocial.objects.get(municipio=municipio, anio=anio)
            except IndicadorSocial.DoesNotExist:
                continue
        elif indicador == 'institucional':
            try:
                indicador_seleccionado = IndicadorInstitucional.objects.get(municipio=municipio, anio=anio)
            except IndicadorInstitucional.DoesNotExist:
                continue
        elif indicador == 'ambiental':
            try:
                indicador_seleccionado = IndicadorAmbiental.objects.get(municipio=municipio, anio=anio)
            except IndicadorAmbiental.DoesNotExist:
                continue



        data.append({
            'municipio': municipio.nombre,
            'subindice': indicador_seleccionado.subindice
        })
    if not data:
        context = {
            'message': 'No se encontraron datos para el año seleccionado.'
        }
        return render(request, 'grafico_municipios.html', context)
    
    # Ordenar los datos por subíndice
    data = sorted(data, key=lambda x: x['subindice'])
    
    # Obtener los 5 mejores y peores municipios
    mejores_municipios = data[-5:]
    peores_municipios = data[:5]
    
    if 'tipo_grafico' in request.GET:
        tipo_grafico = request.GET.get('tipo_grafico')
    else:
        # Asignar un valor predeterminado para 'tipo_grafico' si no está definido
        tipo_grafico = 'bar'

    # Crear dos gráficas, una para los 5 mejores y otra para los 5 peores
    if tipo_grafico == 'bar':
        fig_mejores = px.bar(mejores_municipios, x='municipio', y='subindice', color='municipio')
        fig_peores = px.bar(peores_municipios, x='municipio', y='subindice', color='municipio')
    elif tipo_grafico == 'pie':
       
        fig_mejores = px.pie(mejores_municipios, values='subindice', names='municipio')

        fig_peores = px.pie(peores_municipios, values='subindice', names='municipio')
        fig_mejores.update_traces(textposition='inside', textinfo='value+percent')
        fig_peores.update_traces(textposition='inside', textinfo='value+percent')
       




    
    grafico_mejores = pyo.plot(fig_mejores, auto_open=False, output_type='div')
    grafico_peores = pyo.plot(fig_peores, auto_open=False, output_type='div')


    context = {
        'grafico_mejores': grafico_mejores,
        'grafico_peores': grafico_peores
    }
    return render(request, 'grafico_municipios.html', context)

def seleccion_municipio(request):
    if 'municipality' in request.GET:
        municipality_id = request.GET.get('municipality')
    else:
        # Asignar un valor predeterminado para 'municipality' si no está definido
        municipality_id = None
    
    if 'tipo_grafico' in request.GET:
        tipo_grafico = request.GET.get('tipo_grafico')
    else:
        # Asignar un valor predeterminado para 'tipo_grafico' si no está definido
        tipo_grafico = 'pie'

    

    municipalities = Municipio.objects.all()
    context = {'municipalities': municipalities}

    if municipality_id:
        municipality = Municipio.objects.get(pk=municipality_id)
        economic_indicators = IndicadorEconomico.objects.filter(municipio=municipality)
        social_indicators = IndicadorSocial.objects.filter(municipio=municipality)
        environmental_indicators = IndicadorAmbiental.objects.filter(municipio=municipality)
        institutional_indicators = IndicadorInstitucional.objects.filter(municipio=municipality)
        
        data = []
        for economic_indicator in economic_indicators:
            data.append({
            'indicator': 'Economic',
            'subindex': economic_indicator.subindice,
           
            })
        for social_indicator in social_indicators:
            data.append({
            'indicator': 'Social',
            'subindex': social_indicator.subindice,
           
            })
        for environmental_indicator in environmental_indicators:
            data.append({
            'indicator': 'Environmental',
            'subindex': environmental_indicator.subindice,
           
            })
        for institutional_indicator in institutional_indicators:
            data.append({
            'indicator': 'Institutional',
            'subindex': institutional_indicator.subindice,
           
            })
        
        fig = px.bar(data, x="indicator", y="subindex", color="indicator")

        if tipo_grafico == 'bar':
            fig = px.bar(data, x="indicator", y="subindex", color="indicator")
            
        elif tipo_grafico == 'pie':
            fig = px.pie(data, names="indicator", values="subindex")
          
        grafico = pyo.plot(fig, auto_open=False, output_type='div')
        context['grafico'] = grafico

    return render(request, 'seleccion_municipio.html', context)











def select_municipality(request):
    if request.method == 'POST':
        form = MunicipalitySelectionForm(request.POST)
        if form.is_valid():
            municipio = form.cleaned_data['municipio']
            indicadores_institucionales = IndicadorInstitucional.objects.filter(municipio=municipio)
            indicadores_economicos = IndicadorEconomico.objects.filter(municipio=municipio)
            indicadores_sociales = IndicadorSocial.objects.filter(municipio=municipio)
            indicadores_ambientales = IndicadorAmbiental.objects.filter(municipio=municipio)

            # Cálculo de subíndices para cada tipo de indicador
            for indicador in indicadores_institucionales:
                indicador.calculate_subindice()
            for indicador in indicadores_economicos:
                indicador.calculate_subindice()
            for indicador in indicadores_sociales:
                indicador.calculate_subindice()
            for indicador in indicadores_ambientales:
                indicador.calculate_subindice()

            # Creación de las gráficas
            institucional_chart = create_bar_chart(indicadores_institucionales)
            economico_chart = create_bar_chart(indicadores_economicos)
            social_chart = create_bar_chart(indicadores_sociales)
            ambiental_chart = create_bar_chart(indicadores_ambientales)

            # Renderización de la plantilla con los indicadores seleccionados
            return render(request, 'select_municipality.html', {
                'indicadores_institucionales': institucional_chart,
                'indicadores_economicos': economico_chart,
                'indicadores_sociales': social_chart,
                'indicadores_ambientales': ambiental_chart,
            })
    else:
        form = MunicipalitySelectionForm()

    return render(request, 'select_municipality.html', {'form': form})


def create_bar_chart(indicadores):
    # Recopilar los datos de los subíndices de los indicadores
    subindices = [indicador.subindice for indicador in indicadores]
    nombres = [indicador.nombre for indicador in indicadores]

    # Crear el gráfico de barras
    fig = px.bar(x=nombres, y=subindices)

    return fig

# def seleccion_municipio(request):
   
#     municipality = request.GET.get('municipality')
#     municipalities = Municipio.objects.all()
#     context = {'municipalities': municipalities}
#     if municipality:
#         print('hola')
#         # aquí debes acceder a tus datos y filtrarlos por el municipio seleccionado
#         data = Indicador.objects.filter(municipality__name=municipality)
#         fig = px.bar(data, x="subindex", y="value", color="indicator")
#         context['fig'] = fig
#     return render(request, 'seleccion_municipio.html', context)
