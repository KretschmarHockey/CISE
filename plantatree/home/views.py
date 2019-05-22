from django.shortcuts import render

from store.models import Tree
from shopping_cart.models import Order

# Create your views here.

def home(request):
    object_list = Tree.objects.all()
    filtered_orders = Order.objects.filter(is_ordered=False)
    for product in object_list:
        product.price = product.price / 100
    current_order_products = []
    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.items.all()
        current_order_products = [product.product for product in user_order_items]

    context = {
        'object_list': object_list,
        'current_order_products' : current_order_products
    }

    return render(request, "home/home.html", context)

def about(request):
    return render(request, 'home/about.html', {'title': 'About'})