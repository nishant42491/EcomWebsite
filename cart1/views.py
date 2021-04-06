from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Cart

# Create your views here.

def addtocartview(request):
    if request.method=="POST":
        qtt=request.POST['qt']
        prc=request.POST['price']
        ttl=request.POST['title']
        ipk=request.POST['pk']


    t=Cart.objects.filter(itemid=int(ipk))
    for x in t:
        
        x.quantity+=int(qtt)
        x.save()
        
    
        
    '''cart2=Cart()
    cart2.productname=ttl
    cart2.itemprice=prc
    cart2.quantity=qtt
    cart2.save()'''
    
    return render(request,'cartview.html')

class CartListView(ListView): # new
    model = Cart
    template_name = 'cartview1.html'

    
    

