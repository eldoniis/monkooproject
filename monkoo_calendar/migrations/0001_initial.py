# Generated by Django 4.0.2 on 2022-05-05 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('start', models.CharField(blank=True, max_length=255, null=True)),
                ('end', models.CharField(blank=True, max_length=255, null=True)),
                ('backgroundColor', models.CharField(max_length=255)),
                ('borderColor', models.CharField(max_length=255)),
            ],
        ),
    ]