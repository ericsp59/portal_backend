from django.shortcuts import render
from .models import Order

from .forms import OrderForm

# Create your views here.

def first_page(request):
    order_form = OrderForm()
    object_list = Order.objects.all()
    return render(request, './index.html', {
        'object_list': object_list,
        'order_form': order_form
    })

def form_response(request):
    name = request.POST['name']
    phone = request.POST['phone']

    element = Order(order_name = name, order_phone = phone)
    element.save()
    return render(request, './form_response_page.html', {
        'name': name,
        'phone': phone
    })
 