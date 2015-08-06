# Django forms for the application

from django.forms import Form, ModelForm, ValidationError
from django.forms import DateTimeField, ChoiceField, DateTimeInput, RadioSelect
from django.db.models import Max, Min
from .models import Telemetry, Upload
from django.core.validators import RegexValidator
import re


def get_min_telem_date():
    return Telemetry.objects.aggregate(Min('ps_time')).get('ps_time__min')


def get_max_telem_date():
    return Telemetry.objects.aggregate(Max('ps_time')).get('ps_time__max')


class TelemetryUploadForm(ModelForm):
    """Upload files with this form"""

    class Meta:
        model = Upload
        fields = ['file']

    def clean(self, *args, **kwargs):
        cleaned_data = super(TelemetryUploadForm, self).clean()
        if cleaned_data:
            if not re.search('.*\.csv$', cleaned_data.get("file").name):
                raise ValidationError("Uploaded Files Must Be In CSV Format!")
        return cleaned_data


class TelemetryExtractForm(Form):
    """Query Telem With This Form"""

    FORMAT_NAME_CHOICES = (
        ('imm_extract', 'IMM'),
        ('load_cell_extract', 'Load Cell'),
        ('motion_extract', 'Motion'),
        ('msu_experiment_extract', 'MSU Experiment'),
        ('power_extract', 'Power'),
    )

    start_datetime = DateTimeField(label="Start Date/Time",
                                   initial=get_min_telem_date(),
                                   help_text="Start date/time in YYYY-MM-DD HH:MM:SS format.",
                                   widget=DateTimeInput())
    end_datetime = DateTimeField(label="End Date/Time",
                                 initial=get_max_telem_date(),
                                 help_text="End date/time in YYYY-MM-DD HH:MM:SS format.",
                                 widget=DateTimeInput())
    format_name = ChoiceField(choices=FORMAT_NAME_CHOICES,
                              label="Format",
                              initial="imm_extract",
                              help_text="Extract format, which determines extract columns.",
                              widget=RadioSelect())


class TelemetryGraphForm(Form):
    """Query Telem With This Form"""

    start_datetime = DateTimeField(label="Start Date/Time",
                                   initial=get_min_telem_date(),
                                   help_text="Start date/time in YYYY-MM-DD HH:MM:SS format.",
                                   widget=DateTimeInput())

    end_datetime = DateTimeField(label="End Date/Time",
                                 initial=get_max_telem_date(),
                                 help_text="End date/time in YYYY-MM-DD HH:MM:SS format.",
                                 widget=DateTimeInput())
