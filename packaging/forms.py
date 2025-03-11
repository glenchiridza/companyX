from django.forms import ModelForm

from .models import Warehouse


class WareHouseForm(ModelForm):
    class Meta:
        model = Warehouse
        fields = "__all__"
