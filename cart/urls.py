from django.urls import path

from clothes.urls import urlpatterns
from . import views

urlpatterns = [
    path('order/', views.order_view, name='order'),
    path('create_order/', views.create_order_view, name='create_order'),
]