# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from home.models import *
from carts.forms import CartAddProductForm
# Create your views here.

def index(request):

    categories= Categories.objects.filter();
    products = Product.objects.filter(cate_id=1)

    context ={
        'categories':categories,
        'products': products
    }

    return render(request,"home/index.html",context)

def categories (request,cate_id):
    categories = Categories.objects.filter();
    products= Product.objects.filter(cate_id=cate_id)

    context={
        'categories': categories,
        'products': products
    }
    return render(request,"home/index.html",context)



def product_detail(request, id, slug):
    product = get_object_or_404(Product, product_id=id,
                                         slug=slug,
                                         available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})