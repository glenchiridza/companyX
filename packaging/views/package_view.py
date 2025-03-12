import uuid

from django.shortcuts import render, reverse
from django.views import generic

from packaging.models import Package, Pallet, Line
from packaging.forms import PackageForm


# shows list of all packages existing
class PackageListView(generic.ListView):
    template_name = 'packaging/package_list.html'
    context_object_name = 'packages'

    def get_queryset(self):
        package = Package.objects.all()
        return package


# class to view the details of the package. gets record by primary key
class PackageDetailView(generic.DetailView):
    template_name = 'packaging/package_detail.html'
    context_object_name = 'package'

    def get_queryset(self):
        return Package.objects.filter(pk=self.kwargs['pk'])


# create view auto generates serial checks package type to determine whether it should be placed in pallet first or
# directly into line checks if capacity to hold the package is still there in terms of either limit number or
# capacity in kgs, if so then adds to pallet outputs error message if package cannot fit in provided space (Line/pallet)
class PackageCreateView(generic.CreateView):
    template_name = 'packaging/package_create.html'
    form_class = PackageForm

    def form_valid(self, form):
        if form.is_valid():
            package = form.save(commit=False)
            package.serial_number = str(uuid.uuid4())
            if "LOOSE" in package.package_type:
                pallets = Pallet.objects.all()
                for pallet in pallets:
                    if pallet.capacity_limit_number > 0 and pallet.rack.current_available_capacity > package.mass_of_product:
                        package.pallet = pallet
                        package.save()
            elif "CARTON" in package.package_type:
                lines = Line.objects.all()
                for line in lines:
                    if line.max_packages > 0 and line.current_available_capacity > package.mass_of_product:
                        package.line = line
                        package.save()

            else:
                context = self.get_context_data(form=form)
                context.update({"error_message": "Package could not be loaded : Package Type" + str(
                    package.package_type) + "Mass of : " + str(package.mass_of_product) + "kgs exceeds capacity "
                                                                                          "allocated. Try Adding a new "
                                                                                          "Line or Pallet to collection"})

        return super(PackageCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('packaging-service:package_list')


# view is meant to handle update of model
class PackageUpdateView(generic.UpdateView):
    template_name = 'packaging/package_update.html'
    form_class = PackageForm

    def get_queryset(self):
        return Package.objects.filter(pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('packaging-service:package_list')


class PackageDeleteView(generic.DeleteView):
    template_name = 'packaging/delete.html'

    def get_queryset(self):
        return Package.objects.filter(pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('packaging-service:package_list')
