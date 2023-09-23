from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Operator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    primary_weapon = models.CharField(max_length=255)
    secondary_weapon = models.CharField(max_length=255)
    primary_weapon_ammo_amount = models.IntegerField()
    secondary_weapon_ammo_amount = models.IntegerField()
    armor = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    speed = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)]) 
    description = models.TextField()
    price = models.IntegerField()