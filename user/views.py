from multiprocessing import context
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import *
from user.form import CustomUserForm
# Create your views here.


def fun_master(request):
    
    return render (request,'master.html',)

def funHome(request):
    treanding_pro=Product.objects.filter(trending=1)
    context={'treanding_pro':treanding_pro}
    
    return render(request,'home.html',context)

def funAbout(request):
    return render(request,'about.html')

def funShop(request):
    allpro=Product.objects.filter(status=0)
    context={'allpro':allpro}
    return render(request,'shop.html',context)




def funBlog(request):
    return render (request,'blog.html')


def collection(request):
    category=Category.objects.filter(status=0)
    context=({'category':category})
    return render(request,'collection.html',context)


def CollectionViews(request,slug):
    if(Category.objects.filter(slug=slug,status=0)):
        products=Product.objects.filter(category__slug=slug)
        category=Category.objects.filter(slug=slug).first()
        context=({'products':products,'category':category})
        return render(request,'product.html',context)
    else:
        messages.warning(request,"No Such Categoru found")
        return redirect('collection')
    
    
def productview(request,cate_slug,prod_slug):
    if(Category.objects.filter(slug=cate_slug,status=0)):
        if(Product.objects.filter(slug=prod_slug,status=0)):
            products=Product.objects.filter(slug=prod_slug,status=0).first()
            context={'products':products}
        else:
            messages.error(request,"No Such product Found")
            return redirect('collections')
    else:
        messages.error(request,"No such category Found")
        return redirect('collections')
    return render(request,'viewprduct.html',context)

        
