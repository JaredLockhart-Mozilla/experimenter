# Generated by Django 3.0.7 on 2020-09-25 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("experiments", "0117_auto_20200925_1533"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="nimbusexperiment",
            name="firefox_max_version",
        ),
    ]
