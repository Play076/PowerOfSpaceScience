from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
import os

def index(request):
    context={"Message": "Teste"}
    return render(request, "index.html", context)

def USAGraphic(request):
    state = []
    deaths = []
    cases = []
    deathRatios = []
    result = pd.read_excel(os.path.join("C:/Users/user/Documents/NASA_Challange/models/", "USA.xlsx"), engine='openpyxl',)
    newResult = pd.DataFrame(result, columns=['Location', 'Deaths', 'Cases', 'death ratios'])
    tratesDeaths = newResult[newResult['Deaths'] == '-'].index
    newResult.drop(tratesDeaths, inplace=True)

    state = [location for location in newResult['Location']]

    deaths = pd.DataFrame([location for location in newResult['Deaths']])
    deaths = deaths.dropna()
    deaths = deaths.values.tolist()

    cases = pd.DataFrame([location for location in newResult['Cases']])
    cases = cases.dropna()
    cases = cases.values.tolist()

    deathRatios = pd.DataFrame([location for location in newResult['death ratios']])
    deathRatios = deathRatios.dropna()
    deathRatios = deathRatios.values.tolist()
    return render(request, "USA.html", {"state": state, "deaths": deaths, "cases": cases, "deathratios": deathRatios})

def BRGraphic(request):
    state = []
    deaths = []
    cases = []
    deathRatios = []
    result = pd.read_excel(os.path.join("C:/Users/user/Documents/NASA_Challange/models/", "Brazil.xlsx"), engine='openpyxl',)
    newResult = pd.DataFrame(result, columns=['Location', 'Deaths', 'Cases', 'death ratios'])
    tratesDeaths = newResult[newResult['Deaths'] == '-'].index
    newResult.drop(tratesDeaths, inplace=True)

    state = [location for location in newResult['Location']]

    deaths = pd.DataFrame([location for location in newResult['Deaths']])
    deaths = deaths.dropna()
    deaths = deaths.values.tolist()

    cases = pd.DataFrame([location for location in newResult['Cases']])
    cases = cases.dropna()
    cases = cases.values.tolist()

    deathRatios = pd.DataFrame([location for location in newResult['death ratios']])
    deathRatios = deathRatios.dropna()
    deathRatios = deathRatios.values.tolist()
    return render(request, "BR.html", {"state": state, "deaths": deaths, "cases": cases, "deathratios": deathRatios})

def GERMANYGraphic(request):
    state = []
    deaths = []
    cases = []
    deathRatios = []
    result = pd.read_excel(os.path.join("C:/Users/user/Documents/NASA_Challange/models/", "Brazil.xlsx"), engine='openpyxl',)
    newResult = pd.DataFrame(result, columns=['Location', 'Deaths', 'Cases', 'death ratios'])
    tratesDeaths = newResult[newResult['Deaths'] == '-'].index
    newResult.drop(tratesDeaths, inplace=True)

    state = [location for location in newResult['Location']]

    deaths = pd.DataFrame([location for location in newResult['Deaths']])
    deaths = deaths.dropna()
    deaths = deaths.values.tolist()

    cases = pd.DataFrame([location for location in newResult['Cases']])
    cases = cases.dropna()
    cases = cases.values.tolist()

    deathRatios = pd.DataFrame([location for location in newResult['death ratios']])
    deathRatios = deathRatios.dropna()
    deathRatios = deathRatios.values.tolist()
    return render(request, "GERMANY.html", {"state": state, "deaths": deaths, "cases": cases, "deathratios": deathRatios})

def ALGERIAGraphic(request):
    state = []
    deaths = []
    cases = []
    deathRatios = []
    result = pd.read_excel(os.path.join("C:/Users/user/Documents/NASA_Challange/models/", "Brazil.xlsx"), engine='openpyxl',)
    newResult = pd.DataFrame(result, columns=['Location', 'Deaths', 'Cases', 'death ratios'])
    tratesDeaths = newResult[newResult['Deaths'] == '-'].index
    newResult.drop(tratesDeaths, inplace=True)

    state = [location for location in newResult['Location']]

    deaths = pd.DataFrame([location for location in newResult['Deaths']])
    deaths = deaths.dropna()
    deaths = deaths.values.tolist()

    cases = pd.DataFrame([location for location in newResult['Cases']])
    cases = cases.dropna()
    cases = cases.values.tolist()

    deathRatios = pd.DataFrame([location for location in newResult['death ratios']])
    deathRatios = deathRatios.dropna()
    deathRatios = deathRatios.values.tolist()
    return render(request, "ALGERIA.html", {"state": state, "deaths": deaths, "cases": cases, "deathratios": deathRatios})

def INDIAGraphic(request):
    state = []
    deaths = []
    cases = []
    deathRatios = []
    result = pd.read_excel(os.path.join("C:/Users/user/Documents/NASA_Challange/models/", "Brazil.xlsx"), engine='openpyxl',)
    newResult = pd.DataFrame(result, columns=['STATE/UTS', 'DEATHS', 'TOTAL CASES', 'DEATH RATIO'])
    tratesDeaths = newResult[newResult['DEATHS'] == '-'].index
    newResult.drop(tratesDeaths, inplace=True)

    state = [location for location in newResult['STATE/UTS']]

    deaths = pd.DataFrame([location for location in newResult['DEATHS']])
    deaths = deaths.dropna()
    deaths = deaths.values.tolist()

    cases = pd.DataFrame([location for location in newResult['TOTAL CASES']])
    cases = cases.dropna()
    cases = cases.values.tolist()

    deathRatios = pd.DataFrame([location for location in newResult['DEATH RATIO']])
    deathRatios = deathRatios.dropna()
    deathRatios = deathRatios.values.tolist()
    return render(request, "INDIA.html", {"state": state, "deaths": deaths, "cases": cases, "deathratios": deathRatios})