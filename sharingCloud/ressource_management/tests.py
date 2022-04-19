from itertools import tee
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Ressource

class General():

    def connexion_user(self):
        self.client = Client()
        user = User.objects.create(username='testuser',password="password")
        self.client.force_login(user, backend=None)

    def connexion_superuser(self):
        self.client = Client()
        user = User.objects.create_superuser(username='testuser',password="password")
        self.client.force_login(user, backend=None)


class IndexViewTests(General,TestCase):

    def test_not_connected(self):
        """
        If a user is not connected, a user is rediriged
        """
        ressource = Ressource.objects.create(type="amphithéâtre", label="A1", localization="Batiment A", people_capacity=200)
        response = self.client.get(reverse('ressource_management:index'))
        self.assertEqual(response.status_code, 302)
    
    def test_connected_user(self):
        """
        If a user is not superuser , he has access to the page
        """
        self.connexion_user()
        ressource = Ressource.objects.create(type="amphithéâtre", label="A1", localization="Batiment A", people_capacity=200)
        response = self.client.get(reverse('ressource_management:index'))
        self.assertEqual(response.status_code, 200)

    def test_connected_superuser(self):
        """
        If a user is superuser, he has access to the page
        """
        self.connexion_user()
        ressource = Ressource.objects.create(type="amphithéâtre", label="A1", localization="Batiment A", people_capacity=200)
        response = self.client.get(reverse('ressource_management:index'))
        self.assertEqual(response.status_code, 200)

    def test_no_ressources(self):
        """
        If no ressources exist, an appropriate message is displayed.
        """
        self.connexion_user()
        response = self.client.get(reverse('ressource_management:index'))
        self.assertQuerysetEqual(response.context['ressource_list'], [])

    def test_past_ressource(self):
        """
        The ressources index page may display one ressource.
        """
        self.connexion_user()
        ressource = Ressource.objects.create(type="amphithéâtre", label="A1", localization="Batiment A", people_capacity=200)
        response = self.client.get(reverse('ressource_management:index'))
        self.assertQuerysetEqual(response.context['ressource_list'],[ressource])

    def test_two_past_ressources(self):
        """
        The ressources index page may display multiple ressources.
        """
        self.connexion_user()
        ressource1 = Ressource.objects.create(type="amphithéâtre", label="A1", localization="Batiment A, rez de chaussé", people_capacity=200)
        ressource2 = Ressource.objects.create(type="salle de réunion", label="B7", localization="Batiment B, 1er étage", people_capacity=30)
        response = self.client.get(reverse('ressource_management:index'))
        self.assertQuerysetEqual(response.context['ressource_list'],[ressource1, ressource2],ordered=False)


