import json
from django.core.management.base import BaseCommand
from django.conf import settings
from notable_quotes.models import Author

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        authors_file = settings.BASE_DIR / "notable_quotes" / "data" / "authors.json"

        with open(authors_file, "r", encoding="utf-8") as file:
            authors = json.load(file)

        for item in authors:
            
            author, created = Author.objects.get_or_create(
                name=item["name"],
                born=item["born"],
                country=item["country"],
                famous_for=item["famous_for"],
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Added: {author.name}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Skipped duplicate: {author.name}"
                    )
                )