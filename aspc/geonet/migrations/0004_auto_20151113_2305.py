# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('geonet', '0003_auto_20151113_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geouser',
            name='user',
            field=models.OneToOneField(related_name='geouser', null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
