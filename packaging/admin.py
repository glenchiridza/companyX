from django.contrib import admin

from packaging.models import Warehouse,Package,Rack,Pallet,Line

admin.site.register(Warehouse)
admin.site.register(Package)
admin.site.register(Rack)
admin.site.register(Pallet)
admin.site.register(Line)
