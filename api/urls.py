
from django.urls import path

from api.views import BookReviewDetailApiView

urlpatterns = [
    path('reviews/<int:id>/', BookReviewDetailApiView.as_view(), name='review-detail'),
]