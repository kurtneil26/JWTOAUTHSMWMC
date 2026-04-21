from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class loan_types(models.Model):
    loantype_id = models.AutoField(primary_key=True)
    loantype_name = models.CharField(max_length=100)
    def __str__(self):
        return self.loantype_name

class users(models.Model):
    USERTYPE = (
        ('admin', 'Admin'),
        ('applicant', 'Applicant'),
    )
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    ACCOUNT_STATUS = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    FName = models.CharField(max_length=100)
    MName = models.CharField(max_length=100)
    LName = models.CharField(max_length=100)
    Phonenumber = models.CharField(max_length=15)
    Usertype = models.CharField(max_length=50, choices=USERTYPE)
    dateofbirth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER)
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    account_status = models.CharField(max_length=20, choices=ACCOUNT_STATUS)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    def __str__(self):
        return self.username

class loanapplication(models.Model):
    application_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    loantype_id = models.ForeignKey(loan_types, on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    application_date = models.DateField()
    status = models.CharField(max_length=20)
    approval_date = models.DateField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    released_date = models.DateField(null=True, blank=True)
    paid_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"Application ID: {self.application_id}"
    
class payment_schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    application_id = models.ForeignKey(loanapplication, on_delete=models.CASCADE)
    schedule_date = models.DateField()
    payment_status = models.CharField(max_length=20)
    def __str__(self):
        return f"Schedule ID: {self.schedule_id}"
    
class report(models.Model):
    report_id = models.AutoField(primary_key=True)
    generated_date = models.DateField()
    def __str__(self):
        return f"Report ID: {self.report_id}"
    
class loan_documents(models.Model):
    document_id = models.AutoField(primary_key=True)
    application_id = models.ForeignKey(loanapplication, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=255)
    file_path = models.FileField(upload_to='loan_documents/')
    def __str__(self):
        return self.document_type