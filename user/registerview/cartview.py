from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import JsonResponse


from user.models import Product, Cart


from django.contrib.auth.decorators import login_required

def funcart(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get("product_id"))
            product_check = Product.objects.get(id=prod_id)
            if product_check:
                if Cart.objects.filter(user=request.user.id, product_id=prod_id):
                    return JsonResponse({"status": "Product already cart"})
                else:
                    prod_qty = int(request.POST.get("product_qty"))
                    print("work1nmll;")
                    if product_check.quantity >= prod_qty:
                        Cart.objects.create(
                            user=request.user, product_id=prod_id, product_qty=prod_qty
                        )
                        return JsonResponse({"status": "Product added successfully"})
                    else:
                        return JsonResponse(
                            {
                                "status": "Only"
                                + str(product_check.quantity)
                                + "Quantity available"
                            }
                        )
            else:
                return JsonResponse({"status": "no such product found"})
        else:
            return JsonResponse({"status": "login to continue"})
    print("work10")
    return redirect("/")

@login_required(login_url='login')
def cartpage(request):
    cart=Cart.objects.filter(user=request.user)
    context={'cart':cart}
    return render(request,'cart.html',context)

def updateCart(request):
    if request.method == "POST":
        prod_id = int(request.POST.get("product_id"))
        if Cart.objects.filter(user=request.user, product_id=prod_id):
            prod_qty = int(request.POST.get("product_qty"))
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({"status": "Update Successfully"})
    return redirect("/")


def deletecartitem(request):
    if request.method=="POST":
        prod_id = int(request.POST.get("product_id"))
        if Cart.objects.filter(user=request.user, product_id=prod_id):
            cart_item=Cart.objects.get(product_id=prod_id,user=request.user)
            cart_item.delete()
        return JsonResponse({"status": "Item Removed"})
    return redirect("/")