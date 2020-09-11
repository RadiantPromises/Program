from django.shortcuts import render, HttpResponse

def index(request):
  return HttpResponse("Hello Users!")

def profileList(request):
  return render(request,"profileList.html")
