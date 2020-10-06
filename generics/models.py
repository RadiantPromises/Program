from django.db import models

class Cost(models.Model):
  overall = models.IntegerField()
  current = models.IntegerField()
  needed = models.IntegerField()
  used = models.IntegerField()
  leftover = models.IntegerField()
  projected = models.IntegerField()

class Coordinates(models.Model):
  longitude=models.DecimalField(max_digits=11,decimal_places=8)
  latitude=models.DecimalField(max_digits=11,decimal_places=8)
  elevation = models.IntegerField()

class Address (models.Model):
  line_1= models.CharField(max_length=255)
  line_2= models.CharField(max_length=255)
  city= models.CharField(max_length=255)
  state= models.CharField(max_length=255)
  postal_code= models.CharField(max_length=255)
  countyr= models.CharField(max_length=255)



# Store in Session
# class CartItem(models.Model):
#   name = models.CharField(max_length=255)
#   name = models.CharField(max_length=255)
#   quantity = models.IntegerField()
#   price = models.OneToOneField(Cost,on_delete=models.CASCADE)