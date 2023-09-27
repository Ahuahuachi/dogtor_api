from django.db import models


class Owner(models.Model):
    """Owner object"""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()


class Species(models.Model):
    """Pet species"""

    name = models.CharField(max_length=20)


class Pet(models.Model):
    """Pet object"""

    name = models.CharField(max_length=255)
    owner = models.ForeignKey(Owner, related_name="pets", on_delete=models.CASCADE)
    age = models.IntegerField()
    species = models.ForeignKey(to=Species, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)


class Record(models.Model):
    """Medical record object"""

    class Category(models.IntegerChoices):
        """Medical record category"""

        OTHER = 0
        BLOOD_PRESSURE = 1
        BLOOD_SUGAR = 2
        BLOOD_GLUCOSE = 3
        BLOOD_OXYGEN = 4
        VACCINATION = 5

    category = models.IntegerField(choices=Category.choices)
    procedure = models.CharField(max_length=255)
    pet = models.ForeignKey(Pet, related_name="records", on_delete=models.CASCADE)
    date = models.DateField()
