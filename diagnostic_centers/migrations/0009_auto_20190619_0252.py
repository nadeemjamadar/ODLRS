# Generated by Django 2.2.1 on 2019-06-18 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic_centers', '0008_auto_20190619_0227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diagnosticadmin',
            name='staff',
        ),
        migrations.AddField(
            model_name='diagnosticadmin',
            name='staff',
            field=models.ManyToManyField(to='diagnostic_centers.DiagnosticStaff'),
        ),
    ]
