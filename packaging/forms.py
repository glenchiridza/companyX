from django.forms import ModelForm

from .models import Warehouse, Rack, Pallet, Line, Package


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

class PackageForm(ModelForm):
    class Meta:
        model = Package
        fields = "__all__"


class LineForm(ModelForm):
    class Meta:
        model = Line
        fields = "__all__"
        exclude = ('current_available_capacity','is_special_case')


class PalletForm(ModelForm):
    class Meta:
        model = Pallet
        fields = "__all__"
        exclude = ('current_available_capacity', 'serial_number',)