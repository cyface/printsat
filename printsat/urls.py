from django.conf.urls import patterns, include, url

from django.contrib import admin
from printsat_app.views import HomePage, Extract, ExtractPage, UploadPage

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', HomePage.as_view(), name="home"),
                       url(r'^extract/csv/(?P<format_name>\w+)', Extract.as_view(), name="extract_csv"),
                       url(r'^extract/$', ExtractPage.as_view(), name="extract_page"),
                       url(r'^upload/', UploadPage.as_view(), name="upload_page"),
                       url(r'^admin/', include(admin.site.urls)),
)
