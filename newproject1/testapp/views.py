from django.shortcuts import render
from . models import items,items1,items2

# Create your views here.
'''
def home_view(request):
    items_list=items.objects.all()
    return render(request,'testapp/home.html',{'items_list':items_list})

def home_view1(request):
    items_list1=items1.objects.all()
    return render(request,'testapp/oof.html',{'items_list1':items_list1})    
''' 
def home_view2(request):
    items_list2=items2.objects.all()
    return render(request,'testapp/oof2.html',{'items_list2':items_list2})        