# Generated by Django 4.2.7 on 2023-12-28 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0002_invoice_keyseed_p_timer'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyseed',
            name='p_activated',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
