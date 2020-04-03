from django.db import models

# Create your models here.
class allos(models.Model):
    item1 = models.CharField(max_length=100,null=True)
    item2 = models.CharField(max_length=100,null=True,blank=True)
    item3 = models.CharField(max_length=100,null=True,blank=True)
    item4 = models.CharField(max_length=100,null=True,blank=True)

class ayurs(models.Model):
    item1 = models.CharField(max_length=100,null=True)
    item2 = models.CharField(max_length=100,null=True,blank=True)
    item3 = models.CharField(max_length=100,null=True,blank=True)
    item4 = models.CharField(max_length=100,null=True,blank=True)

class disps(models.Model):
    item1 = models.CharField(max_length=100,null=True)
    item2 = models.CharField(max_length=100,null=True,blank=True)
    item3 = models.CharField(max_length=100,null=True,blank=True)
    item4 = models.CharField(max_length=100,null=True,blank=True)

class neuts(models.Model):
    item1 = models.CharField(max_length=100,null=True)
    item2 = models.CharField(max_length=100,null=True,blank=True)
    item3 = models.CharField(max_length=100,null=True,blank=True)
    item4 = models.CharField(max_length=100,null=True,blank=True)

class pharms(models.Model):
    item1 = models.CharField(max_length=100,null=True)
    item2 = models.CharField(max_length=100,null=True,blank=True)
    item3 = models.CharField(max_length=100,null=True,blank=True)
    item4 = models.CharField(max_length=100,null=True,blank=True)

class respis(models.Model):
    item1 = models.CharField(max_length=100,null=True)
    item2 = models.CharField(max_length=100,null=True,blank=True)
    item3 = models.CharField(max_length=100,null=True,blank=True)
    item4 = models.CharField(max_length=100,null=True,blank=True)

class surgis(models.Model):
    item1 = models.CharField(max_length=100,null=True)
    item2 = models.CharField(max_length=100,null=True,blank=True)
    item3 = models.CharField(max_length=100,null=True,blank=True)
    item4 = models.CharField(max_length=100,null=True,blank=True)

    