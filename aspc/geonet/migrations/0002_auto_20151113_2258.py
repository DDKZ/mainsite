# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('geonet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='geouser',
            name='requests',
            field=models.ManyToManyField(related_name='_geouser_requests_+', to='geonet.GeoUser'),
        ),
        migrations.AlterField(
            model_name='geouser',
            name='user',
            field=models.OneToOneField(related_name='geouser', to=settings.AUTH_USER_MODEL),
        ),
    ]
