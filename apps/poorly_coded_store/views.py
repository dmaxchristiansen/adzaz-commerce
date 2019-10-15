from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    context = {
        "order": Order.objects.last()
        }
    context['totalOrders'] = 0
    context['totalMoney'] = 0
    orders = Order.objects.all()
    for i in orders:
        context['totalOrders']+=i.quantity_ordered
        context['totalMoney']+=i.total_price
    print("Charging credit card...")
    return render(request, "store/checkout.html", context)

def process(request):
    quantity_from_form = int(request.POST["quantity"])
    id_from_form = int(request.POST["id"])
    product = Product.objects.get(id=id_from_form)
    price_from_form = product.price
    total_price=quantity_from_form*price_from_form
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_price)
    return redirect("/checkout")