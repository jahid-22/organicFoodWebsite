from django.shortcuts import render, redirect
from django.views import View
from . forms import UserRegi, CustomarAdd
from django.contrib import messages
from . models import Customar, Cart, OrderPlaced, Product, Feature, ShipingFee, About
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator #@method_decorator(login_required, name='dispatch')

# Create your views here.

# Index / home view

class Home(View):
    def get(self, request):
        obj = About.objects.all()
        fobj = Feature.objects.all()
        honey = Product.objects.filter(catagory='honey')
        oil = Product.objects.filter(catagory='musterd_oil')
        ghee = Product.objects.filter(catagory='ghee')
        red_salt = Product.objects.filter(catagory='red_salt')

        context = {
            'honey': honey,
            'oil': oil,
            'ghee': ghee,
            'red_salt': red_salt,
            'about':obj,
            'feature':fobj
        }
        return render(request, 'index.html', context)

class AboutView(View):
    def get(self, request):
        obj = About.objects.all()
        return render(request, 'about.html', {'about':obj})

# All product view


class Products(View):
    def get(self, request):
        honey = Product.objects.filter(catagory='honey', is_available=True)
        oil = Product.objects.filter(catagory='musterd_oil', is_available=True)
        ghee = Product.objects.filter(catagory='ghee', is_available=True)
        context = {
            'honey': honey,
            'oil': oil,
            'ghee': ghee,
        }
        return render(request, 'product.html', context)

# product detail view


def product_detail(request, id):
    getProduct = Product.objects.get(id=id)
    
    product_allready_on_cart = False
    if request.user.is_authenticated:
        product_allready_on_cart = Cart.objects.filter(Q(user=request.user) & Q(product=id)).exists()

    return render(request, 'product_detail.html', {'poroduct': getProduct, 'product_allready_on_cart':product_allready_on_cart})

# cart view

@login_required
def add_to_cart(request):
    get_product_id = request.GET.get('prod_id')
    
    # if product already in cart
    product_in_cart = Cart.objects.filter(Q(user=request.user) & Q(product=get_product_id)).exists()
    
    if product_in_cart:
        return redirect('/show_cart/')
    else:
        
        get_product = Product.objects.get(id=get_product_id)
        if request.user.is_authenticated: 
            cart = Cart(user=request.user, product=get_product)
            cart.save()
        return redirect('/show_cart/')


# show cart
@login_required()
def showcart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    product_count = cart.count()

    # Total amount of product

    totalamount = 0.0
    amount = 0.0
    shiping_fee = 100

    cartProd = [p for p in Cart.objects.all() if p.user == request.user]
    
    if cartProd:
        for p in cartProd:
            tempamount = p.quantity* p.product.sellingprice
            amount += tempamount
 
    totalamount = amount + shiping_fee

    context = {
        'carts': cart,
        'product_count': product_count,
        'amount': amount,
        'totalamount': totalamount,
        'shiping_fee': shiping_fee
    }

    return render(request, 'cart.html', context)

@login_required
def pluscart(request):
    if request.method == 'GET':
        
        try:
            prod_id = request.GET['prod_id']
            print(prod_id)
            c = Cart.objects.get(Q(product = prod_id) & Q(user=request.user))
            c.quantity += 1
            c.save()
        except Exception as e:
            raise e
        
        # Total amount of product
        amount = 0.0
        shiping_fee = 100
        
        cartProd = [p for p in Cart.objects.all() if p.user == request.user]
        if cartProd:
            for p in cartProd:
                tempamount = p.quantity * p.product.sellingprice
                amount += tempamount
                
        data = {
            'amount': amount,
            'totalamount': amount + shiping_fee,
            'quantity' : c.quantity
        }
        return JsonResponse(data)

