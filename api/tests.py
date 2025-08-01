from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book_data = {
            "title": "1984",
            "author": "George Orwell",
            "isbn": "1234567890123",
            "published_date": "1949-06-08"
        }

    def test_create_book(self):
        response = self.client.post("/api/books/", self.book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data)
        self.assertIn("created_at", response.data)

    def test_get_book(self):
        book = Book.objects.create(**self.book_data)
        response = self.client.get(f"/api/books/{book.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book_data["title"])

    def test_update_book(self):
        book = Book.objects.create(**self.book_data)
        update_data = {"title": "Animal Farm"}
        response = self.client.patch(f"/api/books/{book.id}/", update_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book.refresh_from_db()
        self.assertEqual(book.title, "Animal Farm")

    def test_delete_book(self):
        book = Book.objects.create(**self.book_data)
        response = self.client.delete(f"/api/books/{book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=book.id).exists())
        
        """test"""