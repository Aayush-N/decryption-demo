from django.urls import path

from main.views import MessageDecrypter, HomeView

urlpatterns = [
	path('', HomeView.as_view(), name='home-page'),
    path('decryptMessage', MessageDecrypter.as_view(), name='message-decrypter'),
]