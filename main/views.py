from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import OperatorForm
from django.urls import reverse
from main.models import Operator
from django.http import HttpResponse
from django.core import serializers

def create_operator(request):
    form = OperatorForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse("main:show_main"))
    
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
def show_main(request):
    operators = Operator.objects.all()
    roster_size = len(operators)
    roster_size_message = f"You have {roster_size} operator(s) in your roster"

    context = {
        'creator': 'Dimas Herjunodarpito Notoprayitno',
        'student_id': '2206081282',
        'class': 'PBP C',
        'operators': operators,
        'roster_size': roster_size_message,
    }

    return render(request, "main.html", context)