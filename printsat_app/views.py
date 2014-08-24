import csv
from django.views.generic import FormView, TemplateView, View
from django.http import HttpResponse
from printsat_app.models import Telemetry
from printsat_app.forms import TelemetryQueryForm, TelemetryUploadForm
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.conf import settings
import os


class HomePage(TemplateView):
    """Display Home Page"""
    template_name = 'home.html'


class ExtractPage(FormView):
    """Display Extract Page"""
    template_name = "extract.html"
    form_class = TelemetryQueryForm

    def form_valid(self, form):
        format_name = form.cleaned_data.get("format_name", "imm_extract")
        format_spec_file = file(os.path.join(settings.FORMATS_DIR, format_name + '.csv'))
        format_spec = format_spec_file.readline().rstrip().split(",")
        queryset = Telemetry.objects.filter(
            ps_time__lte=form.cleaned_data.get("end_datetime", '2014-10-01 10:00:00'),
            ps_time__gte=form.cleaned_data.get("start_datetime", '2014-09-01 10:00:00')
        ).values_list(*format_spec)
        if len(queryset) < 1:
            messages.error(self.request, 'Query Returned No Telemetry!')
            return super(ExtractPage, self).get(self)
        else:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=telemetry.csv'
            writer = csv.writer(response, csv.excel)
            writer.writerow(format_spec)
            for obj in queryset:
                writer.writerow(obj)
            return response


class UploadPage(FormView):
    """Display Upload Page"""
    form_class = TelemetryUploadForm
    success_url = reverse_lazy('upload_page')
    template_name = "upload.html"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'File uploaded!')
        return super(UploadPage, self).form_valid(form)


class ExtractCSV(View):
    """Provide extract of telemetry data
        kwarg: 'format_name' - name of CSV file (without .csv) in the 'formats' dir to use to determine output fields
    """

    def get(self, request, *args, **kwargs):
        format_name = kwargs.get("format_name", "imm_extract")
        format_spec_file = file(os.path.join(settings.FORMATS_DIR, format_name + '.csv'))
        format_spec = format_spec_file.readline().rstrip().split(",")
        queryset = Telemetry.objects.all().values_list(*format_spec)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=telemetry.csv'
        writer = csv.writer(response, csv.excel)
        writer.writerow(format_spec)
        for obj in queryset:
            writer.writerow(obj)
        return response

