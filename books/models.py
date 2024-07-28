from users.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    isbn = models.CharField(max_length=17, null=True)
    cover_picture = models.ImageField(default='default.jpg')

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.first_name


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default='')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default='')

    def __str__(self):
        return f"{self.book} by  {self.author}"


class BookReview(models.Model):
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField(null=True)
    stars_given = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True
    )

    def __str__(self):
        return f"{self.book} review by  {self.user}"
