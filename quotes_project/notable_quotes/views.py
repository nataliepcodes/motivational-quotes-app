from django.shortcuts import render, get_object_or_404
from .models import Quote, Author, Category

def home(request):
    # Retrieve all quotes for the database - Quote.objects.all()
    quotes = Quote.objects.all()

    return render(request, "notable_quotes/home.html", {"quotes": quotes})


def author_details(request, author_id):
    # getting an author object by id
    author = get_object_or_404(Author, id=author_id)

    return render(request, "notable_quotes/author.html", {"author": author})


def display_categories(request, category_name):
    category = get_object_or_404(Category, name=category_name)

    return render(request, "notable_quotes/category.html", {"category": category})