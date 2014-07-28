"""Admin site customizations for Printsat"""

# pylint: disable=C0111,E0602,F0401,R0904,E1002

from django.contrib import admin
from django.db import models

from printsat_app.models import Telemetry
from django.contrib.admin import site


class TelemetryAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_created'

admin.site.register(Telemetry, TelemetryAdmin)
