from django.core.mail import send_mail

from goodreads.celery import app


@app.task
def send_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        'kitob3199@mail.ru',
        recipient_list
    )