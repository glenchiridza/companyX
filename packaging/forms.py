from django.forms import ModelForm

from .models import Warehouse, Rack


class WareHouseForm(ModelForm):
    class Meta:
        model = Warehouse
        fields = "__all__"


class RackForm(ModelForm):
    class Meta:
        model = Rack
        fields = "__all__"
