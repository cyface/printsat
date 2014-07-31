"""
##############################################
#####-----Printsat Data Importer-------#######
##############################################
"""

# pylint: disable=E0611,F0401,W0401,W0614,W0612,R0914,R0902

import csv  # first we need import necessary lib:csv
import datetime
import time
import os
from printsat_app.models import *
from django.conf import settings
from django.utils.timezone import utc


def import_data():
    """Import Data"""

    telemetry_header_file = open(os.path.join(settings.BASE_DIR, "printsat_app", "formats", "printsat_telemetry_headers.csv"))
    telemetry_headers = csv.DictReader(telemetry_header_file)
    telemetry_file = open(os.path.join(settings.BASE_DIR, "printsat_app", "test_data", "WD0E_DumpCalc_10292012.csv"))
    telemetry_list = csv.DictReader(telemetry_file, fieldnames=telemetry_headers.fieldnames)

    # Loop through the rows in the CSV
    for row in telemetry_list:
        # Create a telemetry object in the database based on the current row

        if telemetry_list.line_num == 1:
            station = row.get('ps_time')
        elif telemetry_list.line_num == 2:
            lat = row.get('ps_time')
            lon = row.get('ps_time_calc')
        elif telemetry_list.line_num == 3:
            program = row.get('ps_time')
            telem_type = row.get('ps_time_calc')
        elif telemetry_list.line_num == 4:
            pass  # Header Row
        else:
            row.pop("unused1", None)
            row.pop("unused2", None)
            row.pop("unused3", None)
            row.pop("unused4", None)
            row.pop("unused5", None)
            row.pop("unused6", None)
            row.pop("unused7", None)
            row.pop("unused8", None)
            row['station'] = station
            row['lat'] = lat
            row['lon'] = lon
            row['program'] = program
            row['telem_type'] = telem_type
            time_value = time.strptime(row.get('ps_time', '01.01.1900 00:00:00'), '%m.%d.%Y %H:%M:%S')
            row['ps_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time_value) + "+0000"
            row['ps_time_calc'] = datetime.datetime.fromtimestamp(float(row.get('ps_time_calc')), tz=utc)

            telemetry = Telemetry.objects.create(**row)

            # Save the telemetry!
            telemetry.save()
            print telemetry


# #### MAIN FUNCTION TO RUN IF THIS SCRIPT IS CALLED ALONE ##
if __name__ == "__main__":
    import_data()