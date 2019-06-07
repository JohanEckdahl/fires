from django.contrib import admin
from .models import Fire, Site, Parking


admin.site.register(Site)
admin.site.register(Parking)

class FireAdmin(admin.ModelAdmin):
    fields = ['quality', 'summary']
    actions = None
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Fire, FireAdmin)
