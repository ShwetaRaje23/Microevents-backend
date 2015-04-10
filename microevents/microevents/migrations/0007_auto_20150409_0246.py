# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('microevents', '0006_auto_20150330_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='meManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('circle_id', models.IntegerField(default=0)),
                ('user_id', models.IntegerField(default=0)),
                ('accept', models.IntegerField(default=0)),
                ('event', models.ForeignKey(to='microevents.meEvents')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='memananger',
            name='event_id',
        ),
        migrations.DeleteModel(
            name='meMananger',
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
