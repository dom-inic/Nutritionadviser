from django.db import models


class Personal_details(models.Model):
    genders = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('I', 'Intersex'),
    )
    counties = (


        ('Mombasa','Mombasa'),
        ('Kwale','Kwale'),
        ('Kilifi','Kilifi'),
        ('Tana River','Tana River'),
        ('Lamu','Lamu'),
        ('Taita-Taveta', 'Taita-Taveta'),
        ('Garissa','Garissa'),
        ('Wajir','Wajir'),
        ('Mandera','Mandera'),
        ('Marsabit', 'Marsabit'),
        ('Isiolo', 'Isiolo'),
        ('Meru', 'Meru'),
        ('Tharaka-Nithi', 'Tharaka-Nithi'),
        ('Embu', 'Embu'),
        ('Kitui','Kitui'),
        ('Machakos', 'Machakos'),
        ('Makueni', 'Makueni'),
        ('Nyandarua', 'Nyandarua'),
        ('Nyeri', 'Nyeri'),
        ('Kirinyaga', 'Kirinyaga'),
        ('Murang', 'Murang'),
        ('Kiambu', 'Kiambu'),
        ('Turkana', 'Turkana'),
        ('West Pokot', 'West Pokot'),
        ('Samburu', 'Samburu'),
        ('Trans Nzoia','Trans Nzoia'),
        ('Uasin Gishu', 'Uasin Gishu'),
        ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'),
        ('Nandi','Nandi'),
        ('Baringo', 'Baringo'),
        ('Laikipia', 'Laikipia'),
        ('Nakuru', 'Nakuru'),
        ('Narok', 'Narok'),
        ('Kajiado', 'Kajiado'),
        ('Kericho', 'Kericho'),
        ('Bomet', 'Bomet'),
        ('Kakamega','Kakamega'),
        ('Vihiga', 'Vihiga'),
        ('Bungoma', 'Bungoma'),
        ('Busia', 'Busia'),
        ('Siaya', 'Siaya'),
        ('Kisumu', 'Kisumu'),
        ('Homa Bay','Homa Bay'),
        ('Migori', 'Migori'),
        ('Kisii', 'Kisii'),
        ('Nyamira', 'Nyamira'),
        ('Nairobi', 'Nairobi'),
    )

    
    name = models.CharField(max_length=50, primary_key=True)
    id_no = models.IntegerField()
    dob = models.DateField()
    age = models.IntegerField()
    place_of_residency = models.CharField(max_length=30)
    contact = models.IntegerField()
    patient_number = models.IntegerField()
    date_of_visit = models.DateField()
    gender = models.CharField(max_length=1, choices=genders)
    email = models.EmailField()
    county = models.CharField(max_length=30, choices=counties, default='nyamira')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Patients details'

class Health_details(models.Model):
    conditions = (
        ('DA','Diabetes 1'),
        ('DB','Diabetes 2'),
        ('HA','Hiv/Aids'),
        ('A','Anaemia'),
        ('D','dyxlexia'),
        ('PE','pulomanary embolism'),
        ('covid', 'corona virus'),
    )
    diseases = (
        ('DA','Diabetes 1'),
        ('DB','Diabetes 2'),
        ('HA','Hiv/Aids'),
        ('A','Anaemia'),
        ('D','dyxlexia'),
        ('PE','pulomanary embolism'),
        ('covid', 'corona virus'),
    )
    clinicians = (
        ('doc', 'Doctor'),
        ('nutritionist', 'nutritionist'),
        ('mkunga', 'Nurse'),
        ('others', 'others'),
    )
    names = models.ForeignKey(Personal_details, on_delete=models.CASCADE,default='mutahi kagwe')
    patient_number = models.IntegerField()
    previously_diagnised_disease = models.CharField(max_length=30)
    currently_diagonised_disease = models.CharField(max_length=30)
    year_diagonised = models.DateField()
    allergies = models.BooleanField(default=True)
    weight = models.DecimalField(decimal_places=2, max_digits=4)
    height = models.DecimalField(decimal_places=2, max_digits=4)
    bmi = models.DecimalField(decimal_places=2, max_digits=4)
    muac = models.IntegerField()
    on_arvs = models.BooleanField()
    cd4_count = models.IntegerField()
    tca = models.IntegerField()
    clinician_designation = models.CharField(max_length=50, default='doctor')
    diet = models.CharField(max_length=50, default='proteins')
    condition = models.CharField(max_length=30, choices=conditions, default='tuberculosis')
    disease = models.CharField(max_length=30, choices=diseases, default='tuberculosis')
    medicine_prescribed = models.CharField(max_length=50, default='hydrochloroquin')
    clinician = models.CharField(max_length=30, choices=clinicians, default='doctor')

    class Meta:
        verbose_name_plural = 'Health Details'

    def __str__(self):
        return self.names


    



    


    



    


