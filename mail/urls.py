from django.urls import path, include
from mail.views import send_email, send_emails


app_name = 'mail'

urlpatterns = [
    path('', send_email, name='send_email'),
    path('', send_emails, name='send_emails'),
]
