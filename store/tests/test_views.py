from unittest import skip

from django.test import TestCase
from django.contrib.auth.models import User

from store.models import Category, Product

from django.test import Client 

# @skip('demonstrationg skipping')
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass 

class TestViewResponses(testCase):
    def setUp(self):
        self.c = Client()

    def test_url_allowed_hosts(self):
        """
        Test alloweed Hosts
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    # def test_homepage_url(self):
    #     """
    #         Test homepage response status
    #     """