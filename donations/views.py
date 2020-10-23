from django.shortcuts import render, HttpResponse, redirect
from django.template.defaulttags import register
from django.template import Context
from profiles.models import User
from twilio.rest import Client
from decouple import config
import stripe
import json

@register.filter
def get_range(value):
  return range(value)

def index(request):
  stripe.api_key = config('STRIPE_KEY')
  fundsGoal = 10000
  # fundsRaised = stripe.Balance.retrieve().pending[0].amount/100
  fundsRaised = 9000
  fundsRequired = fundsGoal-fundsRaised
  print('\n Funds Raised',fundsRaised,type(fundsRaised))
  percentageRaised = (fundsRaised/fundsGoal)*100
  percentageRequired = 99-percentageRaised # Leave 1 px to fit on same line
  total = percentageRaised + percentageRequired
  print('Percentage Raised:',percentageRaised, 'Percentage Required',percentageRequired,'Total:',total,'\n')



  context = {
    'page': "support",
    'percentageRaised' : percentageRaised,
    'percentageRequired' : percentageRequired,
    'fundsRaised':  f"{fundsRaised:,}",
    'fundsRequired':  f"{fundsRequired:,}"
  }
  return render(request,"support.html",context)

def phases(request):
  return render(request,"phases.html")

def stripeTesting(request):
  stripe.api_key = config('STRIPE_KEY')
  return render(request,"stripe_testing.html")

def updatePaymentIntent(request):
  return HttpResponse("Payment Intent Updated" )

# Process a stripe Payment (Method, Intent, Customer, Confirm)
def stripePayment(request):
  print("\n Stripe payment initiated \n")
  stripe.api_key = config('STRIPE_KEY')
  stripeToken = request.POST['stripeToken']
  print("Stripe Token:",stripeToken)

  # Create Payment Method (From Token)
  paymentMethod = stripe.PaymentMethod.create(
    type='card',
    card= {'token':stripeToken}
  )
  print('Payment Method Created', paymentMethod.id, type(paymentMethod.id))

  # Create Payment Intent
  giveAmount = request.POST['giveAmount']
  stripeAmount = int(giveAmount)*100
  print('Give Amount:', giveAmount,type(giveAmount), 'Stripe Amount:',stripeAmount,type(stripeAmount))
  paymentIntent=stripe.PaymentIntent.create(
    amount=stripeAmount,
    currency='usd',
    description = 'Server Payment Intent',
    payment_method = paymentMethod.id
  )
  print('Payment Intent Created',paymentIntent.id)
  print('Payment Intent amount',paymentIntent.amount)
  print('Payment Intent method',paymentIntent.payment_method)

  # Confirm Payment
  paymentIntentConfirmation = stripe.PaymentIntent.confirm(
    paymentIntent.id
  )
  print('Payment Intent Confirmed',paymentIntentConfirmation.id,paymentIntentConfirmation.status)


  print('End Payment Session \n')
  return render(request,'payment_success.html')


# Where to store Cart Data https://stackoverflow.com/questions/2827764/ecommerceshopping-cartwhere-should-i-store-shopping-cart-data-in-session-or

