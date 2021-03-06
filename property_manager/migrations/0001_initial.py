# Generated by Django 3.0.8 on 2020-08-11 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property', models.CharField(blank=True, max_length=50, null=True)),
                ('client', models.CharField(blank=True, max_length=50, null=True)),
                ('client_account', models.CharField(blank=True, max_length=50, null=True)),
                ('client_name', models.CharField(blank=True, max_length=50, null=True)),
                ('client_email', models.EmailField(max_length=254)),
                ('client_address', models.CharField(blank=True, max_length=50)),
                ('client_contact', models.CharField(blank=True, max_length=50, null=True)),
                ('units', models.IntegerField(blank=True, default='0', null=True)),
                ('units_deposited', models.IntegerField(blank=True, default='0', null=True)),
                ('deposit_authorised_by', models.CharField(blank=True, max_length=50, null=True)),
                ('units_withdrawn', models.IntegerField(blank=True, default='0', null=True)),
                ('withdrawal_authorised_by', models.CharField(blank=True, max_length=50, null=True)),
                ('transfer_to', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('creation_date', models.DateTimeField(blank=True, max_length=50, null=True)),
                ('trust_deed_number', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50, unique=True)),
                ('nominal_value_per_unit', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('total_units', models.IntegerField(default=0)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Manager',
            },
        ),
        migrations.CreateModel(
            name='RegisterHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property', models.CharField(blank=True, max_length=50, null=True)),
                ('client', models.CharField(blank=True, max_length=50, null=True)),
                ('client_account', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('client_name', models.CharField(blank=True, max_length=50, null=True)),
                ('client_email', models.EmailField(max_length=254, null=True)),
                ('client_address', models.CharField(blank=True, max_length=50, null=True)),
                ('client_contact', models.CharField(blank=True, max_length=50, null=True)),
                ('units', models.IntegerField(blank=True, default='0', null=True)),
                ('units_deposited', models.IntegerField(blank=True, default='0', null=True)),
                ('deposit_authorised_by', models.CharField(blank=True, max_length=50, null=True)),
                ('units_withdrawn', models.IntegerField(blank=True, default='0', null=True)),
                ('withdrawal_authorised_by', models.CharField(blank=True, max_length=50, null=True)),
                ('transfer_to', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('creation_date', models.DateTimeField(blank=True, max_length=50, null=True)),
                ('trust_deed_number', models.CharField(max_length=50, null=True)),
                ('location', models.CharField(max_length=50, null=True)),
                ('nominal_value_per_unit', models.DecimalField(decimal_places=2, default=0, max_digits=12, null=True)),
                ('total_units', models.IntegerField(default=0)),
                ('last_updated', models.DateTimeField(null=True)),
                ('timestamp', models.DateTimeField(null=True)),
            ],
        ),
    ]
