from django.shortcuts import render, HttpResponse, redirect
from django.template.defaulttags import register
from profiles.models import User
from decouple import config
import stripe
import json

@register.filter
def get_range(value):
  return range(value)

# def index(request):
#   stripe.api_key = config('STRIPE_KEY')

#   paymentIntent=stripe.PaymentIntent.create(
#     amount='0100',
#     currency='usd',
#     description = 'Initial Payment Intent',
#     payment_method_types=['card']
#   )

#   print("\n ",paymentIntent.client_secret, "\n")

#   context = {
#     'clientSecret' : paymentIntent.client_secret
#     }
#   return render(request,"current_priorities.html",context)

def index(request):
  return render(request,"current_priorities.html")

def stripeTesting(request):
  stripe.api_key = config('STRIPE_KEY')
  return render(request,"stripe_testing.html")

def updatePaymentIntent(request):
  paymentIntent=stripe.PaymentIntent.create(
    amount='0100',
    currency='usd',
    description = 'Initial Payment Intent',
    payment_method_types=['card']
  )


  updatedAmount = request.POST['amount']
  clientSecret = request.POST['clientSecret']
  stripe.api_key = config('STRIPE_KEY')
  paymentIntentID = stripe.PaymentIntent.retrieve(clientSecret).id
  print('\n',updatedAmount,clientSecret,paymentIntentID,'\n')
  # stripe.PaymentIntent.modify(paymentIntentID, amount=updatedAmount)
  return HttpResponse("Payment Intent Updated" )

def stripePayment(request):
  print("\n Stripe payment initiated \n")
  stripe.api_key = config('STRIPE_KEY')

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



  # print(PIntent.client_secret)
  # print(stripe.Balance.retrieve())
  # if stripe.error:
  #   print("There is an error")
    # print(stripe.error.message)
  # print(stripe.error.code)

  # Cust=stripe.Customer.create(
  #   balance="0",
  #   description="My First Test Customer (created for API docs)",)
  # print("Customer",Cust)
  # print(stripe.Customer.retrieve("cus_I7ouXX8a4Hr59e"))

  # Charge = stripe.Charge.create(
  #   amount=200,
  #   customer="cus_I7ouXX8a4Hr59e",
  #   currency="usd",
  #   source="tok_visa",
  #   description="My First Test Charge (created for API docs)",)
  # print(Charge)

# Payment succeeds 4242 4242 4242 4242
# Payment requires authentication 4000 0025 0000 3155
# Payment is declined 4000 0000 0000 9995

  # print(stripe.Customer.list(limit=3))

  # EVENTS
  # print(stripe.Event.list(limit=100))
  return redirect(index)


# Where to store Cart Data https://stackoverflow.com/questions/2827764/ecommerceshopping-cartwhere-should-i-store-shopping-cart-data-in-session-or