@login_required
def minuscart(request):
    if request.method == 'GET':
        
        try:
            prod_id = request.GET['prod_id']
            c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
            c.quantity -= 1
            c.save()
        except Exception as e:
            raise e
        
        # Total amount of product
        amount = 0.0
        shiping_fee = 100
        
        cartProd = [p for p in Cart.objects.all() if p.user == request.user]
        if cartProd:
            for p in cartProd:
                tempamount = p.quantity * p.product.sellingprice
                amount += tempamount
                
        data = {
            'amount': amount,
            'totalamount': amount + shiping_fee,
            'quantity' : c.quantity
        }
        return JsonResponse(data)

@login_required
def removecart(request):
    if request.method == 'GET':
        
        try:
            prod_id = request.GET['prod_id']
            c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
            c.delete()
        except Exception as e:
            raise e
        
        # Total amount of product
        amount = 0.0
        shiping_fee = 100
        
        cartProd = [p for p in Cart.objects.all() if p.user == request.user]
        if cartProd:
            for p in cartProd:
                tempamount = p.quantity * p.product.sellingprice
                amount += tempamount
                

        data = {
            'amount': amount,
            'totalamount': amount + shiping_fee
        }
        
    return JsonResponse(data)

@login_required()
def buy_now(request):
    prod_id = request.GET.get('prod_id')
    print(f"this is a product id: {prod_id}")
    get_product = Product.objects.get(id=prod_id)
    print(f"this is product according to the product id: {get_product}")
    saving_product_in_to_cart = Cart(user=request.user, product=get_product,quantity=1).save()
    return redirect('/checkout/')

# check out view
@login_required
def checkout(request):
    user = request.user
    address = Customar.objects.filter(user=user)
    cart = Cart.objects.filter(user=user)
    total_quantity = 0
    for c in cart:
        tempquantity = c.quantity + 0
        total_quantity += tempquantity
    amount = 0.0
    shiping_fee = 100
    cartProd = [p for p in Cart.objects.all() if p.user == user]
    if cartProd:
        for p in cartProd:
            tempamount =  p.quantity * p.product.sellingprice
            amount += tempamount
    context = {
        'total_quantity' : total_quantity, 
        'address':address,
        'totalamount' : amount + shiping_fee
    }            
    return render(request, 'checkout.html', context)             

@login_required
def paymentdone(request):
    custid = request.GET.get('custid')
    user = request.user
    customar = Customar.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    
    for c in cart:
        OrderPlaced(user=user, customar=customar, product=c.product, quantity=c.quantity).save()
        c.delete()
    
    
    return redirect('/order/')
@login_required
def order(request):
    op = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'order.html', {'order_placed':op})

# feature 
class FeatureView(View):
    def get(self, request):
        obj = Feature.objects.all()
        return render(request, 'feature.html', {'feature':obj})


class Testimonial(View):
    def get(self, request):
        return render(request, 'testimonial.html')


class Contact(View):
    def get(self, request):
        return render(request, 'contact.html')

# Customar profile view
@login_required()
def profile(request):
    form = request.user
    return render(request, 'profile.html', {'form': form})

# customar address view

@login_required
def address(request):
    form = Customar.objects.filter(user=request.user)
    # cartProd = [u for u in Customar.objects.all() if p.user ==request.user]
    # print(cartProd)
    return render(request, 'address.html', {'form': form})

# add new address view

@login_required
def add_address(request):
    if request.method == 'POST':
        form = CustomarAdd(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            district = form.cleaned_data['district']

            reg = Customar(user=request.user, name=name, email=email,
                           phone=phone, address=address, district=district)
            reg.save()
            messages.success(request, 'Successfully added your address!')
            form = CustomarAdd()
    else:
        form = CustomarAdd()
    return render(request, 'add-address.html', {'form': form})

# User Registration view


class UserRegistration(View):
    def get(self, request):
        form = UserRegi()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserRegi(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulaions! Your account created successfully!!')
            form = UserRegi()
        return render(request, 'register.html', {'form': form})
