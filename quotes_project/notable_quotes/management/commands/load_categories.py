import json
from django.core.management.base import BaseCommand
from django.conf import settings
from notable_quotes.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories_file = settings.BASE_DIR / "notable_quotes" / "data" / "categories.json"

        with open(categories_file, "r", encoding="utf-8") as file:
            categories = json.load(file)

        for item in categories:
            category, created = Category.objects.get_or_create(
                name=item["category"]
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Added: {category.name}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Skipped duplicate: {category.name}"
                    )
                )