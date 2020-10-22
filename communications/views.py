from django.shortcuts import render, HttpResponse, redirect
from twilio.rest import Client
from decouple import config

def index(request):
  # Put log of all emails & Text Messages in here.
  return  HttpResponse("View of all Communications")

def texts(request):
  # Log of all texts & replies.  Turnover/Reply Analysis.
  return render(request,'twilio.html')

def sendMessage(request):
  # account_sid = config('TWILIO_SID')
  # auth_token = config('TWILIO_AUTH')
  # print('Account SID',account_sid,'Auth Token',auth_token)

  if config('TWILIO_ACTIVE')==True:

    client=Client(account_sid,auth_token)
    message = client.messages.create(
      to="+17605323540",
      from_='+12544555888',
      body="Thank you for choosing to \n donate and free our youth \n from this horrible injustice. \n \n Please complete your donation \n by clicking on the link below. \n \n http://54.183.183.188/donations/ \n \n Reply STOP to be \n unsubscribed "
    )
    print('\n Message sent')
  else:
    print('\n Twilio is not active, change in .env \n')
  
  return redirect(texts)