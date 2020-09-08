from django.shortcuts import render, HttpResponse

def index(request):
  return HttpResponse("Donations App")

def display(request):
  return render(request,"display.html")