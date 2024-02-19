from django.contrib import admin
from django.urls import path
from . import views
from .views import CreateStripeCheckoutSessionView

urlpatterns = [
    path("",views.index,name='index'),
    path("login.html",views.login1,name='login'),
    path("register.html",views.register,name='register'),
    path("logout",views.logout1,name='logout'),
    path("contact",views.contact,name='contact'),
    path("profile",views.profile,name='profile'),
    path("checkout",views.checkout,name='checkout'),
    path("order",views.Order_confirm,name='order'),
    

    
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),


    path(
        "create-checkout-session",
        CreateStripeCheckoutSessionView.as_view(),
        name="create-checkout-session",
     ),


     path('confirmation',views.confirmation,name='confirmation'),
     path('products/<int:product_id>/',views.product_detail_view, name='product_detail'),
     path('electronics/<int:product_id>/',views.electronics_detail_view, name='electronics_detail')
     


]

