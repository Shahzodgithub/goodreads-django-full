from django.shortcuts import render
from django.views import View

from books.models import BookReview
from django.http import JsonResponse

# Create your views here.
class BookReviewDetailApiView(View):
    def get(self, request, id):
        book_review = BookReview.objects.get(pk=id)

        json_response = {
            'id': book_review.id,
            'stars_given': book_review.stars_given,
            'comments': book_review.comments,
        }


        return JsonResponse(json_response)
