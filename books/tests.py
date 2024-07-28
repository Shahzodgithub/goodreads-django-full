from django.test import TestCase
from django.urls import reverse

from books.models import Book


# Create your tests here.

class BooksTestCase(TestCase):
    def test_no_books(self):
        response = self.client.get(reverse('books:list'))
        self.assertContains(response, 'No books found.')

    def test_books_list(self):
        Book.objects.create(title='Test Book',  description='Test Description', isbn='23432432')
        Book.objects.create(title='Test Book2', description='Test Description2', isbn='27432432')
        Book.objects.create(title='Test Book3', description='Test Description3', isbn='25432432')

        response = self.client.get(reverse('books:list'))

        for book in Book.objects.all():
            self.assertContains(response, book.title)
