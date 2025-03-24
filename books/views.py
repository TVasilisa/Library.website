from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from books.models import ReviewModel, BookModel
from . import forms, models


# review
class CreateReviewView(generic.CreateView):
    model = ReviewModel
    form_class = forms.CreateReviewForm
    template_name = 'review_form.html'
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateReviewView, self).form_valid(form=form)


# book list
class BookListView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'books'
    model = BookModel

    def get_queryset(self):
        return BookModel.objects.all().order_by('-id')


# book detail
class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self):
        return get_object_or_404(models.BookModel, pk=self.kwargs.get('pk'))




# attempt to find
class SearchView(generic.ListView):
    template_name = 'book.html'

    def get_queryset(self):
        return models.BookModel.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, books=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context






def about_me(request):
    return HttpResponse('Меня зовет Василиса, учусь на направлении Backend')


def text_and_photo(request):
    return HttpResponse('<img src="https://cs6.pikabu.ru/post_img/2014/05/15/10/1400167833_1703122734.jpg"/>')

def system_time(request):
    current_time = datetime.today()
    return HttpResponse(current_time)
