from django.db import models
import uuid,qrcode
from io import BytesIO
from django.core.files import File
from restaurant import settings
# Create your models here.


# Table model
class Table(models.Model):
    number = models.IntegerField(unique=True)
    token = models.UUIDField(default=uuid.uuid4,unique=True)
    qr_code = models.ImageField(upload_to="qr_code/",blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Table - {self.number}"
    
    def generate_qr(self):
        url = f"{settings.BASE_URL}/menu/{self.token}"
        qr = qrcode.make(url)

        buffer = BytesIO()
        qr.save(buffer,format='PNG')
        filename = f"table_{self.number}.png"

        self.qr_code.save(filename,File(buffer),save=False)

    
    def save(self,*args,**kwargs):
        creating = self.pk is None
        super().save(*args,**kwargs)

        if creating:
            self.generate_qr()
            super().save(update_fields = ['qr_code'])

    

# Category model
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    
# MenuItem model
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="menu_images/",null=True,blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


