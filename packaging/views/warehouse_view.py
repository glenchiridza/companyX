from django.db.models import Q
from django.shortcuts import render, reverse
from django.views import generic


from user.models import User
from packaging.models import Warehouse, Line, Rack, Pallet, Package
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

    def get_context_data(self, **kwargs):
        warehouse = Warehouse.objects.get(pk=self.kwargs['pk'])
        lines = warehouse.line_set.all()
        racks = warehouse.rack_set.all()
        pallets = Pallet.objects.filter(rack=racks.first())
        packages = Package.objects.filter(Q(line_id=lines.first().id) | Q(pallet_id=pallets.first().id))

        context = super().get_context_data(**kwargs)
        context.update({'lines': lines, 'racks': racks, 'pallets': pallets, 'packages': packages})
        return context


class WareHouseCreateView(generic.CreateView):
    template_name = 'packaging/ware_house_create.html'
    form_class = WareHouseForm

    def form_valid(self, form):
        if form.is_valid():
            warehouse = form.save(commit=False)
            warehouse.current_available_capacity = warehouse.max_allowed_capacity_in_kgs
            warehouse.save()

        return super(WareHouseCreateView, self).form_valid(form)

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
