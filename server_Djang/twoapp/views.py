from django.shortcuts import render
from twoapp.models import Building

def buildPage(request):
    allObects = Building.objects.all()
    params = { "build":allObects}
    return render (request, "buildings.html", params)

def CurrentBuild(request, buildName):
    selected = Building.objects.all().filter(namename=buildName)
    Buildings = selected[0]
    parametr = { "key_build" : Buildings }
    return render (request, "wood.html", parametr)
