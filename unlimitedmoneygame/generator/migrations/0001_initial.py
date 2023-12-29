# Generated by Django 4.2.7 on 2023-12-26 17:03

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('stripe_customer_id', models.CharField(blank=True, max_length=255, null=True)),
                ('username', models.CharField(max_length=16, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('p_money', models.FloatField(null=True)),
                ('p_storedluck', models.FloatField(null=True)),
                ('p_luck', models.FloatField(null=True)),
                ('p_level', models.PositiveIntegerField(null=True)),
                ('p_orders', models.PositiveIntegerField(null=True)),
                ('p_exp', models.PositiveIntegerField(null=True)),
                ('p_trades', models.BooleanField(null=True)),
                ('P_tmoney', models.BooleanField(null=True)),
                ('p_playing', models.BooleanField(null=True)),
                ('p_forceluck', models.DecimalField(decimal_places=3, max_digits=3, null=True)),
                ('p_acceptfriends', models.BooleanField(null=True)),
                ('p_messagesaccept', models.BooleanField(null=True)),
                ('p_currentrade', models.CharField(max_length=32)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='black',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=16)),
                ('p_level', models.PositiveIntegerField()),
                ('p_content', models.CharField(max_length=90)),
                ('p_restricted', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seasontime', models.PositiveIntegerField()),
                ('seasonseed', models.PositiveIntegerField()),
                ('roundtime', models.PositiveIntegerField()),
                ('roundseed', models.PositiveIntegerField()),
                ('roundcounter', models.PositiveIntegerField()),
                ('seshcount', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='glitch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_rarity', models.CharField(max_length=16)),
                ('s_name', models.CharField(max_length=16)),
                ('s_status', models.CharField(max_length=16)),
                ('s_durability', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(500)])),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=16)),
                ('s_rarity', models.CharField(max_length=16)),
                ('s_cooldown', models.PositiveIntegerField()),
                ('s_name', models.CharField(max_length=16)),
                ('s_status', models.CharField(max_length=16)),
                ('s_durability', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(500)])),
            ],
        ),
        migrations.CreateModel(
            name='KeySeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_namer', models.CharField(max_length=16)),
                ('p_keyseed', models.CharField(max_length=32)),
                ('p_amounted', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correspondinglevel', models.PositiveIntegerField()),
                ('correspondingexp', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Luck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LuckCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('downtwenty', models.DecimalField(decimal_places=3, max_digits=3)),
                ('downforty', models.DecimalField(decimal_places=3, max_digits=3)),
                ('downeighty', models.DecimalField(decimal_places=3, max_digits=3)),
                ('downsixteen', models.DecimalField(decimal_places=3, max_digits=3)),
                ('downthirtytwo', models.DecimalField(decimal_places=3, max_digits=3)),
                ('downthirtythree', models.DecimalField(decimal_places=3, max_digits=3)),
                ('pid', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=16)),
                ('price', models.PositiveIntegerField()),
                ('itemname', models.CharField(max_length=16)),
                ('itemstatus', models.CharField(max_length=16)),
                ('itemrarity', models.CharField(max_length=16)),
                ('itemdurability', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(500)])),
                ('itemid', models.PositiveIntegerField()),
                ('imgurl', models.CharField(max_length=72)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=16)),
                ('sp_name', models.CharField(max_length=16)),
                ('Msgkey', models.CharField(max_length=32)),
                ('keyMsg', models.CharField(max_length=32)),
                ('Msgcontent', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Modifiers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baseluck', models.DecimalField(decimal_places=2, max_digits=2)),
                ('takemoney', models.PositiveIntegerField()),
                ('baseforceluck', models.DecimalField(decimal_places=3, max_digits=3)),
                ('sores', models.PositiveIntegerField()),
                ('umgtax', models.FloatField()),
                ('winnersplit', models.DecimalField(decimal_places=2, max_digits=2)),
                ('soresplit', models.DecimalField(decimal_places=2, max_digits=2)),
                ('seasoncounter', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_umg_order', models.PositiveIntegerField()),
                ('s_won_order', models.PositiveIntegerField()),
                ('s_sores_order', models.PositiveIntegerField()),
                ('s_total_sores', models.PositiveIntegerField()),
                ('s_total_umg', models.FloatField()),
                ('s_total_won', models.PositiveIntegerField()),
                ('s_winners', models.CharField(max_length=9999)),
                ('s_losers', models.CharField(max_length=9999)),
            ],
        ),
        migrations.CreateModel(
            name='Playing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=16)),
                ('p_id', models.PositiveIntegerField()),
                ('p_money', models.FloatField()),
                ('p_storedluck', models.FloatField()),
                ('p_luck', models.FloatField()),
                ('p_level', models.PositiveIntegerField()),
                ('p_orders', models.PositiveIntegerField()),
                ('p_exp', models.PositiveIntegerField()),
                ('p_trades', models.BooleanField()),
                ('P_tmoney', models.BooleanField()),
                ('p_playing', models.BooleanField()),
                ('p_forceluck', models.DecimalField(decimal_places=3, max_digits=3)),
                ('p_inventory', models.JSONField()),
                ('p_slot', models.JSONField()),
                ('p_friends', models.JSONField()),
                ('p_acceptfriends', models.BooleanField()),
                ('p_messages', models.JSONField()),
                ('p_messagesaccept', models.BooleanField()),
                ('p_banned', models.JSONField()),
                ('p_currentrade', models.CharField(max_length=32)),
            ],
            options={
                'ordering': ('p_name',),
            },
        ),
        migrations.CreateModel(
            name='PlayingMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_playing', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_rarity', models.CharField(max_length=16)),
                ('p_name', models.CharField(max_length=16)),
                ('s_cooldown', models.PositiveIntegerField()),
                ('s_name', models.CharField(max_length=16)),
                ('s_status', models.CharField(max_length=16)),
                ('s_durability', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(500)])),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_gmoney', models.BooleanField()),
                ('p_name', models.CharField(max_length=16)),
                ('p_amount', models.FloatField()),
                ('p_class', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=16)),
                ('p_active', models.BooleanField()),
                ('fp_accepted', models.BooleanField()),
                ('secp_name', models.CharField(max_length=16)),
                ('secactive', models.PositiveIntegerField()),
                ('secp_accepted', models.BooleanField()),
                ('middlestack', models.JSONField()),
                ('fpstack', models.JSONField()),
                ('spstack', models.JSONField()),
                ('Key', models.CharField(max_length=27)),
                ('BackupKey', models.CharField(max_length=27)),
                ('accepted', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TradeSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_rarity', models.CharField(max_length=16)),
                ('p_name', models.CharField(max_length=16)),
                ('s_cooldown', models.PositiveIntegerField()),
                ('s_name', models.CharField(max_length=16)),
                ('s_status', models.CharField(max_length=16)),
                ('s_durability', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(500)])),
                ('SeedKey', models.CharField(max_length=32)),
                ('BackupKey', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='PayingUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_bool', models.BooleanField(default=False)),
                ('stripe_checkout_id', models.CharField(max_length=500)),
                ('app_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]