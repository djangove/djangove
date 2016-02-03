# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-03 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_standardpage_template_string'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardpage',
            name='template_string',
            field=models.CharField(choices=[('pages/standard_page.html', 'Default Template'), ('pages/standard_page_full.html', 'Standard Page Full')], default='pages/standard_page.html', max_length=255),
        ),
    ]