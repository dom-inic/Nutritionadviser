# Generated by Django 3.0.2 on 2020-05-04 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientdiet', '0005_clinician_designation_coexisting_condition_count_of_residency_currently_diagonised_disease_prescribe'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Clinician_designation',
        ),
        migrations.DeleteModel(
            name='Coexisting_condition',
        ),
        migrations.DeleteModel(
            name='Count_of_residency',
        ),
        migrations.DeleteModel(
            name='Currently_diagonised_disease',
        ),
        migrations.DeleteModel(
            name='Prescribed_diet',
        ),
        migrations.DeleteModel(
            name='Prescription',
        ),
        migrations.RemoveField(
            model_name='personal_details',
            name='id',
        ),
        migrations.AddField(
            model_name='health_details',
            name='allergies',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='health_details',
            name='clinician',
            field=models.CharField(choices=[('doc', 'Doctor'), ('nutritionist', 'nutritionist'), ('mkunga', 'Nurse'), ('others', 'others')], default='doctor', max_length=30),
        ),
        migrations.AddField(
            model_name='health_details',
            name='condition',
            field=models.CharField(choices=[('DA', 'Diabetes 1'), ('DB', 'Diabetes 2'), ('HA', 'Hiv/Aids'), ('A', 'Anaemia'), ('D', 'dyxlexia'), ('PE', 'pulomanary embolism')], default='tuberculosis', max_length=30),
        ),
        migrations.AddField(
            model_name='health_details',
            name='diet',
            field=models.CharField(default='proteins', max_length=50),
        ),
        migrations.AddField(
            model_name='health_details',
            name='disease',
            field=models.CharField(choices=[('DA', 'Diabetes 1'), ('DB', 'Diabetes 2'), ('HA', 'Hiv/Aids'), ('A', 'Anaemia'), ('D', 'dyxlexia'), ('PE', 'pulomanary embolism')], default='tuberculosis', max_length=30),
        ),
        migrations.AddField(
            model_name='health_details',
            name='medicine_prescribed',
            field=models.CharField(default='hydrochloroquin', max_length=50),
        ),
        migrations.AddField(
            model_name='personal_details',
            name='county',
            field=models.CharField(choices=[('Mombasa', 'Mombasa'), ('Kwale', 'Kwale'), ('Kilifi', 'Kilifi'), ('Tana River', 'Tana River'), ('Lamu', 'Lamu'), ('Taita-Taveta', 'Taita-Taveta'), ('Garissa', 'Garissa'), ('Wajir', 'Wajir'), ('Mandera', 'Mandera'), ('Marsabit', 'Marsabit'), ('Isiolo', 'Isiolo'), ('Meru', 'Meru'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Embu', 'Embu'), ('Kitui', 'Kitui'), ('Machakos', 'Machakos'), ('Makueni', 'Makueni'), ('Nyandarua', 'Nyandarua'), ('Nyeri', 'Nyeri'), ('Kirinyaga', 'Kirinyaga'), ('Murang', 'Murang'), ('Kiambu', 'Kiambu'), ('Turkana', 'Turkana'), ('West Pokot', 'West Pokot'), ('Samburu', 'Samburu'), ('Trans Nzoia', 'Trans Nzoia'), ('Uasin Gishu', 'Uasin Gishu'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Nandi', 'Nandi'), ('Baringo', 'Baringo'), ('Laikipia', 'Laikipia'), ('Nakuru', 'Nakuru'), ('Narok', 'Narok'), ('Kajiado', 'Kajiado'), ('Kericho', 'Kericho'), ('Bomet', 'Bomet'), ('Kakamega', 'Kakamega'), ('Vihiga', 'Vihiga'), ('Bungoma', 'Bungoma'), ('Busia', 'Busia'), ('Siaya', 'Siaya'), ('Kisumu', 'Kisumu'), ('Homa Bay', 'Homa Bay'), ('Migori', 'Migori'), ('Kisii', 'Kisii'), ('Nyamira', 'Nyamira'), ('Nairobi', 'Nairobi')], default='nyamira', max_length=30),
        ),
        migrations.AlterField(
            model_name='health_details',
            name='clinician_designation',
            field=models.CharField(default='doctor', max_length=50),
        ),
        migrations.AlterField(
            model_name='personal_details',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
