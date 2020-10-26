from django.shortcuts import render, HttpResponse
from decouple import config

def index(request):
  return HttpResponse('Hello!')

def navbar(request):
  return render(request,'navbar.html',context)

# Get Donations Page IP Address: Switches in Production
def getRootIP():
  rootIP = config("ROOT_IP")
  print('\n',rootIP,'\n')
  donationsPageAddress = "http://"+rootIP+"/donations/"
  return (donationsPageAddress)

def home(request):
  donationsPage = getRootIP
  context = {
    'donationsPage': donationsPage,
    'pageID': 'home',
    'page_title': 'Home'
  }
  return render(request,'homepage.html',context)

def about(request):
  donationsPage = getRootIP
  context = {
    'donationsPage': donationsPage,
    'pageID': 'about',
    'page_title': 'About'
  }
  return render(request,'about.html',context)

def our_target(request):
  donationsPage = getRootIP
  context = {
    'donationsPage': donationsPage,
    'pageID': 'our_target',
    'page_title': 'Our Target'
  }
  return render(request,'our_target.html',context)

# support is in donations app "current_priorities.html"

def events(request):
  donationsPage = getRootIP
  context = {
    'donationsPage': donationsPage,
    'pageID': 'events',
    'page_title': 'Events'
  }
  return render(request,'events.html',context)

def contact(request):
  donationsPage = getRootIP
  context = {
    'donationsPage': donationsPage,
    'pageID': 'contact',
    'page_title': 'Contact'
  }
  return render(request,'contact.html',context)

def privacy(request):
  return render(request,'privacy.html')