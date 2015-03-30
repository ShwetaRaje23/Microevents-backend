# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('microevents', '0002_mecircles_meevents_memananger'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mecircles',
            name='circle_id',
        ),
        migrations.RemoveField(
            model_name='meevents',
            name='event_id',
        ),
        migrations.AddField(
            model_name='meevents',
            name='event_name',
            field=models.CharField(default=b'hue hue hue', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mecircles',
            name='circle_owner',
            field=models.ForeignKey(related_name='circle_owner', to='microevents.meUser'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mecircles',
            name='group_users',
            field=models.ManyToManyField(to='microevents.meUser'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='memananger',
            name='event_id',
            field=models.ForeignKey(to='microevents.meEvents'),
            preserve_default=True,
        ),
    ]
