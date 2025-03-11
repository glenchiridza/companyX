from django.urls import path

from views.warehouse_view import (
    WareHouseListView, WareHouseCreateView, WareHouseDetailView, WareHouseUpdateView
)

app_name = 'packaging'

urlpatterns = [
    ### warehouse urls
    path('create-warehouse/', WareHouseCreateView.as_view(), name='warehouse_create'),
    path('list-warehouse/', WareHouseListView.as_view(), name='warehouse_list'),
    path('warehouse-detail/<int:pk>/', WareHouseDetailView.as_view(), name='warehouse_detail'),
    path('warehouse/<int:pk>/update', WareHouseUpdateView.as_view(), name='warehouse_update'),
]
