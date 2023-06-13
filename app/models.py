from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# About Model - Table
class About(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=800)

class Feature(models.Model):
    title =  models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    featureImg = models.ImageField(upload_to = 'projImg/')

class Customar(models.Model):
    
    SELECT_DISTRICT = [
        ('Barguna','Barguna'),
        ('Barisal','Barisal'),
        ('Bhola','Bhola'),
        ('Jhalokati','Jhalokati'),
        ('Patuakhali','Patuakhali'),
        ('Pirojpur','Pirojpur'),
        ('Bandarban','Bandarban'),
        ('Brahmanbaria','Brahmanbaria'),
        ('Chandpur','Chandpur'),
        ('Chittagong','Chittagong'),
        ('Comilla','Comilla'),
        ('Coxs Bazar','Coxs Bazar'),
        ('Feni','Feni'),
        ('Khagrachhari','Khagrachhari'),
        ('Lakshmipur','Lakshmipur'),
        ('Noakhali','Noakhali'),
        ('Rangamati','Rangamati'),
        ('Dhaka','Dhaka'),
        ('Faridpur','Faridpur'),
        ('Gazipur','Gazipur'),
        ('Gopalganj','Gopalganj'),
        ('Kishoreganj','Kishoreganj'),
        ('Madaripur','Madaripur'),
        ('Manikganj','Manikganj'),
        ('Munshiganj','Munshiganj'),
        ('Narayanganj','Narayanganj'),
        ('Narsingdi','Narsingdi'),
        ('Rajbari','Rajbari'),
        ('Shariatpur','Shariatpur'),
        ('Tangail','Tangail'),
        ('Bagerhat','Bagerhat'),
        ('Chuadanga','Chuadanga'),
        ('Jessore','Jessore'),
        ('Jhenaidah','Jhenaidah'),
        ('Khulna','Khulna'),
        ('Kushtia','Kushtia'),
        ('Magura','Magura'),
        ('Meherpur','Meherpur'),
        ('Narail','Narail'),
        ('Satkhira','Satkhira'),
        ('Jamalpur','Jamalpur'),
        ('Mymensingh','Mymensingh'),
        ('Netrokona','Netrokona'),
        ('Sherpur','Sherpur'),
        ('Bogra','Bogra'),
        ('Joypurhat','Joypurhat'),
        ('Naogaon','Naogaon'),
        ('Natore','Natore'),
        ('Chapai Nawabganj','Chapai Nawabganj'),
        ('Pabna','Pabna'),
        ('Rajshahi','Rajshahi'),
        ('Sirajganj','Sirajganj'),
        ('Dinajpur','Dinajpur'),
        ('Gaibandha','Gaibandha'),
        ('Kurigram','Kurigram'),
        ('Lalmonirhat','Lalmonirhat'),
        ('Nilphamari','Nilphamari'),
        ('Panchagarh','Panchagarh'),
        ('Rangpur','Rangpur'),
        ('Thakurgaon','Thakurgaon'),
        ('Habiganj','Habiganj'),
        ('Moulvibazar','Moulvibazar'),
        ('Sunamganj','Sunamganj'),
        ('Sylhet','Sylhet'),
    ]
    
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    district = models.CharField(max_length=25, choices=SELECT_DISTRICT)
    address = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
    


class ShipingFee(models.Model):
    shipingfee   = models.IntegerField(blank=True)
    
    def __str__(self):
        return str(self.shipingfee)
    

class Product(models.Model):
    
    PRODUCT_CHOICE = [
        ('honey','Honey'),
        ('ghee','Ghee'),
        ('red_salt','red salt'),
        ('musterd_oil','Musterd oil'),
    ]
    title =  models.CharField(max_length=50, default='')
    description = models.TextField(max_length=700)
    brand = models.CharField(max_length=100, default='')
    productImg = models.ImageField(upload_to = 'projImg/')
    sellingprice = models.FloatField()
    discountedprice = models.FloatField(blank=True)
    catagory = models.CharField(choices=PRODUCT_CHOICE, max_length=30)
    quantity = models.CharField(max_length=20) 
    is_available = models.BooleanField(default=True)
    in_stock = models.CharField(max_length=6, default=5)
    shipingfee = models.ForeignKey(ShipingFee, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return str(self.catagory)
    
    
class Cart(models.Model):
    product   = models.ForeignKey(Product, on_delete=models.CASCADE)
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity  = models.IntegerField(default=1)
    
    
class OrderPlaced(models.Model):

    STATUS = [
    ('accepted', 'accepted'),
    ('packed', 'packed'),
    ('on the way', 'on the way'),
    ('deliverd', 'deliverd'),
    ('cancel', 'cancel')

]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customar = models.ForeignKey(Customar, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    orderd_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS, default='pending')
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discountedprice
    
    