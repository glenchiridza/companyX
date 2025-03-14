from django.contrib import admin

from user.models import User, LogisticsManager, \
    Operator

admin.site.register(User)
admin.site.register(LogisticsManager)
admin.site.register(Operator)


# customize portal view
admin.site.site_header = "CompanyX APP"
admin.site.site_title = "CompanyX PORTAL"
admin.site.index_title = "CompanyX Portal"