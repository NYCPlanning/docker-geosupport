from tests.testcase import TestCase

class TestSuggestions(TestCase):


    def test_address_has_multiple_results(self):
        request = self.app.get('/suggest?address=100 Gold')
        response = request.json
        self.assertTrue(len(response['result']) > 1)
        self.assertFalse(response['error'])

    def test_address_has_values(self):
        request = self.app.get('/suggest?address=100 Gold')
        response = request.json
        self.assertIsNotNone(response['result'][0]['First Borough Name'])
        self.assertIsNotNone(response['result'][0]['House Number - Display Format'])
        self.assertIsNotNone(response['result'][0]['First Street Name Normalized'])


    def test_address_with_borough(self):
        request = self.app.get('/suggest?address=100 Gold&borough_code=1')
        response = request.json
        self.assertTrue(len(response['result']) > 0)
        self.assertFalse(response['error'])
        self.assertIsNotNone(response['result'][0]['First Borough Name'])
        self.assertIsNotNone(response['result'][0]['House Number - Display Format'])
        self.assertIsNotNone(response['result'][0]['First Street Name Normalized'])
