# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0031_auto_20171030_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('dept', models.ForeignKey(to='user_login.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Viewhistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='company',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 30, 19, 24, 33, 828000, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 30, 19, 24, 33, 828000, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AddField(
            model_name='viewhistory',
            name='user',
            field=models.ForeignKey(to='user_login.Customer'),
        ),
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.ForeignKey(to='user_login.Item'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(to='user_login.Customer'),
        ),
        migrations.AddField(
            model_name='buy',
            name='item',
            field=models.ForeignKey(to='user_login.Item'),
        ),
        migrations.AddField(
            model_name='buy',
            name='user',
            field=models.ForeignKey(to='user_login.Customer'),
        ),
    ]
