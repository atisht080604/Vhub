# Generated by Django 5.1.6 on 2025-03-07 10:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vapp', '0014_alter_registration_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='Vapp.event'),
        ),
    ]
