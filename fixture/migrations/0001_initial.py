# Generated by Django 2.0 on 2018-11-07 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Components',
            },
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('current_machine', models.CharField(max_length=100)),
                ('current_operation', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('INACTIVE', 'Inactive'), ('ACTIVE', 'Active')], max_length=10)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Machines',
            },
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('status', models.CharField(choices=[('INACTIVE', 'Inactive'), ('ACTIVE', 'Active')], max_length=10)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fixture.Machine')),
            ],
            options={
                'verbose_name_plural': 'Operations',
            },
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(choices=[('temprature', 'temprature'), ('pressure', 'pressure')], max_length=20)),
                ('value', models.IntegerField()),
                ('component', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fixture.Component')),
                ('machine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fixture.Machine')),
                ('operation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fixture.Operation')),
            ],
            options={
                'verbose_name_plural': 'Stats',
            },
        ),
        migrations.AddField(
            model_name='component',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fixture.Machine'),
        ),
        migrations.AddField(
            model_name='component',
            name='operation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fixture.Operation'),
        ),
    ]
