# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-31 13:48
from __future__ import unicode_literals

import blog.fields
import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160731_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zipcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zipcode', models.CharField(max_length=7)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=blog.fields.PhoneNumberField(max_length=20, validators=[blog.validators.phone_number_validator, blog.validators.phone_number_validator, blog.validators.phone_number_validator]),
        ),
    ]