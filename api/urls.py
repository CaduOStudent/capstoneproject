from django.urls import path
from .views import health_view, book_view, book_detail_view, bulk_create_books_view

urlpatterns = [
    path('health/', health_view, name='health'),
    path('books/', book_view, name='book-list'),
    path('books/<int:pk>/', book_detail_view, name='book-detail'),
    # Add any additional paths here
    path('books/bulk-create/', bulk_create_books_view, name='bulk-create-books'),
]