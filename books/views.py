from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from books.models import Book

# class BookListView(View):
#     def get(self, request):
#         books = Book.objects.all().order_by('id')
#         page_size = request.GET.get('page_size', 2)
#         paginator = Paginator(books, 2)
#         page_num = request.GET.get('page', 1)
#         page_obj = paginator.get_page(page_num)
#         return render(request, 'books/books_list.html', {'page_obj': page_obj})


#HEre generic code alternative to the above one
class BookListView(ListView):
    template_name = 'books/books_list.html'
    queryset = Book.objects.all()
    context_object_name = 'books'
    paginate_by = 2


# class BookDetailView(View):
#     def get(self, request, id):
#         book = Book.objects.get(id=id)
#         return render(request, 'books/book_detail.html', {'book': book})

class BookDetailView(DetailView):
    template_name = 'books/book_detail.html'
    pk_url_kwarg = 'id'
    model = Book

