import csv
from django.views.generic import FormView, TemplateView, View
from django.http import HttpResponse
from printsat_app.models import Telemetry
from printsat_app.forms import TelemetryUploadForm
from django.utils.encoding import smart_str
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages


class HomePage(TemplateView):
    template_name = 'home.html'


class UploadPage(FormView):
    form_class = TelemetryUploadForm
    success_url = reverse_lazy('upload_page')
    template_name = "upload.html"

    def form_valid(self, form):
        form.save()
        #  @TODO: Add CSV import code hook here
        messages.success(self.request, 'File uploaded!')
        return super(UploadPage, self).form_valid(form)


class CannedExtract(View):
    def get(self, request, *args, **kwargs):
        queryset = Telemetry.objects.all()[:5]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=telemetry.csv'
        writer = csv.writer(response, csv.excel)
        response.write(u'\ufeff'.encode('utf8'))
        writer.writerow([
            smart_str(u"ID"),
            smart_str(u"PS_Time"),
            smart_str(u"Station"),
        ])
        for obj in queryset:
            writer.writerow([
                smart_str(obj.pk),
                smart_str(obj.ps_time),
                smart_str(obj.station),
            ])
        return response