# Generated by Django 4.2.7 on 2023-12-29 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0006_deletedinvoice_p_qrcode_invoice_p_qrcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='APIKEY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KEY', models.CharField(max_length=255)),
            ],
        ),
    ]
