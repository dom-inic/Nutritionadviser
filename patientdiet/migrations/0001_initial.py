# Generated by Django 3.0.3 on 2020-04-29 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_no', models.IntegerField(max_length=8)),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('age', models.IntegerField(max_length=3)),
                ('place_of_residency', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('patient_number', models.IntegerField()),
                ('date_of_visit', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('I', 'Intersex')], max_length=1)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
