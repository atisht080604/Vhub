# Generated by Django 5.1.6 on 2025-03-11 17:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vapp', '0023_eventcertificate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventcertificate',
            old_name='certificate_id',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='eventcertificate',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='eventcertificate',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vapp.event'),
        ),
        migrations.AlterField(
            model_name='eventcertificate',
            name='file',
            field=models.FileField(default='certificates/default_certificate.pdf', upload_to='certificates/'),
        ),
        migrations.AlterField(
            model_name='eventcertificate',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
