from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from .models import *
from .forms import CreateUserForm
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
      
# Create your views here.
@login_required
def home(request):
   
   if request.user.is_authenticated:
       customer = request.user.customer
       order, created = Order.objects.get_or_create(customer=customer, complete=False)
       items = order.orderitem_set.all()
       cartItems = order.get_cart_items
   else:
       items=[]
       order = {'get_cart_total':0,'get_cart_items':0}
       cartItems = order['get_cart_items']

   yerbas=Yerbas.objects.all()
   return render(request, "home.html", {'yerbas':yerbas, 'cartItems': cartItems})

def authView(request):
    if request.method == "POST":
      form = UserCreationForm(request.POST or None)
      if form.is_valid():
         form.save()
         return redirect("base:login")
    else:  
     form = CreateUserForm()
    return render(request, "registration/signup.html", {"form": form})

def future(request):
    return render(request, 'future.html', {})


def cart(request):
   if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
   else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
   return render(request, "cart.html", {'items':items, 'order':order,'cartItems': cartItems})

def logout_view(request):
        logout(request)
        return redirect('base:home')  

@csrf_exempt
def updateItem(request):
    try:
        data = json.loads(request.body)
        yerbaId = data['yerbaId']
        action = data['action']

        print('Action:', action)
        print('yerbaId:', yerbaId)
        
        customer = request.user.customer
        yerba = Yerbas.objects.get(id=yerbaId)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        orderItem, created = OrderItem.objects.get_or_create(order=order, yerba=yerba)

        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)
        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)

        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()

        return JsonResponse('Item was added', safe=False)
    except Exception as e:
        print(f"Error: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500, safe=False)



