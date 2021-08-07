from django.db import models
from django.contrib.auth.models import User


class GroceryItem(models.Model):
    
     item_owner = models.ForeignKey(User,on_delete=models.CASCADE)
     item_name = models.CharField(max_length=100)
     item_qty = models.CharField(max_length=50)
     item_status = models.CharField(max_length=50)
     item_date = models.CharField(max_length=100)


     def __str__(self):
          return f"{self.item_owner.first_name} {self.item_name}"