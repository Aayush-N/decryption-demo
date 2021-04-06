from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class DecryptionSuccessTest(APITestCase):
	# This test case makes sure decryption is happening
    def test_when_message_decrypted_success(self):
        url = reverse('message-decrypter')
        data = {"passphrase": "topsecret", "message": "-----BEGIN PGP PUBLIC KEY BLOCK-----\n\njA0ECQMCVady3RUyJw3X0kcBF+zdkfZOMhISoYBRwR3uk3vNv+TEg+rJnp4/yYISpEoI2S82cDiCNBIVAYWB8WKPtH2R2YSussKhpSJ4mFgqyOA01uwroA===KvJQ-----END PGP PUBLIC KEY BLOCK-----"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class IncorrectMessageFormatTest(APITestCase):
	# This test case makes sure the format of the message is correct
    def test_when_message_decrypted_fail(self):
        url = reverse('message-decrypter')
        data = {"passphrase": "topsecret", "message": "jA0ECQMCVady3RUyJw3X0kcBF+zdkfZOMhISoYBRwR3uk3vNv+TEg+rJnp4/yYISpEoI2S82cDiCNBIVAYWB8WKPtH2R2YSussKhpSJ4mFgqyOA01uwroA===KvJQ"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class CorrectDecryptionTest(APITestCase):
	# This test case makes sure the correct decryption is happening
    def test_when_message_decrypted_is_correct(self):
        url = reverse('message-decrypter')
        data = {"passphrase": "topsecret", "message": "-----BEGIN PGP PUBLIC KEY BLOCK-----\n\njA0ECQMCVady3RUyJw3X0kcBF+zdkfZOMhISoYBRwR3uk3vNv+TEg+rJnp4/yYISpEoI2S82cDiCNBIVAYWB8WKPtH2R2YSussKhpSJ4mFgqyOA01uwroA===KvJQ-----END PGP PUBLIC KEY BLOCK-----"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.data, {'DecryptedMessage': 'Nice work!\n'})