from django.shortcuts import render, reverse
from django.views import generic

from user.models import User
from packaging.models import Warehouse
from packaging.forms import WareHouseForm



class WareHouseListView(generic.ListView):
    template_name = 'packaging/ware_house_list.html'
    context_object_name = 'warehouses'

    def get_queryset(self):
        warehouse = Warehouse.objects.all()
        return warehouse


class WareHouseDetailView(generic.DetailView):
    template_name = 'packaging/ware_house_detail.html'
    context_object_name = 'warehouse'

    def get_queryset(self):
        return Warehouse.objects.filter(pk=self.kwargs['pk'])


class WareHouseCreateView(generic.CreateView):
    template_name = 'packaging/ware_house_create.html'
    form_class = WareHouseForm

    def get_success_url(self):
        return reverse('packaging-service:warehouse_list')


class WareHouseUpdateView(generic.UpdateView):
    template_name = 'packaging/ware_house_update.html'
    form_class = WareHouseForm

    def get_queryset(self):
        return Warehouse.objects.filter(pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('packaging-service:warehouse_list')


class WareHouseDeleteView(generic.DeleteView):
    template_name = 'packaging/delete.html'

    def get_queryset(self):
        return Warehouse.objects.filter(pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('packaging-service:warehouse_list')