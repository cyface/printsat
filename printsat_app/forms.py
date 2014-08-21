# Django forms for the application

from django.forms import Form, ModelForm, ValidationError
from django.forms import DateField
from printsat_app.models import Upload
from printsat_app.import_utils import import_data
from django.core.validators import RegexValidator
import re


class TelemetryUploadForm(ModelForm):
    """Upload files with this form"""

    class Meta:
        model = Upload

    def clean(self, *args, **kwargs):
        cleaned_data = super(TelemetryUploadForm, self).clean()
        print cleaned_data.get("file")
        if not re.search('.*\.csv$', cleaned_data.get("file").name):
            raise ValidationError("Uploaded Files Must Be In CSV Format!")

        import_data(cleaned_data.get("file"))

        return cleaned_data


class TelemetryQueryForm(Form):
    """Query Telem With This Form"""

    start_date = DateField()
    end_date = DateField()