from tests.testcase import TestCase

class TestApi(TestCase):

    def test_func_name(self):
        request = self.app.get('/geocode/address?house_number=100&street=Gold st&borough_code=1')
        response = request.json
        self.assertFalse(response['error'])
        self.assertIsNotNone(response['result']['First Borough Name'])
        self.assertIsNotNone(response['result']['House Number - Display Format'])
        self.assertIsNotNone(response['result']['First Street Name Normalized'])

    def test_func_code(self):
        request = self.app.get('/geocode/1b?house_number=100&street=Gold st&borough_code=1')
        response = request.json
        self.assertFalse(response['error'])
        self.assertIsNotNone(response['result']['First Borough Name'])
        self.assertIsNotNone(response['result']['House Number - Display Format'])
        self.assertIsNotNone(response['result']['First Street Name Normalized'])

    def test_attr_error(self):
        fake_func = '0'
        request = self.app.get('/geocode/{}'.format(fake_func))
        response = request.json
        self.assertTrue(response['error'])
        self.assertEqual(response['result']["Message"],  "Unknown Geosupport function '{}'.".format(fake_func))

    def test_geo_error(self):
        request = self.app.get('/geocode/address')
        response = request.json
        self.assertTrue(response['error'])
        self.assertEqual(response['result']["Message"],  "NO INPUT DATA RECEIVED")
