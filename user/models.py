
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
    # shirt_size=(
    #     ('S','Small'),
    #     ('M','Medium'),
    #     ('L','Large'),
    #     ('XL','Xtra Large'),
    #     ('XXL','Double Xtra Large'),
    # )
    # size=models.CharField(max_length=6,choices=shirt_size,null=True)
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
    
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
class WishList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fname=models.CharField(max_length=150, null=False)
    lname=models.CharField(max_length=150, null=False)
    email=models.CharField(max_length=150, null=False)
    phone=models.CharField(max_length=150, null=False)
    address=models.TextField(null=False)
    city=models.CharField(max_length=150, null=False)
    state=models.CharField(max_length=150, null=False)
    country=models.CharField(max_length=150, null=False)
    pincode=models.CharField(max_length=50, null=False)
    total_price=models.FloatField(null=False)
    payment_mode=models.CharField(max_length=150,null=False)
    payment_id=models.CharField(max_length=150,null=True)
    orderstatuses=(
        ('pending','pending'),
        ('Out For Shipping','Out For Shipping'),
        ('Completed','Completed')
    )
    status=models.CharField(max_length=150,choices=orderstatuses,default='pending')
    message=models.TextField(null=True)
    tracking_no=models.CharField(max_length=150,null=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{}-{}'.format(self.id,self.tracking_no)     
    
    

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.FloatField(null=False)
    quantity=models.IntegerField(null=False)
    
    def __srt__(self):
        return '{} {}'.format(self.order.id,self.order.tracking_no)    

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=120,null=False)
    address=models.TextField(null=False)
    city=models.CharField(max_length=150, null=False)
    state=models.CharField(max_length=150, null=False)
    country=models.CharField(max_length=150, null=False)
    pincode=models.CharField(max_length=50, null=False)
    created_at=models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username