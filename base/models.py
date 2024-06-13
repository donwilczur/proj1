from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Yerbas (models.Model):
    yerba_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    opis=models.TextField(blank=True)
    price_pu = models.IntegerField()
    dost_ilosc = models.IntegerField()
    foto = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.name
    
    @property
    def fotoURL(self):
        try:
            url= self.foto.url
        except: 
            url = ''
        return url

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name= models.CharField(max_length=200,null=True)
    email= models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False, null=True, blank=False)
    transaction_id=models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems= self.orderitem_set.all()
        total= sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems= self.orderitem_set.all()
        total= sum([item.quantity for item in orderitems])
        return total
    
class OrderItem(models.Model):
    yerba=models.ForeignKey(Yerbas,on_delete=models.SET_NULL, blank=True, null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL, blank=True, null=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total= self.yerba.price_pu * self.quantity
        return total