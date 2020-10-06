from django.db import models
from django.forms import ModelForm
from generics.models import Address

class Donor(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email_address = models.CharField(max_length=50)
  address = models.ManyToManyField(Address)
  description= models.CharField(max_length=255)
  phone_number = models.CharField(max_length=15)
  birthday = models.DateTimeField()
  password = models.CharField(max_length = 255)

class DonorForm(ModelForm):
  class Meta:
    model = Donor
    fields = ['first_name', 'last_name','email_address','address']