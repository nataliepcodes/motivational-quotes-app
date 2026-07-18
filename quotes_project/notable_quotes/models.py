from django.db import models

class Quote(models.Model):
    quote = models.TextField(unique=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return f'"{self.quote}" - {self.author}'
    

class Author(models.Model):
    name = models.CharField(max_length=100)
    born = models.IntegerField()
    country = models.CharField(max_length=100)
    famous_for = models.TextField()
    quote = models.TextField(unique=True)

    def __str__(self):
        return self.name
