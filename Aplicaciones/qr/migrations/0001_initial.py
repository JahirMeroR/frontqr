# Generated by Django 4.1.6 on 2023-02-20 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('custom_id', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=35)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=35)),
                ('role', models.CharField(max_length=35)),
                ('sex', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1)),
                ('age', models.PositiveSmallIntegerField()),
                ('country', models.CharField(max_length=35)),
                ('city', models.CharField(max_length=35)),
                ('address', models.CharField(max_length=35)),
                ('phone', models.CharField(max_length=10)),
                ('code_qr', models.CharField(max_length=35)),
            ],
        ),
    ]