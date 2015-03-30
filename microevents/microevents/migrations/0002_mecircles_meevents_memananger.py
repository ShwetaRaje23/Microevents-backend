# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('microevents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='meCircles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('circle_id', models.IntegerField(default=0)),
                ('circle_name', models.CharField(max_length=30)),
                ('circle_owner', models.ForeignKey(related_name='circle_owner', to='microevents.meUser')),
                ('group_users', models.ManyToManyField(to='microevents.meUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='meEvents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_id', models.IntegerField(default=0)),
                ('venue', models.CharField(max_length=30)),
                ('date_time', models.DateTimeField(null=True, blank=True)),
                ('owner', models.ForeignKey(to='microevents.meUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='meMananger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_id', models.IntegerField(default=0)),
                ('circle_id', models.IntegerField(default=0)),
                ('user_id', models.IntegerField(default=0)),
                ('accept', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
