from django.shortcuts import render, HttpResponse

def index(request):
  return HttpResponse('Hello!')

def home(request):
  return render(request,'homepage.html')

def about(request):
  return render(request,'about.html')
