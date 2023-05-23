from django.contrib import admin
from .models import *


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'nickname', 'phone']


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


@admin.register(MasterSchedule)
class MasterScheduleAdmin(admin.ModelAdmin):
    list_display = ['date', 'master', 'site']


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ['star_time', 'end_time']


@admin.register(ClientOffer)
class ClientServiceAdmin(admin.ModelAdmin):
    list_display = ['client', 'master_schedule', 'shift']

admin.site.register(Client, ClientAdmin)
admin.site.register(Master, MasterAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(MasterSchedule, MasterScheduleAdmin)
admin.site.register(Shift, ShiftAdmin)
admin.site.register(ClientOffer, ClientServiceAdmin)