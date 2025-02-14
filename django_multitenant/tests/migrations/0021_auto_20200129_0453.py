# Generated by Django 2.2.9 on 2020-01-29 04:53

from django.db import migrations, models
import django.db.models.deletion
import django_multitenant.fields


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0020_auto_20200129_0404"),
    ]
    atomic = False
    operations = [
        migrations.AlterField(
            model_name="modelconfig",
            name="employee",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="configs",
                to="tests.Employee",
            ),
        )
    ]
