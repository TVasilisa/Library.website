from django.urls import path

from clothes.urls import urlpatterns
from . import views
from .views import OrderView, CreateOrderView

urlpatterns = [
    path('order/', OrderView.as_view(), name='order'),
    path('create_order/', CreateOrderView.as_view(), name='create_order'),
]