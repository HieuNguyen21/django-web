from django.db import models
from store.models import Product

class Cart(models.Model):
    cart_id = models.CharField(max_length=250,blank=True)
    data_added = models.DateField(auto_now_add=True)

    def _str_ (self):
        return self.cart_id
class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
  
    def _str_ (self):
        return self.product
# Create your models here.
