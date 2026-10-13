from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Recipe


class RecipeModelTests(TestCase):
    def test_str_returns_title(self):
        recipe = Recipe(title='Koshary')
        self.assertEqual(str(recipe), 'Koshary')


class RecipeAccessTests(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(title='Test', image='food_images/x.jpg')

    def test_add_requires_login(self):
        response = self.client.get(reverse('add_recipe'))
        self.assertEqual(response.status_code, 302)

    def test_delete_requires_login(self):
        url = reverse('delete_recipe', args=[self.recipe.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Recipe.objects.filter(id=self.recipe.id).exists())

    def test_delete_rejects_get(self):
        user = get_user_model().objects.create_user('u', password='p')
        self.client.force_login(user)
        url = reverse('delete_recipe', args=[self.recipe.id])
        self.assertEqual(self.client.get(url).status_code, 405)
        self.assertTrue(Recipe.objects.filter(id=self.recipe.id).exists())

    def test_delete_with_post(self):
        user = get_user_model().objects.create_user('u', password='p')
        self.client.force_login(user)
        url = reverse('delete_recipe', args=[self.recipe.id])
        self.client.post(url)
        self.assertFalse(Recipe.objects.filter(id=self.recipe.id).exists())
# Create your tests here.
