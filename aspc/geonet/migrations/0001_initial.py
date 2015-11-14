# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('longitude', models.DecimalField(default=-117.71008, max_digits=10, decimal_places=6)),
                ('latitude', models.DecimalField(default=34.10079, max_digits=10, decimal_places=6)),
                ('friends', models.ManyToManyField(related_name='_geouser_friends_+', to='geonet.GeoUser')),
                ('requests', models.ManyToManyField(related_name='_geouser_requests_+', to='geonet.GeoUser')),
                ('user', models.OneToOneField(related_name='geouser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
