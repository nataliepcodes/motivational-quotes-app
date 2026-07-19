from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    born = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=100)
    famous_for = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name


class Quote(models.Model):
    quote = models.TextField(unique=True)

    # Related name helps to retrieve all data (e.g. author.quotes.all() without using quote_set.all()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="quotes"
    )

    category = models.ManyToManyField(
        Category,
        related_name="quotes"
    )

    def __str__(self):
        return f'"{self.quote}" - {self.author}'
