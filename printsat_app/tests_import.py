"""Automated unitests for the printsat telem db importer"""

# pylint: disable=C0103,C0111,R0902,R0904,W0401,W0614

from django.test import TestCase
from django.conf import settings
from printsat_app.models import *  #@UnusedWildImport
from printsat_app.import_utils import import_data
from decimal import Decimal
import datetime
import os


class TestTelemetryImportsEmptyDB(TestCase):
    """Test Importing Telem Into an Empty DB"""

    def setup(self):
        pass

    def test_live_telem(self):
        live_telem_file_path = os.path.join(settings.BASE_DIR, "printsat_app", "test_data", "WD0E_Eng_10252014.csv")
        import_data(live_telem_file_path)
        results = Telemetry.objects.filter(
            ps_time__lte="2014-10-25 15:40:00",
            ps_time__gte="2014-10-25 15:38:00").values_list("bat_v", flat=True)
        self.assertEquals(12, len(results))
        self.assertAlmostEquals(Decimal(135.27), sum(results))
        results = Telemetry.objects.get(ps_time="2014-10-25 15:38:12")
        self.assertIsNone(results.test_v_1)

    def test_dump_telem(self):
        dump_telem_file_path = os.path.join(settings.BASE_DIR, "printsat_app", "test_data", "WD0E_DumpCalc_10252014.csv")
        import_data(dump_telem_file_path)
        results = Telemetry.objects.filter(
            ps_time__lte="2014-10-25 15:40:00",
            ps_time__gte="2014-10-25 15:38:00").values_list("test_v_1", flat=True)
        self.assertEquals(12, len(results))
        self.assertAlmostEquals(Decimal(0.67), sum(results))
        results = Telemetry.objects.get(ps_time="2014-10-25 15:38:12")
        self.assertIsNone(results.last_good_io_telem)