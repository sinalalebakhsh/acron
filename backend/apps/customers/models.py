# acron/backend/apps/customers/models.py

from django.db import models
from django.conf import settings

class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Address(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='addresses')
    title = models.CharField(max_length=50,help_text="مثال: خانه، محل کار",null=True,blank=True)
    receiver_name = models.CharField(max_length=100,null=True,blank=True)
    phone_number = models.CharField(max_length=15,null=True,blank=True)
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.TextField()
    postal_code = models.CharField(max_length=10)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
    
    
    