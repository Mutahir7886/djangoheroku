# Generated by Django 3.1 on 2020-10-26 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0010_auto_20200426_1651'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='bio_data',
            name='name_email',
        ),
    ]
