# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('microevents', '0008_auto_20150402_2229'),
    ]

    operations = [
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
            model_name='meevents',
            name='owner',
            field=models.ForeignKey(to='microevents.meUser'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='memanager',
            name='accept',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