class DetailViewTest(General,TestCase):

    def test_not_connected(self):
        """
        If a user is not connected, a user is rediriged
        """
        ressource = Ressource.objects.create(type="amphithéâtre", label="A1", localization="Batiment A", people_capacity=200)
        response = self.client.get(reverse('ressource_management:detail',args=[1]))
        self.assertEqual(response.status_code, 302)
    
    def test_connected_user(self):
        """
        If a user is not superuser , he has access to the page
        """
        self.connexion_user()
        ressource = Ressource.objects.create(type="amphithéâtre", label="A1", localization="Batiment A", people_capacity=200)
        response = self.client.get(reverse('ressource_management:detail',args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_connected_superuser(self):
        """
        If a user is superuser, he has access to the page
        """
        self.connexion_superuser()
        ressource = Ressource.objects.create(type="amphithéâtre", label="A1", localization="Batiment A", people_capacity=200)
        response = self.client.get(reverse('ressource_management:detail',args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_no_ressource(self):
        """
        If no ressources exist, an appropriate message is displayed.
        """
        self.connexion_user()
        response = self.client.get(reverse('ressource_management:detail',args=[1]))
        self.assertEqual(response.status_code, 404)

    def test_past_ressource(self):
        """
        The ressource detail page may display ressource.
        """
        self.connexion_user()
        ressource = Ressource.objects.create(type="amphithéâtre", label="A1", localization="Batiment A", people_capacity=200)
        response = self.client.get(reverse('ressource_management:detail',args=[1]))
        self.assertEqual(response.context['ressource'],ressource)


class UpdateViewTest(General,TestCase):

    def test_not_connected(self):
        """
        If a user is not connected, a user is rediriged
        """
        ressource = Ressource.objects.create(type="amphithéâtre", label="A1", localization="Batiment A", people_capacity=200)
        response = self.client.get(reverse('ressource_management:update',args=[1]))
        self.assertEqual(response.status_code, 302)
    
    def test_connected_user(self):
        """
        If a user is not superuser , a user is blocked
        """
        self.connexion_user()
        ressource = Ressource.objects.create(type="amphithéâtre", label="A1", localization="Batiment A", people_capacity=200)
        response = self.client.get(reverse('ressource_management:update',args=[1]))
        self.assertEqual(response.status_code, 403)

    def test_connected_superuser(self):
        """
        If a user is superuser, he has access to the page
        """
        self.connexion_superuser()
        ressource = Ressource.objects.create(type="amphithéâtre", label="A1", localization="Batiment A", people_capacity=200)
        response = self.client.get(reverse('ressource_management:update',args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_no_ressource(self):
        """
        If no ressources exist, an appropriate message is displayed.
        """
        self.connexion_superuser()
        response = self.client.get(reverse('ressource_management:update',args=[1]))
        self.assertEqual(response.status_code, 404)

    def test_past_ressource(self):
        """
        The ressource update page may display ressource.
        """
        self.connexion_superuser()
        ressource = Ressource.objects.create(type="amphithéâtre", label="A1", localization="Batiment A", people_capacity=200)
        response = self.client.get(reverse('ressource_management:update',args=[1]))
        self.assertEqual(response.context['ressource'],ressource)


class DeleteViewTest(General,TestCase):

    def test_not_connected(self):
        """
        If a user is not connected, a user is blocked
        """
        ressource = Ressource.objects.create(type="amphithéâtre", label="A1", localization="Batiment A", people_capacity=200)
        response = self.client.get(reverse('ressource_management:delete',args=[1]))
        self.assertEqual(response.status_code, 403)
    
    def test_connected_user(self):
        """
        If a user is not superuser , a user is blocked
        """
        self.connexion_user()
        ressource = Ressource.objects.create(type="amphithéâtre", label="A1", localization="Batiment A", people_capacity=200)
        response = self.client.get(reverse('ressource_management:delete',args=[1]))
        self.assertEqual(response.status_code, 403)

    def test_connected_superuser(self):
        """
        If a user is superuser, he has redirigate and a ressource is deleted
        """
        self.connexion_superuser()
        ressource = Ressource.objects.create(type="amphithéâtre", label="A1", localization="Batiment A", people_capacity=200)
        response = self.client.get(reverse('ressource_management:delete',args=[1]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(Ressource.objects.filter(id=1)),0)

    def test_no_ressource(self):
        """
        If no ressource exist, a user is rediriged 302.
        """
        self.connexion_superuser()
        response = self.client.get(reverse('ressource_management:delete',args=[1]))
        self.assertEqual(response.status_code, 302)


class CreateViewTest(General,TestCase):

    def test_not_connected(self):
        """
        If a user is not connected, a user is rediriged
        """
        response = self.client.get(reverse('ressource_management:add'))
        self.assertEqual(response.status_code, 302)
    
    def test_connected_user(self):
        """
        If a user is not superuser , a user is blocked
        """
        self.connexion_user()
        response = self.client.get(reverse('ressource_management:add'))
        self.assertEqual(response.status_code, 403)

    def test_connected_superuser(self):
        """
        If a user is superuser, he has access to the page
        """
        self.connexion_superuser()
        response = self.client.get(reverse('ressource_management:add'))
        self.assertEqual(response.status_code, 200)