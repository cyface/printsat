"""Admin site customizations for Printsat"""

# pylint: disable=C0111,E0602,F0401,R0904,E1002

from django.contrib import admin
from printsat_app.models import Telemetry, Upload

class TelemetryAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_created'


class UploadAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_created'

admin.site.register(Telemetry, TelemetryAdmin)
admin.site.register(Upload, UploadAdmin)
