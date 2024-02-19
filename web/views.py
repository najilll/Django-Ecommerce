from django.shortcuts import render, get_object_or_404
from . models import Product
from . models import slider,Contact,Electronics,Baner,Order,Order_item
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . models import Order_item

from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from cart.cart import Cart


from django.contrib.auth.decorators import login_required
import stripe
from django.conf import settings
from django.views import View


def index(request):
    context={
        'produ':Product.objects.all(),
        'front':slider.objects.all(),
        'gadgets':Electronics.objects.all(),
        'baner':Baner.objects.all(),
    }
    return render(request,'web/index.html',context)




def login1(request):
    if request.method=="POST":
        name=request.POST.get('user_name')
        pass1=request.POST.get('password')
        user=authenticate(username=name,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return redirect('register.html')

    return render(request,'web/accounts/login.html')


def register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirm_password')
        if pass1==pass2:
               user=User.objects.create_user(name,email,pass1)
               
               user.save()
               return redirect("login.html")
    return render(request,'web/accounts/register.html')


def logout1(request):
    logout(request)
    return redirect('index')


def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        location = request.POST.get('location')
        message = request.POST.get('message')

        Contact1=Contact(
            name=name,
            email=email,
            location=location,
            message=message
        )

        Contact1.save()
    return render(request,'web/contact.html')


@login_required(login_url="login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="login")

def cart_detail(request):
    return render(request,'web/cart.html')



@login_required(login_url="login")
def profile(request):
    return render(request,'web/profile.html')


@login_required(login_url="login")
def checkout(request):
    if request.method=='POST':

        uid=request.session.get('_auth_user_id')
        userr=User.objects.get(id=uid)
        cart=request.session.get('cart')
        First_name = request.POST.get('first_name')
        Last_name = request.POST.get('last_name')
        Street_address = request.POST.get('street_address')
        Country = request.POST.get('country')
        City = request.POST.get('city')
        State = request.POST.get('state')
        Postcode = request.POST.get('postcode')
        Phone = request.POST.get('phone')
        Email = request.POST.get('email')

        order1=Order(
            First_name=First_name,
            Last_name=Last_name,
            Country=Country,
            Street_address=Street_address,
            Town_city=City,
            State=State,
            Zip=Postcode,
            Number=Phone,
            email=Email,
            user=userr,
        )

        order1.save()
        for i in cart:
            a=float(cart[i]['price'])
            b=int(cart[i]['quantity'])
            total=a*b

            product_details=Order_item(
                order=order1,
                product=(cart[i]['name']),
                image=cart[i]['image'],
                quantity=cart[i]['quantity'],
                price=cart[i]['price'],
                total=total
            )
            product_details.save()
    return render(request,'web/checkout.html')



@login_required(login_url="login")
def Order_confirm(request):
    return render(request,'web/order.html')




stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateStripeCheckoutSessionView(View):
    """
    Create a checkout session and redirect the user to Stripe's checkout page
    """

    def post(self, request, *args, **kwargs):
        
        price1=Product.objects.all()
        for p in price1:
            price2=p.price
            name1=p.name
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": int(price2) * 2,
                        "product_data": {
                            "name": name1,
                        },
                    },
                    "quantity":1,
                }
            ],
            
            mode="payment",
            success_url='http://localhost:8000/order',
            cancel_url='http://localhost:8000/login',
        )
        return redirect(checkout_session.url)



def confirmation(request):
    return render(request,'web/confirmation.html')






def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'web/product-details.html', context)


def electronics_detail_view(request, product_id):
    gadgets = get_object_or_404(Electronics, id=product_id)
    context = {
        'gadgets': gadgets,
    }
    return render(request, 'web/product-details.html', context)

def error_404_view(request,exception):
    return render(request,'web/404.html')
