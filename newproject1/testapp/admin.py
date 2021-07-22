from django.contrib import admin
from . models import items,items1,items2

class itemsAdmin(admin.ModelAdmin):
    list_display=['item_name','image','link','price','off_price','off_p','publish','created','updated','site','company','item']
    list_filter=('item_name','price','created','site','company','item')
    search_fields=('item_name','company','item','site')

class itemsAdmin1(admin.ModelAdmin):
    list_display=['item_name','image1','image2','image3','image4','link','price','off_price','off_p','publish','created','updated','site','company','item']
    list_filter=('item_name','price','created','site','company','item')
    search_fields=('item_name','company','item','site')  

class itemsAdmin2(admin.ModelAdmin):
    list_display=['item_name','item_name2','item_name3','image1','image2','image3','link','price','off_price','off_p','publish','created','updated','site','company','link2','price2','off_price2','off_p2','link3','price3','off_price3','off_p3']
    list_filter=('item_name','price','created','site','item_name3','site3','company3','item3')
    search_fields=('item_name','company','item','site')  



# Register your models here.
admin.site.register(items,itemsAdmin)
admin.site.register(items1,itemsAdmin1)
admin.site.register(items2,itemsAdmin2)
