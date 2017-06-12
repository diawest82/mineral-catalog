from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Mineral
# Create your tests here.


class MineralModelTestcase(TestCase):
    def test_mineral_model(self):
        minerals = Mineral.objects.create(
            name="rock name",
            image_filename="file name",
            image_caption='caption',
            category='category',
            formula='formula test',
            strunz_classification='classification test',
            crystal_system='crystal test',
            unit_cell='cell',
            color='color test',
            crystal_symmetry='symetry test',
            cleavage='cleavage',
            mohs_scale_hardness='hardness scale',
            luster='luster',
            streak='streak',
            diaphaneity='diaphaneity',
            optical_properties='properties',
            refractive_index='index test',
            crystal_habit='habit test',
            specific_gravity='gravity test',
        )
        self.assertEqual(minerals.name, 'rock name')


class MineralViewTestCase(TestCase):
    def setUp(self):
        self.minerals = Mineral.objects.create(
            name="rock name",
            image_filename="file name",
            image_caption='caption',
            category='category',
            formula='formula test',
            strunz_classification='classification test',
            crystal_system='crystal test',
            unit_cell='cell',
            color='color test',
            crystal_symmetry='symetry test',
            cleavage='cleavage',
            mohs_scale_hardness='hardness scale',
            luster='luster',
            streak='streak',
            diaphaneity='diaphaneity',
            optical_properties='properties',
            refractive_index='index test',
            crystal_habit='habit test',
            specific_gravity='gravity test',
        )

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.minerals, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        self.assertContains(resp, self.minerals.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'pk': self.minerals.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.minerals, resp.context['mineral'])
