# Generated by Django 4.2.7 on 2023-12-28 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0003_keyseed_p_activated'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='p_timer',
            field=models.PositiveIntegerField(default=3600),
            preserve_default=False,
        ),
    ]
