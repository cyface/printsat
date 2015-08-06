import csv
from django.views.generic import FormView, TemplateView, View
from django.http import HttpResponse
from .models import Telemetry
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.conf import settings
from printsat_app.import_utils import import_data
import os
from django.core import serializers
from rest_pandas import PandasView, PandasSerializer
from .forms import TelemetryExtractForm, TelemetryUploadForm, TelemetryGraphForm, get_min_telem_date, get_max_telem_date


class HomePage(TemplateView):
    """Display Home Page"""
    template_name = 'home.html'


class ExtractPage(FormView):
    """Display Extract Page"""
    template_name = "extract.html"
    form_class = TelemetryExtractForm

    def form_valid(self, form):
        format_name = form.cleaned_data.get("format_name", "imm_extract")
        format_spec_file = file(os.path.join(settings.FORMATS_DIR, format_name + '.csv'))
        format_spec = format_spec_file.readline().rstrip().split(",")
        queryset = Telemetry.objects.filter(
            ps_time__lte=form.cleaned_data.get("end_datetime", get_min_telem_date()),
            ps_time__gte=form.cleaned_data.get("start_datetime", get_max_telem_date())
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
        if form:
            result = import_data(form.cleaned_data.get("file"))
            messages.success(self.request, result)
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


class PanelGraphView(FormView):
    """Show a Solar Panel Current Graph"""

    template_name = 'panel_graph.html'
    form_class = TelemetryGraphForm
    success_url = reverse_lazy('panel_graph_page')

    def form_valid(self, form):
        """
        If the form is valid, re-render the page with the completed form and new data.
        """
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        form = kwargs.get('form')

        if form.is_valid():
            panel_data = Telemetry.objects.filter(ps_time__range=(form.cleaned_data['start_datetime'], form.cleaned_data['end_datetime']))
        else:
            panel_data = Telemetry.objects.filter(ps_time__range=(get_min_telem_date(), get_max_telem_date()))

        return {
            'data': serializers.serialize('json', panel_data, fields=('ps_time_seconds', 'bat_v', 'sp1_i_5', 'sp2_i_6', 'sp3_i_7', 'sp4_i_8')),
            'form': form
        }


class MSUExpGraphView(FormView):
    """Show a MSU Experiment Graph"""

    template_name = 'msu_graph.html'
    form_class = TelemetryGraphForm
    success_url = reverse_lazy('msu_graph_page')

    def form_valid(self, form):
        """
        If the form is valid, re-render the page with the completed form and new data.
        """
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        form = kwargs.get('form')

        if form.is_valid():
            msu_data = Telemetry.objects.filter(ps_time__range=(form.cleaned_data['start_datetime'], form.cleaned_data['end_datetime']))
        else:
            msu_data = Telemetry.objects.filter(ps_time__range=(get_min_telem_date(), get_max_telem_date()))

        return {
            'data': serializers.serialize('json', msu_data, fields=('ps_time_seconds', 'msu_temp_1', 'msu_temp_2', 'msu_temp_3', 'msu_temp_4')),
            'form': form
        }


class PandaView(TemplateView):
    template_name = "pandas.html"


class PanelSerializer(PandasSerializer):
    class Meta:
        model = Telemetry
        fields = ('id', 'ps_time_seconds', 'sp1_i_5')


class PanelSeriesView(PandasView):
    model = Telemetry
    serializer_class = PanelSerializer

    # In response to get(), the underlying Django REST Framework ListAPIView
    # will load the default queryset (self.model.objects.all()) and then pass
    # it to the following function.

    def filter_queryset(self, qs):
        # At this point, you can filter queryset based on self.request or other
        # settings (useful for limiting memory usage)
        return qs

    # Then, the included PandasSerializer will serialize the queryset into a
    # simple list of dicts (using the DRF ModelSerializer).  To customize
    # which fields to include, subclass PandasSerializer and set the
    # appropriate ModelSerializer options.  Then, set the serializer_class
    # property on the view to your PandasSerializer subclass.

    # Next, the PandasSerializer will load the ModelSerializer result into a
    # DataFrame and pass it to the following function on the view.

    def transform_dataframe(self, dataframe):
        # Here you can transform the dataframe based on self.request
        # (useful for pivoting or computing statistics)
        return dataframe

        # Finally, the included Renderers will process the dataframe into one of
        # the output formats below.
