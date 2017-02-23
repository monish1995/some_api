from __future__ import unicode_literals

from django.db import models
import django
from django.conf import settings
from django.db import models


#for signup 
# class User(models.Model):
#     name = models.CharField(max_length=30,primary_key=True,blank=False)
#     username = models.CharField(max_length=30,blank=False)
#     email = models.EmailField(max_length=70,blank=False)
#     password = models.CharField(max_length=30,blank=False)
    


#user info
class User_info(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birth_date = models.DateField()
    legal_id = models.CharField(max_length=300) #driving license,any id
    resource = models.CharField(max_length=300)
    contact = models.CharField(max_length=20,blank=False)


class Cars(models.Model):
    plate_no = models.CharField(max_length=30)
    model_name = models.CharField(max_length=300)

class Parking_lot(models.Model):
    place_name = models.CharField(max_length=300)
    lot_id = models.CharField(max_length=30)
    lot_address = models.CharField(max_length=300)


class Transaction_info(models.Model):
	username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	plot_id = models.CharField(max_length=30)
	plate_no = models.CharField(max_length=30)
	check_in_time = models.TimeField()
	check_out_time = models.TimeField()
	amount = models.IntegerField()
	flag = models.CharField(max_length=2) # Booked = B , Checked in = CI , Checked out = CO