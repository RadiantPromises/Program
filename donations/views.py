from django.shortcuts import render, HttpResponse,redirect
from profiles.models import User
import json

def index(request):
  users = User.objects.all()

  if 'cart' in request.session:
    items_in_cart = len(json.loads(request.session['cart'])["items"])
    # request.session['cart']
  else:
    items_in_cart = ""
  
  context={
    'users':users,
    'items_in_cart':items_in_cart
  }
  return render(request,"display.html",context)
  
def addToCart(request):
  
  # Check to see if there is a cart
  if 'cart' not in request.session:
    current_cart = {
      "items": [],
      # "items_in_cart":0
    }
  else:
    current_cart = json.loads(request.session['cart'])
  
  new_cart_item = {
    # Include quantity
    "cost_id": request.POST['cost_id'],
    "amount" : request.POST['donation-amount'],
    "remainder" : request.POST['donation-remainder'],
    "years": request.POST['donation-years']
  }
  current_cart["items"].append(new_cart_item)
  # current_cart["items_in_cart"]

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