from django.test import TestCase
from django.test import Client
from task import result


class IndexTestCase(TestCase):

    def test_get_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)


class MatchingCase(TestCase):
    filter_obj = None

    def setUp(self):
        self.matching_obj = result

    def test_matching_keys(self):
        key = "SUCCINYL CHOLINE CHLORIDE 500MG"
        expected_result = [{'value': 'DEMECLOCYCLINE HYDROCHLORIDE FILM COATED TABLET 300MG', 'percent': 52.38},
                           {'value': 'DONEPEZIL HYDROCHLORIDE 10MG TABLET', 'percent': 51.52},
                           {'value': 'DONEPEZIL HYDROCHLORIDE 5MG TABLET', 'percent': 52.31},
                           {'value': 'FLUCONAZOLE CAP 200MG', 'percent': 50.00},
                           {'value': 'URSODEOXYCHOLIC ACID TABLET 150MG', 'percent': 53.12},
                           {'value': 'ZINC CHLORIDE 1MG/ML INJ', 'percent': 54.55}]
        result =self.matching_obj.get_matching(key)
        self.assertEqual(result, expected_result)
