from django.shortcuts import render, reverse
from django.views import generic

from packaging.models import Rack,Warehouse
from packaging.forms import RackForm


class RackListView(generic.ListView):
    template_name = 'packaging/rack_list.html'
    context_object_name = 'racks'

    def get_queryset(self):
        rack = Rack.objects.all()
        return rack


class RackDetailView(generic.DetailView):
    template_name = 'packaging/rack_detail.html'
    context_object_name = 'rack'

    def get_queryset(self):
        return Rack.objects.filter(pk=self.kwargs['pk'])


class RackCreateView(generic.CreateView):
    template_name = 'packaging/rack_create.html'
    form_class = RackForm

    def get_success_url(self):
        return reverse('packaging-service:rack_list')


class RackUpdateView(generic.UpdateView):
    template_name = 'packaging/rack_update.html'
    form_class = RackForm

    def get_queryset(self):
        return Rack.objects.filter(pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('packaging-service:rack_list')


class RackDeleteView(generic.DeleteView):
    template_name = 'packaging/delete.html'

    def get_queryset(self):
        return Rack.objects.filter(pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('packaging-service:rack_list')
