from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book


# Health Check Endpoint — Always useful for monitoring and testing
# This endpoint can be used to check if the API is up and running
# It returns a simple JSON response indicating the service status.
# It can be extended to include more detailed health checks in the future.
class HealthView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"status": "ok"})  # Simple health check

health_view = HealthView.as_view()


# View for listing all books or creating a new one
class BookView(APIView):
    """ Handles GET for listing all books and POST for creating a new book """

    def get(self, request, *args, **kwargs):
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)

        # Wrap data for future extensibility
        return Response({
            "count": all_books.count(),
            "results": serializer.data
        })

    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Respond with 201 status on successful creation
        return Response(serializer.data, status=status.HTTP_201_CREATED)

book_view = BookView.as_view()


# View for retrieving, updating, or deleting a single book by its ID (pk)
class BookDetailView(APIView):
    """ Handles GET, PUT, PATCH, DELETE for an individual book """

    def get(self, request, pk, *args, **kwargs):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        book = get_object_or_404(Book, pk=pk)

        # Validates full update
        serializer = BookSerializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def patch(self, request, pk, *args, **kwargs):
        book = get_object_or_404(Book, pk=pk)

        # Partial update
        serializer = BookSerializer(book, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk, *args, **kwargs):
        book = get_object_or_404(Book, pk=pk)
        book.delete()

        # HTTP 204 as best practice for empty successful deletion
        return Response(status=status.HTTP_204_NO_CONTENT)

book_detail_view = BookDetailView.as_view()