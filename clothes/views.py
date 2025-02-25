from django.shortcuts import render
from . import models
from django.views import generic


class AllClothesView(generic.ListView):
    model = models.Clothes
    template_name = 'clothing/all_clothes.html'
    context_object_name = 'all_clothes'
    queryset = models.Clothes.objects.all().order_by('-id')

# def all_clothes(request):
#     if request.method == 'GET':
#         query = models.Clothes.objects.all().order_by('-id')
#         context_object_name = {
#             'all_clothes': query,
#         }
#         return render(request, template_name='clothing/all_clothes.html', context=context_object_name)


class ChildClothesView(generic.ListView):
    model = models.Clothes
    template_name = 'clothing/child_cloth.html'
    context_object_name = 'child_clothes'

    def get_queryset(self):
        return models.Clothes.objects.filter(tags__name='Детская').order_by('-id')



class TeenClothesView(generic.ListView):
    model = models.Clothes
    template_name = 'clothing/teen_clothes.html'
    context_object_name = 'teen_clothes'

    def get_queryset(self):
        return models.Clothes.objects.filter(tags__name='Подростковая').order_by('-id')



class AdultClothesView(generic.ListView):
    model = models.Clothes
    template_name = 'clothing/adult_cloth.html'
    context_object_name = 'adult_clothes'

    def get_queryset(self):
        return models.Clothes.objects.filter(tags__name='Взрослая').order_by('-id')





# def child_clothes(request):
#     if request.method == 'GET':
#         query = models.Clothes.objects.filter(tags__name='Детская').order_by('-id')
#         context_object_name = {
#             'child_clothes': query,
#         }
#         return render(request, template_name='clothing/child_cloth.html', context=context_object_name)
#
#
# def teen_clothes(request):
#     if request.method == 'GET':
#         query = models.Clothes.objects.filter(tags__name='Подростковая').order_by('-id')
#         context_object_name = {
#             'teen_clothes': query,
#         }
#         return render(request, template_name='clothing/teen_clothes.html', context=context_object_name)
#
#
# def adult_clothes(request):
#     if request.method == 'GET':
#         query = models.Clothes.objects.filter(tags__name='Взрослая').order_by('-id')
#         context_object_name = {
#             'adult_clothes': query,
#         }
#         return render(request, template_name='clothing/adult_cloth.html', context=context_object_name)
