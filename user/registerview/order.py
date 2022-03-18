
from django.shortcuts import redirect, render
from django.contrib import messages

from django.http import HttpResponse, JsonResponse
from user.models import Product, Cart, WishList,Profile, Order, OrderItem


from django.contrib.auth.decorators import login_required


def myorder(request):
    
    order=Order.objects.filter(user=request.user)
    context={'order':order}
    return render(request,'order.html',context)
    
    
    
def vieworder(request,t_no):
    order=Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitems=OrderItem.objects.filter(order=order)
    context={'order':order,'orderitems':orderitems}
    return render(request,'orderview.html',context)    