# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('printsat_app', '0003_auto_20141027_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telemetry',
            name='ps_time_seconds',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='upload',
            name='file',
            field=models.FileField(upload_to=b'C:/Users/tlwhit2/PycharmProjects/printsat\\media_root'),
            preserve_default=True,
        ),
    ]
