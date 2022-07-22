from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class Entry(models.Model):
    title = models.CharField(max_length=255, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title
