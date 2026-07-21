from django.shortcuts import render, get_object_or_404
from .models import Quote, Author, Category
from datetime import date

def home(request):
    # Retrieve all quotes for the database - Quote.objects.all()
    quotes = Quote.objects.all()

    day = date.today().timetuple().tm_yday

    daily_quote = quotes[date % quotes.count()] # go through all current quotes then start again

    today = day.today()

    return render(request, "notable_quotes/home.html", 
                  {"daily_quote": daily_quote,
                    "today": today,
                   }
    )


def all_quotes(request):
    # Retrieve all quotes for the database - Quote.objects.all()
    quotes = Quote.objects.all()

    return render(request, "notable_quotes/all_quotes.html", {"quotes": quotes})


def author_details(request, author_id):
    # getting an author object by id
    author = get_object_or_404(Author, id=author_id)

    return render(request, "notable_quotes/author.html", {"author": author})


def display_categories(request, category_name):
    # name__iexact ignores the case (lower/Upper/UPPER) ! could Improve to slug=slug !
    # without a slug: category/Personal%20Growth/
    # with a slug could be: category/personal-growth
    category = get_object_or_404(Category, name__iexact=category_name) 

    return render(request, "notable_quotes/category.html", {"category": category})