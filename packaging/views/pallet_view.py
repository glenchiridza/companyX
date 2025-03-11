import uuid

from django.shortcuts import render, reverse
from django.views import generic

from packaging.models import Pallet, Package
from packaging.forms import PalletForm


class PalletListView(generic.ListView):
    template_name = 'packaging/pallet_list.html'
    context_object_name = 'pallets'

    def get_queryset(self):
        pallet = Pallet.objects.all()
        return pallet


class PalletDetailView(generic.DetailView):
    template_name = 'packaging/pallet_detail.html'
    context_object_name = 'pallet'

    def get_queryset(self):
        return Pallet.objects.filter(pk=self.kwargs['pk'])


class PalletCreateView(generic.CreateView):
    template_name = 'packaging/pallet_create.html'
    form_class = PalletForm

    def form_valid(self, form):

        if form.is_valid():
            pallet = form.save(commit=False)
            pallet.serial_number = str(uuid.uuid4())
            pallet.current_available_capacity = pallet.capacity_limit_number
            pallet.save()

        return super(PalletCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('packaging-service:pallet_list')


class PalletUpdateView(generic.UpdateView):
    template_name = 'packaging/pallet_update.html'
    form_class = PalletForm

    def get_queryset(self):
        return Pallet.objects.filter(pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('packaging-service:pallet_list')


class PalletDeleteView(generic.DeleteView):
    template_name = 'packaging/delete.html'

    def get_queryset(self):
        return Pallet.objects.filter(pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('packaging-service:pallet_list')
