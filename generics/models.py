from django.db import models

class Cost(models.Model):
  overall = models.IntegerField()
  current = models.IntegerField()
  needed = models.IntegerField()
  used = models.IntegerField()
  leftover = models.IntegerField()
  projected = models.IntegerField()

# Store in Session
# class CartItem(models.Model):
#   name = models.CharField(max_length=255)
#   name = models.CharField(max_length=255)
#   quantity = models.IntegerField()
#   price = models.OneToOneField(Cost,on_delete=models.CASCADE)