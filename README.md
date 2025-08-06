## capstoneProject

This project have the objective of creating a bookcatalog API using python









## List of commands to test CRUD:

## Add new book:

curl -H "Content-Type: application/json" -X POST localhost:8000/api/books/ -d '{
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "isbn": "9780061120084",
            "published_date": "1960-07-11"
        }'

curl -H "Content-Type: application/json" -X POST localhost:8000/api/books/ -d '{
            "title": "Pride and Prejudice",
            "author": "Jane Austen",
            "isbn": "9780141439518",
            "published_date": "1813-01-28"
        }'

curl -H "Content-Type: application/json" -X POST localhost:8000/api/books/ -d '{
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "isbn": "9780743273565",
            "published_date": "1925-04-10"
        }'

curl -H "Content-Type: application/json" -X POST localhost:8000/api/books/ -d '{
            "title": "Moby-Dick",
            "author": "Herman Melville",
            "isbn": "9780142437247",
            "published_date": "1851-10-18"
        }'


## Bulk Add Many Books:

curl -H "Content-Type: application/json" -X POST localhost:8000/api/books/bulk-create/ -d '[
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
        },
{
            "title": "Crime and Punishment",
            "author": "Fyodor Dostoevsky",
            "isbn": "9780143058144",
            "published_date": "1866-01-01"
        },
{
            "title": "The Catcher in the Rye",
            "author": "J. D. Salinger",
            "isbn": "9780316769488",
            "published_date": "1951-07-16"
        },
{
            "title": "1984",
            "author": "George Orwell",
            "isbn": "9780451524935",
            "published_date": "1949-06-08"
        },
{
            "title": "War and Peace",
            "author": "Leo Tolstoy",
            "isbn": "9780199232765",
            "published_date": "1869-01-01"
        }


]'


## Delete Book:

curl -X DELETE localhost:8000/api/books/1/

curl -H "Content-Type: application/json" -X DELETE localhost:8000/api/books/2/

## Get Specific Book:

curl -s localhost:8000/api/books/{id}/ | jq

## Get all Books:

curl -s localhost:8000/api/books/ | jq


## Edit:

curl -H "Content-Type: application/json" -X PATCH localhost:8000/api/books/7/ -d '{"title":"Dracula from Barm"}'
