import uuid

from django.shortcuts import render, reverse
from django.views import generic

from packaging.models import Line, Package
from packaging.forms import LineForm


class LineListView(generic.ListView):
    template_name = 'packaging/line_list.html'
    context_object_name = 'lines'

    def get_queryset(self):
        line = Line.objects.all()
        return line


class LineDetailView(generic.DetailView):
    template_name = 'packaging/line_detail.html'
    context_object_name = 'line'

    def get_queryset(self):
        return Line.objects.filter(pk=self.kwargs['pk'])


# make additional checks on capacity before saving
class LineCreateView(generic.CreateView):
    template_name = 'packaging/line_create.html'
    form_class = LineForm

    def form_valid(self, form):

        if form.is_valid():
            line = form.save(commit=False)
            line.serial_number = str(uuid.uuid4())
            line.current_available_capacity = line.max_capacity_allowed_in_kgs
            if line.warehouse.current_available_capacity > line.max_capacity_allowed_in_kgs:
                line.save()
            else:
                context = self.get_context_data(form=form)
                context.update({"error_message": "Line of weight " + str(
                    line.max_capacity_allowed_in_kgs) + "kgs exceeds warehouse capacity only left with " + str(
                    line.warehouse.current_available_capacity) + "kgs in space. Try reducing rack amount or choose a "
                                                                 "different Warehouse with more capacity "})
                return self.render_to_response(context)

        return super(LineCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('packaging-service:line_list')


class LineUpdateView(generic.UpdateView):
    template_name = 'packaging/line_update.html'
    form_class = LineForm

    def get_queryset(self):
        return Line.objects.filter(pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('packaging-service:line_list')


class LineDeleteView(generic.DeleteView):
    template_name = 'packaging/delete.html'

    def get_queryset(self):
        return Line.objects.filter(pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('packaging-service:line_list')
