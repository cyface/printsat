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
from decimal import InvalidOperation
from django.db import IntegrityError


def import_data(telemetry_file_path):
    """Import Data"""

    if isinstance(telemetry_file_path, str):
        telemetry_file = open(telemetry_file_path)
    else:
        telemetry_file = telemetry_file_path

    if "DumpRaw" in telemetry_file.name:
        header_file_name = "printsat_raw_telemetry_headers.csv"
    else:
        header_file_name = "printsat_telemetry_headers.csv"

    telemetry_header_file = open(os.path.join(settings.BASE_DIR, "printsat_app", "formats", header_file_name))
    telemetry_headers = csv.DictReader(telemetry_header_file)
    telemetry_list = csv.DictReader(telemetry_file, fieldnames=telemetry_headers.fieldnames)

    station = ""
    lat = ""
    lng = ""
    program = ""
    telem_type = ""
    row_count = 0
    imported_rows = 0
    invalid_rows = 0
    duplicate_rows = 0

    # Loop through the rows in the CSV
    for row in telemetry_list:

        # Create a telemetry object in the database based on the current row
        if telemetry_list.line_num == 1:
            station = row.get('ps_time')
        elif telemetry_list.line_num == 2:
            lat = row.get('ps_time')
            lng = row.get('ps_time_seconds')
        elif telemetry_list.line_num == 3:
            program = row.get('ps_time')
            telem_type = row.get('ps_time_seconds')
        elif telemetry_list.line_num == 4:
            pass  # Header Row
        else:
            row_count += 1
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
            row['lng'] = lng
            row['program'] = program
            row['telem_type'] = telem_type

            try:
                time_value = time.strptime(row.get('ps_time', '01.01.1900 00:00:00'), '%m.%d.%Y %H:%M:%S')
                row['ps_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time_value)
                row['ps_time_seconds'] = datetime.datetime.fromtimestamp(float(row.get('ps_time_seconds')))
                telemetry = Telemetry.objects.create(**row)
                telemetry.save()
                imported_rows += 1
                print ("."),
            except (InvalidOperation, ValueError):
                print ("ERROR ON THIS ROW: "),
                print (row)
                invalid_rows += 1
            except IntegrityError:
                print ("DUPLICATE ROW: "),
                # print (row)
                duplicate_rows += 1

    result_string = "\n\rImported {0} rows. Did not import {1} duplicate rows and {2} invalid rows out of {3} total rows in the file.".format(imported_rows, duplicate_rows, invalid_rows, row_count)
    print (result_string)
    return result_string


# #### MAIN FUNCTION TO RUN IF THIS SCRIPT IS CALLED ALONE ##
if __name__ == "__main__":
    import_data(os.path.join(settings.BASE_DIR, "printsat_app", "test_data", "WD0E_DumpCalc_10292012.csv"))