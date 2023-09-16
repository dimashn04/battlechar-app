from django.forms import ModelForm
from main.models import Operator

class OperatorForm(ModelForm):
  class Meta:
    model = Operator
    fields = ["name", "unit", "primary_weapon", 
              "secondary_weapon", "primary_weapon_ammo_amount", "secondary_weapon_ammo_amount", 
              "armor", "speed", "description", "price"]