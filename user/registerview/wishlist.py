from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import JsonResponse


from user.models import Product, Cart, WishList


from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def funWishlist(request):
    wishlists=WishList.objects.filter(user=request.user)
    context={'wishlists':wishlists}
    return render(request,'wishlist.html',context)



def addToWishlist(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get("product_id"))
            product_check = Product.objects.get(id=prod_id)
            if product_check:
                if WishList.objects.filter(user=request.user, product_id=prod_id):
                    return JsonResponse({"status": "product already in wishlist"})
                else:
                   WishList.objects.create(user=request.user, product_id=prod_id)
                   return JsonResponse({"status": " Product added to wishlist"})
            else:
                return JsonResponse({"status": "No such Products found"})
        else:
            return JsonResponse({"status": "login to continue"})
    return redirect('/')    


def deletewishlistitem(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get("product_id"))

            if WishList.objects.filter(user=request.user, product_id=prod_id):
                wishlistitem = WishList.objects.filter(product_id=prod_id)
                wishlistitem.delete()
                return JsonResponse({"status": "product removed from wishlist"})
            else:

                return JsonResponse({"status": "product not found in wishlist"})
        else:
            return JsonResponse({"status": "login to continue"})

    return redirect("/")