# Generated by Django 3.0.3 on 2020-04-29 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientdiet', '0003_auto_20200429_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='health_details',
            name='name',
            field=models.CharField(default=12, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='health_details',
            name='patient_number',
            field=models.IntegerField(),
        ),
    ]
