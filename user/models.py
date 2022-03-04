from email.policy import default
from itertools import product
from unicodedata import category
from django.db import models
import datetime
import os
from django.contrib.auth.models import User

# Create your models here.

def get_file_path(request,filename):
    orginal_filename= filename
    nowtime=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename="%s%s"%(nowtime,orginal_filename)
    return os.path.join('uploads/',filename)

class Category(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    item=models.CharField(max_length=100,null=False,blank=True)
    image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    
    
    
    def __str__(self) :
        return self.name
    
    
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    product_image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    product_image_2=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    product_image_3=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    product_image_4=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    small_description=models.CharField(max_length=200,null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    price=models.FloatField(null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    tag=models.CharField(max_length=150,null=False,blank=False)
    meta_title=models.CharField(max_length=150,null=False,blank=False)
    meta_keyword=models.CharField(max_length=150,null=False,blank=False)
    meta_description=models.TextField(max_length=550,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
       
    def __str__(self) :
        return self.name
    

# class images(models.Model):
#     product=models.ForeignKey(Product,on_delete=models.CASCADE)
#     title=models.CharField(max_length=30,blank=True)
#     product_image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
  
    
    
