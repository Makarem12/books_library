from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from .models import book
from django.contrib.auth import get_user_model

# Home page tests using SimpleTestCase since it does not require database access
class HomeTest(SimpleTestCase):
    def test_home_page_status(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_home_page(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'home.html')


# Books list and details tests using TestCase since they require database access
class BooksListTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='password'
        )

        # Create test data
        book.objects.create(
            author=self.user,
            title="Book 1",
            description="Description 1",
            rating="5",
            publish_date="2023-01-01"
        )
        book.objects.create(
            author=self.user,
            title="Book 2",
            description="Description 2",
            rating="4",
            publish_date="2023-02-01"
        )

    def test_books_list_page_status(self):
        url = reverse('books')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_books_list_page(self):
        url = reverse('books')
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'books_list.html')
        
