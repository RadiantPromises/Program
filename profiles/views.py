from django.shortcuts import render, HttpResponse
from profiles.models import User

def index(request):
  users = User.objects.all()
  # print(users[0].first_name)
  context={
    'users' : users
  }
  return render(request,"profileList.html",context)
