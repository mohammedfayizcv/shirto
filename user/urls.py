
from django.contrib import admin
from django.urls import include, path
from .import views

from user.registerview import authview


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
]
