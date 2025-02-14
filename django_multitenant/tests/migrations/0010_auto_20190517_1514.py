# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-17 15:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_multitenant.fields
import django_multitenant.mixins


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0009_auto_20190412_0839"),
    ]

    operations = [
        migrations.CreateModel(
            name="TempModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tests.Account",
                        db_constraint=False,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(django_multitenant.mixins.TenantModelMixin, models.Model),
        ),
    ]
