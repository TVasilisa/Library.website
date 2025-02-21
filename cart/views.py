from django.shortcuts import render, redirect
from . import models, forms

def order_view(request):
    if request.method == 'GET':
        query = models.CartModel.objects.all()
        context_object_name = {
            'order': query,
        }
        return render(request, 'cart/order.html', context = context_object_name)

def create_order_view(request):
    if request.method == 'POST':
        form = forms.TodoOrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('order')
    else:
        form = forms.TodoOrderForm()
        return render(request, 'cart/create_order.html', {'form': form})