"""Automated unitests for the printsat"""

# pylint: disable=C0103,C0111,R0902,R0904,W0401,W0614

from django.test import TestCase
from printsat_app.models import *  #@UnusedWildImport
import datetime


class TestTelemetryQuery(TestCase):
    """Test Querying Telemetry"""

    fixtures = ["printsat_fixture.json"]

    def setup(self):
        pass

    def test_date_query(self):
        # start_date = datetime.datetime.strptime("12.16.2015 09:00:00", '%m.%d.%Y %H:%M:%S')
        # end_date = datetime.datetime.strptime("12.16.2015 10:00:00", '%m.%d.%Y %H:%M:%S')
        results = Telemetry.objects.filter(ps_time__lte="2015-12-16 10:00:00", ps_time__gte="2015-12-16 09:00:00")
        # print len(results)
        self.assertEqual(10, len(results))