from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()
from printsat_app.views import HomePage, CannedExtract, UploadPage

urlpatterns = patterns('',
                       url(r'^$', HomePage.as_view(), name="home"),
                       url(r'^canned/', CannedExtract.as_view(), name="canned"),
                       url(r'^upload/', UploadPage.as_view(), name="upload_page"),
                       url(r'^admin/', include(admin.site.urls)),
                       )
