from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Equipment
from .forms import EquipmentForm, ExampleForm


def index(request):
    return render(request, 'fundation_base.html')


def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'equipment/equipment_list.html', {'equipments': equipments})


def equipment_create(request):
    equipment_form = EquipmentForm(data=request.POST)
    if equipment_form.is_valid():
        new_equipment = equipment_form.save(commit=False)
        new_equipment.save()
    else:
        equipment_form = EquipmentForm()

    return render(request, 'equipment/create.html', {'equipment_form': equipment_form})


def test_form(request):
    f = ExampleForm(data=request.POST)
    return render(request, 'equipment/test.html', {'example_form': f})


class EquipmentList(ListView):
    model = Equipment


class EquipmentDetail(DetailView):
        model = Equipment


class EquipmentCreate(CreateView):
    model = Equipment
    # form_class = EquipmentForm
    fields = ('type', 'serial_no')


class EquipmentUpdate(UpdateView):
    model = Equipment
    fields = ('type', 'serial_no')


class EquipmentDelete(DeleteView):
    model = Equipment
    success_url = reverse_lazy('equipment-list')