from django.test import TestCase

from django.urls import reverse

from .models import Mineral
from .views import mineral_list, mineral_detail
# Create your tests here.

class MineralTest(TestCase):

    def create_mineral(self, name="fake"):
        return Mineral.objects.create(name=name)

    def test_mineral_creation(self):
        min = self.create_mineral()
        self.assertTrue(isinstance(min, Mineral))
        self.assertEqual(min.pk, 875)
