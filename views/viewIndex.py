from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
import os

def index(request):
    context={"Message": "Teste"}
    return render(request, "index.html", context)

def readfile(request):
    state = []
    deaths = []
    cases = []
    deathRatios = []
    result = pd.read_excel(os.path.join("C:/Users/user/Documents/NASA_Challange/models/", "USA.xlsx"), engine='openpyxl',)
    #graph = gp.get_plot(result['Location'], result['Deaths'], result['Cases'], result['death ratios'])
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
    deathRatios = [location for location in newResult['death ratios']]
    return render(request, "index.html", {"state": state, "deaths": deaths, "cases": cases, "deathRatios": deathRatios})