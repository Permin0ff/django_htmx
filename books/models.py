from django.db import models


class Book(models.Model):
    title = models.CharField(
        max_length=200,
        blank=True,
    )
    author = models.CharField(
        max_length=200,
        blank=True,
    )
    price = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    read = models.BooleanField(
        default=False,
        blank=True,
    )

    def __str__(self):
        return self.title
