from django.shortcuts import render

# Create your views here.
from axf.models import Wheel, Nav, Mustbuy, Shop, Mainshow, Foodtypes


def home(request):
    wheels=Wheel.objects.all()
    navs=Nav.objects.all()
    mustbuys=Mustbuy.objects.all()
    shophead=Shop.objects.all()[0]
    shoptabs=Shop.objects.all()[1:3]
    shopclasses=Shop.objects.all()[3:7]
    shopcommends=Shop.objects.all()[7:11]
    mainshows = Mainshow.objects.all()
    response_str={
        'wheels': wheels,
        'navs':navs,
        'mustbuys':mustbuys,
        'shophead':shophead,
        'shoptabs':shoptabs,
        'shopclasses':shopclasses,
        'shopcommends':shopcommends,
        'mainshows':mainshows
    }
    return render(request,'home/home.html',
                  context=response_str)


def market(request):
    foodtypes=Foodtypes.objects.all()
    context={
        'foodtypes':foodtypes,
    }
    return render(request,'market/market.html',context=context)


def cart(request):
    return render(request,'cart/cart.html')


def mine(request):
    return render(request,'mine/mine.html')