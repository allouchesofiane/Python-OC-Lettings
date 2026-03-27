"""Module contenant les modèles de l'application lettings."""
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """Modèle représentant une adresse postale."""

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999)]
        )
    country_iso_code = models.CharField(
        max_length=3,
        validators=[MinLengthValidator(3)]
        )

    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self):
        """Retourne une représentation lisible de l'adresse."""
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """Modèle représentant une location."""

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Retourne le titre de la location."""
        return self.title
