from django.shortcuts import render, reverse
from django.views import generic

from packaging.models import Rack, Warehouse
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

    def form_valid(self, form):

        if form.is_valid():
            rack = form.save(commit=False)
            rack.current_available_capacity = rack.weight_capacity
            if rack.warehouse.current_available_capacity > rack.weight_capacity:
                rack.save()
            else:
                context = self.get_context_data(form=form)
                context.update({"error_message": "Rack of weight " + str(
                    rack.weight_capacity) + "kgs exceeds warehouse capacity only left with " + str(
                    rack.warehouse.current_available_capacity) + "kgs in space. Try reducing rack amount or choose a "
                                                                 "different Warehouse with more capacity "})
                return self.render_to_response(context)

        return super(RackCreateView, self).form_valid(form)

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
