import uuid

from django.shortcuts import render, reverse
from django.views import generic

from packaging.models import Package
from packaging.forms import PackageForm


class PackageListView(generic.ListView):
    template_name = 'packaging/package_list.html'
    context_object_name = 'packages'

    def get_queryset(self):
        package = Package.objects.all()
        return package


class PackageDetailView(generic.DetailView):
    template_name = 'packaging/package_detail.html'
    context_object_name = 'package'

    def get_queryset(self):
        return Package.objects.filter(pk=self.kwargs['pk'])


class PackageCreateView(generic.CreateView):
    template_name = 'packaging/package_create.html'
    form_class = PackageForm

    def form_valid(self, form):

        if form.is_valid():
            package = form.save(commit=False)
            package.serial_number = str(uuid.uuid4())
            package.current_available_capacity = package.capacity_limit_number
            package.save()

        return super(PackageCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('packaging-service:package_list')


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
