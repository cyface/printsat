# Django forms for the application

from django.forms import Form, ModelForm, ValidationError
from django.forms import DateTimeField, ChoiceField, DateTimeInput, RadioSelect
from printsat_app.models import Upload
from django.core.validators import RegexValidator
import re


class TelemetryUploadForm(ModelForm):
    """Upload files with this form"""

    class Meta:
        model = Upload

    def clean(self, *args, **kwargs):
        cleaned_data = super(TelemetryUploadForm, self).clean()
        if cleaned_data:
            if not re.search('.*\.csv$', cleaned_data.get("file").name):
                raise ValidationError("Uploaded Files Must Be In CSV Format!")
        return cleaned_data


class TelemetryQueryForm(Form):
    """Query Telem With This Form"""

    FORMAT_NAME_CHOICES = (
        ('imm_extract', 'IMM'),
        ('load_cell_extract', 'Load Cell'),
        ('motion_extract', 'Motion'),
        ('msu_experiment_extract', 'MSU Experiment'),
        ('power_extract', 'Power'),
    )

    start_datetime = DateTimeField(label="Start Date/Time",
                                   initial="2014-10-25 15:38:00",
                                   help_text="Start date/time in YYYY-MM-DD HH:MM:SS format.",
                                   widget=DateTimeInput())
    end_datetime = DateTimeField(label="End Date/Time",
                                 initial="2014-10-25 15:48:00",
                                 help_text="End date/time in YYYY-MM-DD HH:MM:SS format.",
                                 widget=DateTimeInput())
    format_name = ChoiceField(choices=FORMAT_NAME_CHOICES,
                              label="Format",
                              initial="imm_extract",
                              help_text="Extract format, which determines extract columns.",
                              widget=RadioSelect())
