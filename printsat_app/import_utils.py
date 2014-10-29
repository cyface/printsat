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
from django.core.exceptions import ObjectDoesNotExist

def import_data(telemetry_file_path):
    """Import Data"""

    if isinstance(telemetry_file_path, str):
        telemetry_file = open(telemetry_file_path)
    else:
        telemetry_file = telemetry_file_path

    if "Eng" in telemetry_file.name:
        header_file_name = "printsat_live_telemetry_headers.csv"
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
    ignored_rows = 0
    imported_rows = 0
    invalid_rows = 0
    updated_rows = 0

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
#                row['ps_time_seconds'] = datetime.datetime.fromtimestamp(float(row.get('ps_time_seconds')))
                
                try:
                    telemetry = Telemetry.objects.get(ps_time=row['ps_time'])
                    if telemetry.telem_type == 'Dump Calc' and row['telem_type'] == 'Dump Raw':
                        ignored_rows += 1  # Ignore Raw Rows if we aleady have a calc Row for same time
                    else:
                        Telemetry.objects.filter(ps_time=row['ps_time']).update(**row)
                        updated_rows += 1
                except ObjectDoesNotExist:
                    telemetry = Telemetry.objects.create(**row)
                    telemetry.save()
                    imported_rows += 1
                print ("."),
            except (InvalidOperation, ValueError):
                print ("ERROR ON THIS ROW: "),
                print (row)
                invalid_rows += 1

    result_string = "\n\rImported {0} rows, Updated {1} rows. There were {2} invalid rows, and {3} ignored rows out of {4} total rows in the file that were not imported.".format(imported_rows, updated_rows, invalid_rows, ignored_rows, row_count)
    print (result_string)
    return result_string


# #### MAIN FUNCTION TO RUN IF THIS SCRIPT IS CALLED ALONE ##
if __name__ == "__main__":
    import_data(os.path.join(settings.BASE_DIR, "printsat_app", "test_data", "WD0E_DumpCalc_10292012.csv"))
