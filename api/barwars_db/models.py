from django.db import models

class User(models.Model):
  uuid = models.CharField(max_length=64, primary_key=True)
  profile_name = models.CharField(max_length=64)
  submit_count = models.IntegerField(default=0)
  solved_count = models.IntegerField(default=0)
  points = models.IntegerField(default=100)
  time_created = models.DateTimeField(auto_now_add = True)
  time_updated = models.DateTimeField(auto_now = True)

class Challenge(models.Model):
  cid = models.AutoField(primary_key=True)
  barcode = models.CharField(max_length=32)
  description = models.CharField(max_length=128)
  status = models.IntegerField()
  uuid = models.ForeignKey('User')
  time_created = models.DateTimeField(auto_now_add = True)
  time_updated = models.DateTimeField(auto_now = True)

  
