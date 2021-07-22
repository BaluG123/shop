from django.db import models
from django.utils import timezone

# Create your models here.
class items(models.Model):
    SITE_CHOICES=(('amazon','Amazon'),('flifkart','Flifkart'),('ajio','Ajio'))
    COMPANY_CHOICES=(('puma','Puma'),('adidas','Adidas'),('nike','Nike'),('h&m','H&M'))
    item_type=(('t-shirt','T-short'),('shirt','Shirt'),('pant','Pant'),('shoe','Shoe'))
    item_name=models.CharField(max_length=100)
    image=models.FileField(null=True,blank=True,upload_to='images/')
    link=models.CharField(max_length=10000)
    price=models.IntegerField()
    off_price=models.IntegerField()
    off_p=models.IntegerField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    site=models.CharField(max_length=100,choices=SITE_CHOICES,default="amazon")
    company=models.CharField(max_length=100,choices=COMPANY_CHOICES,default="null")
    item=models.CharField(max_length=100,choices=item_type,default="null")

    class Meta:
        ordering=['-publish']

    def __str__(self):
        return self.item_name    

class items1(models.Model):
    SITE_CHOICES=(('amazon','Amazon'),('flifkart','Flifkart'),('ajio','Ajio'))
    COMPANY_CHOICES=(('puma','Puma'),('adidas','Adidas'),('nike','Nike'),('h&m','H&M'))
    item_type=(('t-shirt','T-shirt'),('shirt','Shirt'),('pant','Pant'),('shoe','Shoe'))
    item_name=models.CharField(max_length=100)
    image1=models.FileField(null=True,blank=True,upload_to='images/')
    image2=models.FileField(null=True,blank=True,upload_to='images/')
    image3=models.FileField(null=True,blank=True,upload_to='images/')
    image4=models.FileField(null=True,blank=True,upload_to='images/')
    link=models.CharField(max_length=10000)
    price=models.IntegerField()
    off_price=models.IntegerField()
    off_p=models.IntegerField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    site=models.CharField(max_length=100,choices=SITE_CHOICES,default="amazon")
    company=models.CharField(max_length=100,choices=COMPANY_CHOICES,default="null")
    item=models.CharField(max_length=100,choices=item_type,default="null")

    class Meta:
        ordering=['-publish']

    def __str__(self):
        return self.item_name           


class items2(models.Model):
    SITE_CHOICES=(('amazon','Amazon'),('flifkart','Flifkart'),('ajio','Ajio'))
    COMPANY_CHOICES=(('puma','Puma'),('adidas','Adidas'),('nike','Nike'),('h&m','H&M'))
    item_type=(('t-shirt','T-short'),('shirt','Shirt'),('pant','Pant'),('shoe','Shoe'))
    item_name=models.CharField(max_length=100)
    image1=models.FileField(null=True,blank=True,upload_to='images/')
    link=models.CharField(max_length=10000)
    price=models.IntegerField()
    off_price=models.IntegerField()
    off_p=models.IntegerField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    site=models.CharField(max_length=100,choices=SITE_CHOICES,default="amazon")
    company=models.CharField(max_length=100,choices=COMPANY_CHOICES,default="null")
    item2=models.CharField(max_length=100,choices=item_type,default="null")
    item_name2=models.CharField(max_length=100)
    image2=models.FileField(null=True,blank=True,upload_to='images/')
    link2=models.CharField(max_length=10000)
    price2=models.IntegerField()
    off_price2=models.IntegerField()
    off_p2=models.IntegerField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    site2=models.CharField(max_length=100,choices=SITE_CHOICES,default="amazon")
    company2=models.CharField(max_length=100,choices=COMPANY_CHOICES,default="null")
    item3=models.CharField(max_length=100,choices=item_type,default="null")
    item_name3=models.CharField(max_length=100)
    image3=models.FileField(null=True,blank=True,upload_to='images/')
    link3=models.CharField(max_length=10000)
    price3=models.IntegerField()
    off_price3=models.IntegerField()
    off_p3=models.IntegerField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    site3=models.CharField(max_length=100,choices=SITE_CHOICES,default="amazon")
    company3=models.CharField(max_length=100,choices=COMPANY_CHOICES,default="null")
    item3=models.CharField(max_length=100,choices=item_type,default="null")

    class Meta:
        ordering=['-publish']

    def __str__(self):
        return self.item_name 



