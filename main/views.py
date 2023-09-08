from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Fuze',
        'unit': 'Spetsnaz',
        'primary_weapon': '6P41',
        'secondary_weapon': 'Makarov PMM',
        'ammo_amount': 200,
        'armor': 3,
        'speed': 1,
        'operator_description': "Fuze is best played as an aggressive flanker and area denial Operator. His strengths allow him to dispatch defensive capabilities and harass enemies anchored in defensive positions. Fuze's APM-6 cluster charge propels a group of explosive cluster grenades through any soft breach surface.",
        'price': 12500,
    }

    return render(request, "main.html", context)