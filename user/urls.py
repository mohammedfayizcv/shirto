
from django.contrib import admin
from django.urls import include, path
from .import views

from user.registerview import authview,cartview,wishlist,checkout,order


urlpatterns = [
  path('master',views.fun_master,name='master'),
  path('',views.funHome,name='home'),
  path('about/',views.funAbout,name='about'),
  
  path('shop/',views.funShop,name='shop'),

  path('blog/',views.funBlog,name='blog'),
  
  path('collection',views.collection,name='collection'),
  
  path('collections/<str:slug>',views.CollectionViews,name='collections'),
  
   path('collection/<str:cate_slug>/<str:prod_slug>',views.productview,name='productview'),
   
   path('resigster/',authview.Register,name='register'),
   path('login/',authview.loginPage,name='login'),
   path('logout/',authview.logoutpage,name='logout'),
   path('add-to-cart',cartview.funcart,name='addtocart'),
   path('cart',cartview.cartpage,name='cart'),
   path('update-cart',cartview.updateCart,name='update-cart'),
   path('delete-cart-item',cartview.deletecartitem,name='delete-cart-item'),
   path('wishlist',wishlist.funWishlist,name='wishlist'),
   path('add-to-wishlist',wishlist.addToWishlist,name='addtowishlist'),
   path('delete-wishlist-item',wishlist.deletewishlistitem,name='delete-wishlist-item'),
   path('checkout',checkout.funcheckout,name='checkout'),
   path('placeorder',checkout.placeorder,name='placeorder'),
   path('proceeed-to-pay',checkout.razorpayCheck,name='proceeed-to-pay'),
   path('my-order',order.myorder,name='my-order'),
   path('orderview/<str:t_no>',order.vieworder,name='orderview'),
   
  
   
   
]
