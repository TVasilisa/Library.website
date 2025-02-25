from modulefinder import AddPackagePath

from django.urls import path

from . import views
from .views import AllClothesView, ChildClothesView, TeenClothesView, AdultClothesView

urlpatterns = [
    path('all_clothes/', AllClothesView.as_view(), name='all_clothes'),
    path('child_clothes/', ChildClothesView.as_view(), name='child_clothes'),
    path('teen_clothes/', TeenClothesView.as_view(), name='teen_clothes'),
    path('adult_clothes/', AdultClothesView.as_view(), name='adult_clothes'),
]
