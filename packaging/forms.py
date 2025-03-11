from django.forms import ModelForm

from .models import Warehouse, Rack, Pallet


class WareHouseForm(ModelForm):
    class Meta:
        model = Warehouse
        fields = "__all__"
        exclude = ('current_available_capacity',)


class RackForm(ModelForm):
    class Meta:
        model = Rack
        fields = "__all__"
        exclude = ('current_available_capacity',)


class PalletForm(ModelForm):
    class Meta:
        model = Pallet
        fields = "__all__"
        exclude = ('current_available_capacity',)