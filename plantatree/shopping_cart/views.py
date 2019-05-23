from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

from store.models import Tree

from shopping_cart.extras import generate_order_id
from shopping_cart.models import OrderItem, Order

# Create your views here.
def add_to_cart(request, **kwargs):
    product = Tree.objects.filter(id=kwargs.get('item_id', "")).first()
    order_item, status = OrderItem.objects.get_or_create(product=product)
    user_order, status = Order.objects.get_or_create(is_ordered=False)
    user_order.items.add(order_item)
    if status:
        user_order.ref_code = generate_order_id()
        user_order.save()
        
    messages.info(request, "item added to cart")
    return redirect(reverse('home:home'))

def delete_from_cart(request, item_id):
    print("Here")
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('shopping_cart:order_summary'))

def order_details(request, **kwargs):
    order = Order.objects.filter(is_ordered=False)
    if order.exists():
        existing_order = order[0]
    else:
        existing_order = 0
    context = {
        'order': existing_order
    }
    return render(request, 'order_summary.html', context)
