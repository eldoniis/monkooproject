# Generated by Django 4.0.2 on 2022-05-18 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monkoo_calendar', '0002_rename_event_id_events_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='userId',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
