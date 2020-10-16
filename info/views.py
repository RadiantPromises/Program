from django.shortcuts import render, HttpResponse

def index(request):
  return HttpResponse('Hello!')

def home(request):
  return render(request,'homepage.html')

def about(request):
  return render(request,'about.html')

def our_target(request):
  return render(request,'our_target.html')

def events(request):
  return render(request,'events.html')

def contact(request):
  return HttpResponse('Contact')