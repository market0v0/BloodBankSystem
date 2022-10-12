# Generated by Django 4.1.1 on 2022-10-12 08:20

import accounts.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodSupply',
            fields=[
                ('supply_id', models.AutoField(primary_key=True, serialize=False)),
                ('aplus_amount', models.IntegerField(default=0, verbose_name='A+ amount')),
                ('amin_amount', models.IntegerField(default=0, verbose_name='A- amount')),
                ('bplus_amount', models.IntegerField(default=0, verbose_name='B+ amount')),
                ('bmin_amount', models.IntegerField(default=0, verbose_name='B- amount')),
                ('abplus_amount', models.IntegerField(default=0, verbose_name='AB+ amount')),
                ('abmin_amount', models.IntegerField(default=0, verbose_name='AB- amount')),
                ('oplus_amount', models.IntegerField(default=0, verbose_name='O+ amount')),
                ('omin_amount', models.IntegerField(default=0, verbose_name='O- amount')),
            ],
            options={
                'verbose_name_plural': 'Blood Supplies',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('user_image', models.ImageField(default='default.svg', upload_to=accounts.models.image_path)),
                ('type', models.CharField(choices=[('I', 'Individual'), ('O', 'Organization')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.user')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('weight', models.FloatField(verbose_name='Weight (kg)')),
                ('contact_number', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(regex='^(09|\\+639)\\d{9}$')])),
                ('health_condition', models.TextField(blank=True, max_length=50, null=True, verbose_name='Health conditions (optional)')),
                ('blood_type', models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')], max_length=3)),
                ('individual_type', models.CharField(choices=[('D', 'Donor'), ('R', 'Recipient')], max_length=1)),
            ],
            bases=('accounts.user',),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.user')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(regex='^(09|\\+639)\\d{9}$')])),
                ('org_type', models.CharField(choices=[('H', 'Hospital'), ('B', 'Blood Bank')], max_length=1)),
                ('blood_supply', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.bloodsupply')),
            ],
            bases=('accounts.user',),
        ),
        migrations.CreateModel(
            name='BloodBank',
            fields=[
                ('organization_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.organization')),
            ],
            options={
                'verbose_name_plural': 'Blood Banks',
            },
            bases=('accounts.organization',),
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('individual_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.individual')),
            ],
            bases=('accounts.individual',),
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('organization_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.organization')),
            ],
            bases=('accounts.organization',),
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('individual_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.individual')),
            ],
            bases=('accounts.individual',),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('request_date', models.DateField()),
                ('blood_type', models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')], max_length=3)),
                ('quantity', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Declined', 'Declined')], max_length=10)),
                ('blood_bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.bloodbank')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Transfusion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfusion_date', models.DateField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Declined', 'Declined')], max_length=10)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.hospital')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.recipient')),
            ],
            options={
                'unique_together': {('recipient', 'transfusion_date')},
            },
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_date', models.DateField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Declined', 'Declined')], max_length=10)),
                ('blood_bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.bloodbank')),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.donor')),
            ],
            options={
                'unique_together': {('donor', 'donation_date')},
            },
        ),
    ]
