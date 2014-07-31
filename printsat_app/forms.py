# Django forms for the application

from django.forms import FileField, Form


class TelemetryUploadForm(Form):
    """Upload files with this form"""
    file = FileField()