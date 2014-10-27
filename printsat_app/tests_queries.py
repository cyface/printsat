"""Automated unitests for the printsat telem db queries"""

# pylint: disable=C0103,C0111,R0902,R0904,W0401,W0614

from django.test import TestCase
from django.conf import settings
from printsat_app.models import *  #@UnusedWildImport
import datetime
import os


class TestTelemetryQuery(TestCase):
    """Test Querying Telemetry"""

    fixtures = ["updated_data.json"]

    def setup(self):
        pass

    def test_date_query(self):
        results = Telemetry.objects.filter(ps_time__lte="2014-10-25 15:40:00", ps_time__gte="2014-10-25 15:38:00")
        self.assertEqual(12, len(results))

    def test_file_format(self):
        format_spec_file = file(os.path.join(settings.BASE_DIR, "printsat_app", "formats", "imm_extract.csv"))
        format_spec = format_spec_file.readline().rstrip().split(",")
        results = Telemetry.objects.filter(
            ps_time__lte="2014-10-25 15:40:00",
            ps_time__gte="2014-10-25 15:38:00").values(*format_spec)
        self.assertEqual(12, len(results))
        self.assertNotIn("readrad_timeout_errs", results.field_names)