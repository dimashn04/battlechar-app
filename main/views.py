import json
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.http import HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import OperatorForm
from django.urls import reverse
from main.models import Operator
from django.http import HttpResponse
from django.core import serializers

# Special thanks to Faris Zhafir Faza for teaching me on how to do this.
def add_primary_ammo_amount(request, operator_id):
    operator = Operator.objects.get(id=operator_id)
    operator.primary_weapon_ammo_amount += 1
    operator.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def dec_primary_ammo_amount(request, operator_id):
    operator = Operator.objects.get(id=operator_id)
    operator.primary_weapon_ammo_amount -= 1
    operator.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def add_secondary_ammo_amount(request, operator_id):
    operator = Operator.objects.get(id=operator_id)
    operator.secondary_weapon_ammo_amount += 1
    operator.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def remove_operator(request, operator_id):
    operator = Operator.objects.get(id=operator_id)
    operator.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def edit_operator(request, id):
    # Get product berdasarkan ID
    product = Operator.objects.get(pk=id)

    # Set product sebagai instance dari form
    form = OperatorForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def dec_secondary_ammo_amount(request, operator_id):
    if request.method == 'POST' and 'Decrement' in request.POST:
        operator = Operator.objects.get(id=operator_id)
        operator.secondary_weapon_ammo_amount -= 1
        operator.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def create_operator(request):
    form = OperatorForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {"form": form}
    return render(request, "create_operator.html", context)

def show_xml(request):
    data = Operator.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Operator.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Operator.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Operator.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_html(request):
    operators = Operator.objects.all()
    roster_size = len(operators)
    roster_size_message = f"You have {roster_size} operator(s) in your roster"
    
    context = {
        'operators': operators,
        'roster_size': roster_size_message,
    }

    return render(request, "show_only_operators.html", context)

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    operators = Operator.objects.filter(user=request.user)
    roster_size = Operator.objects.filter(user=request.user).count()

    context = {
        'creator': request.user.username,
        'class': 'PBP C',
        'operators': operators,
        'roster_size': roster_size,
        'last_login': request.COOKIES['last_login']
    }

    return render(request, "main.html", context)

def get_operator_json(request):
    operator_item = Operator.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', operator_item))

@csrf_exempt
def add_operator_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        unit = request.POST.get("unit")
        primary_weapon = request.POST.get("primary_weapon")
        secondary_weapon = request.POST.get("secondary_weapon")
        primary_weapon_ammo_amount = request.POST.get("primary_weapon_ammo_amount")
        secondary_weapon_ammo_amount = request.POST.get("secondary_weapon_ammo_amount")
        armor = request.POST.get("armor")
        speed = request.POST.get("speed")
        description = request.POST.get("description")
        price = request.POST.get("price")
        user = request.user

        new_operator = Operator(name=name, 
                               price=price,
                               unit=unit,
                               primary_weapon=primary_weapon,
                               secondary_weapon=secondary_weapon,
                               primary_weapon_ammo_amount=primary_weapon_ammo_amount,
                               secondary_weapon_ammo_amount=secondary_weapon_ammo_amount,
                               armor=armor,
                               speed=speed,
                               description=description, 
                               user=user)
        new_operator.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_operator_ajax(request, operator_id):
    if request.method == "DELETE":
        operator = Operator.objects.get(pk=operator_id, user=request.user)
        operator.delete()
        return HttpResponse(b"DELETED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def create_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        new_op = Operator.objects.create(
            user=request.user,
            name=data['name'],
            price=int(data['price']),
            primary_weapon=data['primary_weapon'],
            secondary_weapon=data['secondary_weapon'],
            primary_weapon_ammo_amount=int(data['primary_weapon_ammo_amount']),
            secondary_weapon_ammo_amount=int(data['secondary_weapon_ammo_amount']),
            armor=int(data['armor']),
            speed=int(data['speed']),
            description=data['description'],
            unit=data['unit']
        )

        new_op.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
def show_json_by_user(request):
    data = Operator.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")