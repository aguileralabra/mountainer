from django.test import TestCase
from django.urls import reverse
from .models import Turist
import json

class TuristTestCase(TestCase):

    def setUp(self):
        self.turist = Turist()
        self.response = turist.get(reverse('list'))
        selft.detail_url = reverse('detail', args=['project1'])
    
    def test_project_list_GET(self):
        response = self.turist.get(self.list_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'mountain/turists')