# Django forms for the application

from django.forms import Form, ModelForm, ValidationError
from django.forms import DateTimeField, ChoiceField, DateTimeInput
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

    FORMAT_NAME_CHOICES = (
        ('imm_extract', 'IMM'),
        ('load_cell_extract', 'Load Cell'),
        ('motion_extract', 'Motion'),
        ('msu_experiment', 'MSU Experiment'),
        ('power', 'Power'),
    )

    start_datetime = DateTimeField(label="Start Date/Time",
                                   initial="2013-02-21 12:57:00",
                                   widget=DateTimeInput(attrs={'class': 'form-control'})
    )
    end_datetime = DateTimeField(label="End Date/Time",
                                 initial="2013-02-21 12:59:00",
                                 widget=DateTimeInput(attrs={'class': 'form-control'}))
    format_name = ChoiceField(choices=FORMAT_NAME_CHOICES)