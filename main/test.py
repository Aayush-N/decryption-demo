from rest_framework.test import APIRequestFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class DecryptionTest(APITestCase):

    def test_when_message_decrypted_success(self):
        url = reverse('message-decrypter')
        data = {"passphrase": "topsecret", "message": "-----BEGIN PGP PUBLIC KEY BLOCK-----\n\njA0ECQMCVady3RUyJw3X0kcBF+zdkfZOMhISoYBRwR3uk3vNv+TEg+rJnp4/yYISpEoI2S82cDiCNBIVAYWB8WKPtH2R2YSussKhpSJ4mFgqyOA01uwroA===KvJQ-----END PGP PUBLIC KEY BLOCK-----"}
        response = self.client.post(url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)