from itertools import tee
from django.test import TestCase
from django.urls import reverse

from .models import Ressource

class IndexViewTests(TestCase):

    def test_no_ressources(self):
        """
        If no ressources exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('ressource_management:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No ressource_management are available.")
        self.assertQuerysetEqual(response.context['ressource_list'], [])

    def test_past_ressource(self):
        """
        The ressources index page may display one ressource.
        """
        ressource = Ressource.objects.create(type="amphithéâtre", label="A1", localization="Batiment A", people_capacity=200)
        response = self.client.get(reverse('ressource_management:index'))
        self.assertQuerysetEqual(response.context['ressource_list'],[ressource])

    def test_two_past_ressources(self):
        """
        The ressources index page may display multiple ressources.
        """
        ressource1 = Ressource.objects.create(type="amphithéâtre", label="A1", localization="Batiment A, rez de chaussé", people_capacity=200)
        ressource2 = Ressource.objects.create(type="salle de réunion", label="B7", localization="Batiment B, 1er étage", people_capacity=30)
        response = self.client.get(reverse('ressource_management:index'))
        self.assertQuerysetEqual(response.context['ressource_list'],[ressource1, ressource2],ordered=False)


class DetailViewTest(TestCase):

    def test_no_ressource(self):
        """
        If no ressources exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('ressource_management:detail',args=[1]))
        self.assertEqual(response.status_code, 404)

    def test_past_ressource(self):
        """
        The ressource detail page may display ressource.
        """
        ressource = Ressource.objects.create(type="amphithéâtre", label="A1", localization="Batiment A", people_capacity=200)
        response = self.client.get(reverse('ressource_management:detail',args=[1]))
        self.assertEqual(response.context['ressource'],ressource)


class UpdateViewTest(TestCase):

    def test_no_ressource(self):
        """
        If no ressources exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('ressource_management:update',args=[1]))
        self.assertEqual(response.status_code, 404)

    def test_past_ressource(self):
        """
        The ressource update page may display ressource.
        """
        ressource = Ressource.objects.create(type="amphithéâtre", label="A1", localization="Batiment A", people_capacity=200)
        response = self.client.get(reverse('ressource_management:update',args=[1]))
        self.assertEqual(response.context['ressource'],ressource)


class DeleteViewTest(TestCase):

    def test_no_ressource(self):
        """
        If no ressources exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('ressource_management:delete',args=[1]))
        self.assertEqual(response.status_code, 404)

    def test_past_ressource(self):
        """
        The ressource delete page may display ressource.
        """
        ressource = Ressource.objects.create(type="amphithéâtre", label="A1", localization="Batiment A", people_capacity=200)
        response = self.client.get(reverse('ressource_management:delete',args=[1]))
        self.assertEqual(response.context['ressource'],ressource)


class CreateViewTest(TestCase):
    
    def test_page_exist(self):
        """
        The page exist
        """
        response = self.client.get(reverse('ressource_management:add'))
        self.assertEqual(response.status_code, 200)