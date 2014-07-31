import csv
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from printsat_app.models import Telemetry
from django.utils.encoding import smart_str


class HomePage (TemplateView):
    template_name = 'home.html'


class CannedExtract (View):

    def get(self, request, *args, **kwargs):
        queryset = Telemetry.objects.all()[:5]
        response = HttpResponse(mimetype='text/csv')
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