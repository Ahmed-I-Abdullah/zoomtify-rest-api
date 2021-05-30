# Generated by Django 3.2.3 on 2021-05-29 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_alter_meeting_notified_contacts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='notified_contacts',
        ),
        migrations.AddField(
            model_name='meeting',
            name='notified_contacts',
            field=models.ManyToManyField(null=True, related_name='notification_meetings', to='meetings.Contact'),
        ),
    ]