from django.urls import path

from packaging.views.warehouse_view import (
    WareHouseListView, WareHouseCreateView, WareHouseDetailView, WareHouseUpdateView,WareHouseDeleteView
)

from packaging.views.rack_view import (
    RackListView, RackCreateView, RackDetailView, RackUpdateView,RackDeleteView
)

from packaging.views.pallet_view import (
    PalletListView, PalletCreateView, PalletDetailView, PalletUpdateView,PalletDeleteView
)

app_name = 'packaging'

urlpatterns = [
    ### warehouse urls
    path('create-warehouse/', WareHouseCreateView.as_view(), name='warehouse_create'),
    path('list-warehouse/', WareHouseListView.as_view(), name='warehouse_list'),
    path('warehouse-detail/<int:pk>/', WareHouseDetailView.as_view(), name='warehouse_detail'),
    path('warehouse/<int:pk>/update', WareHouseUpdateView.as_view(), name='warehouse_update'),
    path('warehouse/<int:pk>/delete', WareHouseDeleteView.as_view(), name='warehouse_delete'),

    ### rack urls
    path('create-rack/', RackCreateView.as_view(), name='rack_create'),
    path('list-rack/', RackListView.as_view(), name='rack_list'),
    path('rack-detail/<int:pk>/', RackDetailView.as_view(), name='rack_detail'),
    path('rack/<int:pk>/update', RackUpdateView.as_view(), name='rack_update'),
    path('rack/<int:pk>/delete', RackDeleteView.as_view(), name='rack_delete'),

    ### pallet urls
    path('create-pallet/', PalletCreateView.as_view(), name='pallet_create'),
    path('list-pallet/', PalletListView.as_view(), name='pallet_list'),
    path('pallet-detail/<int:pk>/', PalletDetailView.as_view(), name='pallet_detail'),
    path('pallet/<int:pk>/update', PalletUpdateView.as_view(), name='pallet_update'),
    path('pallet/<int:pk>/delete', PalletDeleteView.as_view(), name='pallet_delete'),
]
