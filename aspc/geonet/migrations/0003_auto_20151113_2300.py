# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geonet', '0002_auto_20151113_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geouser',
            name='latitude',
            field=models.DecimalField(default=34.10079, max_digits=10, decimal_places=6),
        ),
        migrations.AlterField(
            model_name='geouser',
            name='longitude',
            field=models.DecimalField(default=-117.71008, max_digits=10, decimal_places=6),
        ),
    ]
