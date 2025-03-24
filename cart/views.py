from django.shortcuts import render, redirect
from django.views import generic

from . import models, forms


class OrderView(generic.ListView):
    template_name = 'cart/order.html'
    context_object_name = 'order'

    def get_queryset(self):
        return models.CartModel.objects.all()

# def order_view(request):
#     if request.method == 'GET':
#         query = models.CartModel.objects.all()
#         context_object_name = {
#             'order': query,
#         }
#         return render(request, 'cart/order.html', context = context_object_name)


class CreateOrderView(generic.CreateView):
    template_name = 'cart/create_order.html'
    form_class = forms.TodoOrderForm
    success_url = '/order/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateOrderView, self).form_valid(form=form)


# def create_order_view(request):
#     if request.method == 'POST':
#         form = forms.TodoOrderForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('order')
#     else:
#         form = forms.TodoOrderForm()
#         return render(request, 'cart/create_order.html', {'form': form})