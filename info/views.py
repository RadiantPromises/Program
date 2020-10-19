from django.shortcuts import render, HttpResponse

def index(request):
  return HttpResponse('Hello!')

def navbar(request):
  return render(request,'navbar.html')

def home(request):
  context = {
    'page': 'home'
  }
  return render(request,'homepage.html',context)

def about(request):
  context = {
    'page': 'about'
  }
  return render(request,'about.html',context)

def our_target(request):
  context = {
    'page': 'our_target'
  }
  return render(request,'our_target.html',context)

def events(request):
  context = {
    'page': 'events'
  }
  return render(request,'events.html',context)

def contact(request):
  context = {
    'page': 'contact'
  }
  return HttpResponse('Contact',context)