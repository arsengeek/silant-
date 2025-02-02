# Generated by Django 5.1.5 on 2025-01-19 19:24

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FailureNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='RecoveryMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='ReferenceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('useRole', models.CharField(choices=[('guest', 'Guest'), ('menager', 'Menager'), ('client', 'Client'), ('serviceCompany', 'ServiceCompany')], default='guest', max_length=15)),
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
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factoryNumber', models.CharField(max_length=100)),
                ('factoryNumberEngine', models.CharField(max_length=100)),
                ('factoryNumberTransmission', models.CharField(max_length=100)),
                ('factoryNumberLeadingBridge', models.CharField(max_length=100)),
                ('factoryNumberManagedBridge', models.CharField(max_length=100)),
                ('factoryNumberSupplyContract', models.CharField(max_length=100)),
                ('dataShipment', models.DateField()),
                ('consumer', models.CharField(max_length=100)),
                ('adressExplotation', models.CharField(max_length=200)),
                ('complictation', models.TextField()),
                ('client', models.CharField(max_length=100)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='machines_as_model', to='silantapp.referencemodel')),
                ('modelEngine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='machines_as_modelEngine', to='silantapp.referencemodel')),
                ('modelLeadingBridge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='machines_as_modelLeadingBridge', to='silantapp.referencemodel')),
                ('modelManagedBridge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='machines_as_modelManagedBridge', to='silantapp.referencemodel')),
                ('modelTransmission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='machines_as_modelTransmission', to='silantapp.referencemodel')),
                ('serviceCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='machines', to='silantapp.servicecompany')),
            ],
        ),
        migrations.CreateModel(
            name='Reclamation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataReclamation', models.DateField()),
                ('development', models.IntegerField()),
                ('descriotionReject', models.TextField()),
                ('useSpareParts', models.TextField()),
                ('dataRecovery', models.DateField()),
                ('downtimeEquipment', models.IntegerField()),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reclamations', to='silantapp.machine')),
                ('rejectNode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reclamations', to='silantapp.failurenode')),
                ('recoveryMethod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reclamations', to='silantapp.recoverymethod')),
                ('serviceCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reclamations', to='silantapp.servicecompany')),
            ],
        ),
        migrations.CreateModel(
            name='TO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTO', models.DateField()),
                ('development', models.IntegerField()),
                ('orderNumber', models.CharField(max_length=100)),
                ('dataOrder', models.DateField()),
                ('organizationDoTO', models.CharField(max_length=100)),
                ('TypeTO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tos', to='silantapp.maintenancetype')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tos', to='silantapp.machine')),
                ('serviceCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tos', to='silantapp.servicecompany')),
            ],
        ),
    ]
