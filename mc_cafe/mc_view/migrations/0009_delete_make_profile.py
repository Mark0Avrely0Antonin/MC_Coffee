# Generated by Django 4.0.2 on 2022-02-26 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mc_view', '0008_rename_profile_make_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Make_Profile',
        ),
    ]
