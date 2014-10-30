from django.conf.urls import patterns, include, url

from django.contrib import admin
from printsat_app.views import HomePage, ExtractCSV, ExtractPage, MSUExpGraphView, PanelGraphView, PandaView, UploadPage

from printsat_app.rest_api import api_router

from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns

from printsat_app.views import TimeSeriesView

urlpatterns = \
    patterns('',
             url(r'^$', HomePage.as_view(), name="home"),
             url(r'^extract/csv/(?P<format_name>\w+)', ExtractCSV.as_view(), name="extract_csv"),
             url(r'^extract/$', ExtractPage.as_view(), name="extract_page"),
             url(r'^upload/', UploadPage.as_view(), name="upload_page"),
             url(r'^graph/panel/', PanelGraphView.as_view(), name="panel_graph_page"),
             url(r'^graph/msu/', MSUExpGraphView.as_view(), name="msu_graph_page"),
             url(r'^api/', include(api_router.urls)),
             url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
             url(r'^data/', TimeSeriesView.as_view()),
             url(r'^pandas/', PandaView.as_view()),
             url(r'^admin/', include(admin.site.urls)),
    )
