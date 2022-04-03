from django.shortcuts import render
from twoapp.models import WoodBuildings

def buildPage(request):
    allObects = WoodBuildings.objects.all()
    params = { "build":allObects}
    return render (request, "buildings.html", params)

def CurrentBuild(request):
    return "Currnt Build"
