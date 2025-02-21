from datetime import datetime
from idlelib import query

from django.shortcuts import render, get_object_or_404, redirect

from . import models, forms
from django.http import HttpResponse

#review
def create_review_view(request):
    if request.method == 'POST':
        form = forms.CreateReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            book_id = review.choice_book.id
            return redirect('book_detail', id=book_id)
    else:
        form = forms.CreateReviewForm
        return render(request, 'review_form.html', {'form': form})

# books list
def book_list_view(request):
    if request.method == 'GET':
        query = models.BookModel.objects.all().order_by('-id')
        context_object_name = {
            'books': query,
        }
        return render(request, template_name='book.html', context=context_object_name)

#book details
def book_detail_view(request, id):
    if request.method == 'GET':
        query = get_object_or_404(models.BookModel, id=id)
        context_object_name = {
            'book_id': query,
        }
        return render(request, template_name='book_detail.html', context=context_object_name)


def about_me(request):
    if request.method == 'GET':
        return HttpResponse('Меня зовет Василиса, учусь на направлении Backend')


def text_and_photo(request):
    if request.method == 'GET':
        return HttpResponse('<img src="https://cs6.pikabu.ru/post_img/2014/05/15/10/1400167833_1703122734.jpg"/>')


def system_time(request):
    if request.method == 'GET':
        current_time = datetime.today()
        return HttpResponse(current_time)
