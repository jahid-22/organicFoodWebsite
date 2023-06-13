from django.contrib import admin
from . models import Cart, Customar, Product, OrderPlaced, About, Feature, ShipingFee
# Register your models here.

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'description']

@admin.register(Feature)
class AdminFeature(admin.ModelAdmin):
    list_display = ['id','title','featureImg']

@admin.register(Customar)
class AdminCustomar(admin.ModelAdmin):
    list_display = ['id', 'name', 'email','phone','district','address','user']

@admin.register(ShipingFee)
class AdminShipingFee(admin.ModelAdmin):
    list_display = ['shipingfee']

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['id','title', 'sellingprice', 'catagory', 'quantity', 'is_available','in_stock','brand']

@admin.register(Cart)
class AdminCart(admin.ModelAdmin):
    list_display = ['id','user', 'product','quantity']

@admin.register(OrderPlaced)
class AdminOrderPlaced(admin.ModelAdmin):
    list_display = ['id','user','customar','product','quantity','orderd_date','status']
