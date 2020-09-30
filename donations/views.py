from django.shortcuts import render, HttpResponse,redirect
from django.template.defaulttags import register
from profiles.models import User
import json
import os

@register.filter
def get_range(value):
  return range(value)

def index(request):
  users = User.objects.all()

  if 'cart' in request.session:
    print("\nCart in session")
    # items_in_cart = json.loads(request.session['cart'])["items_in_cart"]
    print(json.loads(request.session['cart']),"\n")
    # request.session['cart']
  # else:
  #   items_in_cart = ""
  
  context = {
    'users':users,
    # 'items_in_cart':items_in_cart
  }

  # print('\n OS Environment:',os.environ.get['TOAST'],'\n')
  # TOASTY = os.environ.get('TOAST')
  # print('\n Secret Key:',TOASTY,"\n")
  return render(request,"current_priorities.html",context)
  
def addToCart(request):
  
  # Check to see if there is a cart
  if 'cart' not in request.session:
    items_in_cart = 0
    current_cart = {
      "items": [],
      "items_in_cart":items_in_cart
    }
  else:
    current_cart = json.loads(request.session['cart'])
    items_in_cart = current_cart["items_in_cart"]

  new_cart_item = {
    "cart_item_id" : items_in_cart + 1,
    "cost_id": request.POST['cost_id'],
    "title": request.POST['title'],
    "description": request.POST['description'],
    "quantity": request.POST['quantity'],
    "full_cost": request.POST['full_cost'],
    "partial_cost": request.POST['partial_cost'],
    "reoccurance_date": request.POST['reoccurance_date']

    # "amount" : request.POST['donation-amount'],
    # "remainder" : request.POST['donation-remainder'],
    # "years": request.POST['donation-years']
  }

  print(new_cart_item)
  current_cart["items"].append(new_cart_item)
  current_cart["items_in_cart"] = len(current_cart["items"])

  # Store Cart Data in Session
  request.session['cart'] = json.dumps(current_cart)
  return redirect(cart,permanent=True)

def removeFromCart(request,cost_id):
  print("\nRemove From Cart:",cost_id)
  return redirect(index)

def emptyCart(request):
  request.session.flush()
  return redirect(index)

def cart(request):
  if 'cart' in request.session:
    current_cart = json.loads(request.session['cart'])
  else:
    current_cart = "Your Cart is empty"
  context = {
    "cart": current_cart
  }
  return render(request,"cart.html",context)


# Where to store Cart Data https://stackoverflow.com/questions/2827764/ecommerceshopping-cartwhere-should-i-store-shopping-cart-data-in-session-or