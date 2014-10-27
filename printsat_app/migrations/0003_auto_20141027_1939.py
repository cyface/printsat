# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('printsat_app', '0002_auto_20141027_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telemetry',
            name='bat_temp',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
