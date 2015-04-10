# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('microevents', '0010_auto_20150410_0136'),
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
    ]
