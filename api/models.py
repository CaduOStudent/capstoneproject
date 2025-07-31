from django.db import models

# The models are the "class" in python
# They are used to create the database tables
# and define the structure of the data
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation

    def __str__(self):
        return f"{self.title} by {self.author}"


