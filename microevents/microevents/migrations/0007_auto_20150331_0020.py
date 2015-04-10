# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('microevents', '0006_auto_20150330_2353'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='meMananger',
            new_name='meManager',
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
    ]
