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
            pallet.current_available_capacity = pallet.capacity_limit_number
            packages_in_pallet = Package.objects.get(pallet=pallet)
            total_mass = 0
            for package in packages_in_pallet:
                total_mass += package.quality_mark.mass_of_product
            if pallet.rack.current_available_capacity > total_mass:
                pallet.save()
            else:
                context = self.get_context_data(form=form)
                context.update({"error_message": "Pallet of capacity : " + str(
                    total_mass) + "kgs exceeds Rack capacity only left with " + str(
                    pallet.rack.current_available_capacity) + "kgs in space. Try reducing pallet amount or choose a "
                                                                 "different Rack with more capacity "})
                return self.render_to_response(context)

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
