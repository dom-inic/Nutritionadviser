# Generated by Django 3.0.3 on 2020-04-29 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientdiet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_details',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='personal_details',
            name='id_no',
            field=models.IntegerField(),
        ),
    ]
