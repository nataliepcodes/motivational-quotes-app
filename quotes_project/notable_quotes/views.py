from django.shortcuts import render
from .models import Quote

def home(request):
    # Retrieve all quotes for the database - Quote.objects.all()
    quotes = Quote.objects.all()

    return render(request, "notable_quotes/home.html", {"quotes": quotes})
