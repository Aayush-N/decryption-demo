from django.urls import path

from main.views import MessageDecrypter

urlpatterns = [
    path('decryptMessage', MessageDecrypter.as_view(), name='message-decrypter'),
]