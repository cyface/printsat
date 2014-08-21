"""Automated unitests for the printsat"""

# pylint: disable=C0103,C0111,R0902,R0904,W0401,W0614

from django.test import TestCase
from printsat_app.models import *  #@UnusedWildImport


class TestTelemetryQuery(TestCase):
    """Test Querying Telemetry"""

    fixtures = ["printsat_telem_fixture.json"]

    def setup(self):
        pass

    def test_date_query(self):
        results = Telemetry.objects.all()
        print len(results)
