from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MessageSerializer
from django.views.generic.base import TemplateView

import gnupg
# Create your views here.


class MessageDecrypter(APIView):
	"""
	Accepts only POST, converts the encrypted text into a decrypted text
	"""
	def post(self, request, format=None):
		serializer = MessageSerializer(data=request.data)
		if serializer.is_valid():
			gpg = gnupg.GPG()
			decrypted_data = gpg.decrypt(serializer.data['message'], passphrase=serializer.data['passphrase'], always_trust=True)
			if decrypted_data.ok:
				messageDict = {}
				messageDict['DecryptedMessage'] = decrypted_data.data.decode("utf-8")
				return Response(messageDict, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HomeView(TemplateView):
    template_name = "home.html"