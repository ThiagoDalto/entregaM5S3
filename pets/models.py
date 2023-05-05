from django.db import models


class PetSex(models.TextChoices):
    MALE = ("Male",)
    FEMALE = ("Female",)
    NOT_INFORMED = "Not informed"


class Pet(models.Model):
    name = models.CharField(
        max_length=50,
    )
    age = models.IntegerField()
    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
    sex = models.CharField(
        max_length=20,
        choices=PetSex.choices,
        default=PetSex.NOT_INFORMED,
    )
    group = models.ForeignKey(
        "groups.Group",
        on_delete=models.CASCADE,
        related_name="groups",
    )
    traits = models.ManyToManyField(
        "traits.Trait",
        related_name="traits",
    )
