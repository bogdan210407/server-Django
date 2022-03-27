from django.shortcuts import render
def buildPage(request):
    return render (request, "buildings.html")
