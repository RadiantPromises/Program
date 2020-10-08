from django.shortcuts import render, HttpResponse, redirect
from django.template.defaulttags import register
from django.template import Context
from profiles.models import User
from decouple import config
import stripe
import json

@register.filter
def get_range(value):
  return range(value)

# def index(request):
#   stripe.api_key = config('STRIPE_KEY')



#   print("\n ",paymentIntent.client_secret, "\n")

#   context = {
#     'clientSecret' : paymentIntent.client_secret
#     }
#   return render(request,"current_priorities.html",context)

def index(request):
  stripe.api_key = config('STRIPE_KEY')
  fundsGoal = 10000
  fundsRaised = stripe.Balance.retrieve().pending[0].amount/100
  # fundsRaised = 9000
  fundsRequired = fundsGoal-fundsRaised
  print('\n Funds Raised',fundsRaised,type(fundsRaised))
  percentageRaised = (fundsRaised/fundsGoal)*100
  percentageRequired = 99-percentageRaised # Leave 1 px to fit on same line
  total = percentageRaised + percentageRequired
  print('Percentage Raised:',percentageRaised, 'Percentage Required',percentageRequired,'Total:',total,'\n')

# f"{number:,}"

  context = {
    'percentageRaised' : percentageRaised,
    'percentageRequired' : percentageRequired,
    'fundsRaised':  f"{fundsRaised:,}",
    'fundsRequired':  f"{fundsRequired:,}"
  }
  return render(request,"current_priorities.html",context)

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



# Check to see if customer exists

  # customer = stripe.Customer.create(
  #   name = request.POST['name_on_card'] ,
  #   description = "test Customer2",
  #   email = request.POST['email_address'],
  #   phone = request.POST['phone_number'],
  #   address = {
  #     "line1" : request.POST['address_line_1'],
  #     "line2" : request.POST['address_line_2'],
  #     "city" : request.POST['address_city'],
  #     "state" : request.POST['address_state'],
  #     "postal_code" : request.POST['address_postal_code'],
  #     "country" : 'United States'
  #   }
  # )

# Payment succeeds 4242 4242 4242 4242
# Payment requires authentication 4000 0025 0000 3155
# Payment is declined 4000 0000 0000 9995

  # print(stripe.Customer.list(limit=3))

  # EVENTS
  # print(stripe.Event.list(limit=100))
  print('End Payment Session \n')
  return render(request,'payment_success.html')


# Where to store Cart Data https://stackoverflow.com/questions/2827764/ecommerceshopping-cartwhere-should-i-store-shopping-cart-data-in-session-or