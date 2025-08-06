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
        
    def test_bulk_create_books(self):
        bulk_books_data = [
            {
                "title": "One Hundred Years of Solitude",
                "author": "Gabriel García Márquez",
                "isbn": "9780060883287",
                "published_date": "1967-06-05"
            },
            {
                "title": "The Hobbit",
                "author": "J. R. R. Tolkien",
                "isbn": "9780007458424",
                "published_date": "1937-09-21"
            }
        ]
        response = self.client.post("/api/books/bulk-create/", bulk_books_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["title"], "One Hundred Years of Solitude")
        self.assertEqual(response.data[1]["title"], "The Hobbit")
        self.assertEqual(Book.objects.count(), 2)
        
        """test"""