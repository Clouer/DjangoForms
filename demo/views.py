from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.views.decorators.http import require_POST

from demo import forms
from demo.models import Book


def search(request):
    return render(request, 'demo/search.html', context={'form': forms.SearchForm()})


def get_search(request):
    return HttpResponse(str(request.GET['mail']))


@require_POST
def post_search(request):
    return HttpResponse(str(request.POST['mail']))


class SubscribeView(View):
    def get(self, request):
        return render(request, 'demo/subscribe.html', context={'form': forms.SubscribeForm()})

    def post(self, request):
        form = forms.SubscribeForm(request.POST)
        if form.is_valid():
            print('УРА')
            return redirect(request.path)
        return render(request, 'demo/subscribe.html', context={'form': form})


class IceCreamView(View):
    def get(self, request):
        return render(request, 'demo/ice-cream.html', context={'form': forms.IceCreamForm()})

    def post(self, request):
        form = forms.IceCreamForm(request.POST)
        if form.is_valid():
            print('УРА')
            return redirect(reverse('search'))
        return render(request, 'demo/ice-cream.html', context={'form': form})


def look_book(request, book_id):
    return render(request, 'demo/look-book.html', context={'book': get_object_or_404(Book, id=book_id)})


class BookView(View):
    def get(self, request):
        return render(request, 'demo/book.html', context={'form': forms.BookForm()})

    def post(self, request):
        form = forms.BookForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            book = Book.objects.create(
                surname=cleaned['surname'],
                name=cleaned['name'],
                luggage_weight=cleaned['luggage_weight'],
                pass_id=cleaned['pass_id']
            )
            return redirect(reverse('look_book', kwargs={'book_id': book.id}))
        return render(request, 'demo/book.html', context={'form': form})
