from django.shortcuts import render, redirect, get_object_or_404
from books.models import Book
from .forms import BookForm
from django.db.models import Q
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book


# Create your views here.




def book_list(request):
    books = Book.objects.select_related('genre','author').all()

    return render(
        request,'grud/book_list.html',{'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    return render(request,'grud/book_datail.html',{'book': book})

def book_create(request):

    if request.method == 'POST':
        form = BookForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect('book_list')

    else:
        form = BookForm()

    return render(request,'grud/book_form.html',{'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = BookForm(
            request.POST,
            request.FILES,
            instance=book
        )

        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=pk)

    else:
        form = BookForm(instance=book)
    return render(request,'grud/book_form.html',{'form': form})

def book_delete(request, pk):


    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')

    return render(request,'grud/book_delete.html',{'book': book})







class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer