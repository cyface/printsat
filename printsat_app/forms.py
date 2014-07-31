# Django forms for the application

from django.forms import ModelForm
from printsat_app.models import Upload


class TelemetryUploadForm(ModelForm):
    """Upload files with this form"""
    class Meta:
        model = Upload