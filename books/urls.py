from django.urls import path

from books.views import BookListView, BookDetailView

app_name = 'books'
urlpatterns = [
    path('', BookListView.as_view(), name='list'),
    # bookdetailview gets id from route
    path("<int:id>/", BookDetailView.as_view(), name='detail'),
]
