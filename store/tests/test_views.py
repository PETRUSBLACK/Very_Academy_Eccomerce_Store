from unittest import skip

from django.test import TestCase

from django.contrib.auth.models import User
from store.models import Category, Product
from django.urls import reverse 
from django.test import Client 

# @skip('demonstrationg skipping')
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass 

class TestViewResponses(testCase):
    def setUp(self):
        self.c = Client()
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                                slug='django-beginners', price='20.00', image='django')

    def test_url_allowed_hosts(self):
        """
        Test alloweed Hosts
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        response = self.c.get(reverse('store:product_detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)

    # def test_homepage_url(self):
    #     """
    #         Test homepage response status
    #     """