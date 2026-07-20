import json
from django.core.management.base import BaseCommand
from django.conf import settings
from notable_quotes.models import Quote, Category

# Command to help load quotes onto the database
# To run it: 
# 1. Check if migrations are up to date: $ python manage.py migrate
# 2. Add data: $ python manage.py load_quotes
# To check database after adding data:
# $ python manage.py shell
# from notable_quotes.models import Quote
# Quote.objects.count()
# Quote.objects.all()
# for quote in Quote.objects.all():
    #print(quote.quote, "-", quote.author)

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        quotes_file = settings.BASE_DIR / "notable_quotes" / "data" / "quotes.json"

        with open(quotes_file, "r", encoding="utf-8") as file:
            quotes = json.load(file)

        # Load each quote from JSON
        # Check if the quote exists with get_or_create()
        # get_or_create() returns:
        # - quote: the Quote object
        # - created: True if a new record was created, False if it already existed
        for item in quotes:
            
            quote, created = Quote.objects.get_or_create(
                quote=item["quote"],
                author=item["author"],
            )

            #  "categories": ["Resilience", "Perseverance", "Courage"]    
            for category_name in item["categories"]:
                category = Category.objects.get(name=category_name)
                quote.category.add(category) # added to the joining table >> notable_quotes_quote_category

            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Added: {quote.quote}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Skipped duplicate: {quote.quote}"
                    )
                )