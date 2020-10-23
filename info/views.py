from django.shortcuts import render, HttpResponse

def index(request):
  return HttpResponse('Hello!')

def navbar(request):
  return render(request,'navbar.html')

def home(request):
  context = {
    'pageID': 'home',
    'page_title': 'Home'
  }
  return render(request,'homepage.html',context)

def about(request):
  context = {
    'pageID': 'about',
    'page_title': 'About'
  }
  return render(request,'about.html',context)

def our_target(request):
  context = {
    'pageID': 'our_target',
    'page_title': 'Our Target'
  }
  return render(request,'our_target.html',context)

# support is in donations app "current_priorities.html"

def events(request):
  context = {
    'pageID': 'events',
    'page_title': 'Events'
  }
  return render(request,'events.html',context)

def contact(request):
  context = {
    'pageID': 'contact',
    'page_title': 'Contact'
  }
  return render(request,'contact.html',context)