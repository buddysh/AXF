import hashlib
import json
import random
import time

from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from axf.models import Wheel, Nav, Mustbuy, Shop, Mainshow, Foodtypes, Goods, User


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

# @csrf_exempt
def market(request,childid='0',sortid='0'):

    index = int(request.COOKIES.get('index', '0'))

    if request.method == 'GET':
        foodtypes = Foodtypes.objects.all()
        # goods = Goods.objects.filter(categoryid=num).filter()
        childtypes = foodtypes[index].childtypenames.split('#')
        categoryid = foodtypes[index].typeid
        if childid == '0':
            goods = Goods.objects.filter(categoryid=categoryid)
        else:
            goods = Goods.objects.filter(categoryid=categoryid).filter(childcid=childid)

        if sortid == '1':
            goods = goods.order_by('-productnum')
        elif sortid == '2':
            goods = goods.order_by('price')
        elif sortid == '3':
            goods = goods.order_by('-price')

        # print(childtypes)
        child_typelist=[]
        for item in childtypes:
            nameid=item.split(':')
            temp={
                'name':nameid[0],
                'id':nameid[1]
            }
            child_typelist.append(temp)
        # print(child_typelist)
        context = {
            'foodtypes': foodtypes,
            'goods': goods,
            'child_typelist':child_typelist,
            'childid': childid
        }
        return render(request,'market/market.html',context=context)
    # if request.method == 'POST':
    #     foodtypes = Foodtypes.objects.values()
    #     num=request.POST.get('num')
    #     goods = Goods.objects.filter(categoryid=num).values()
    #     context = {
    #         'foodtypes': list(foodtypes),
    #         'goods': list(goods),
    #     }
    #     print(context)
    #     return JsonResponse(context)

def cart(request):
    return render(request,'cart/cart.html')


# def mine(request):
#     return render(request,'mine/mine.html')

def mine(request):
    token = request.session.get('token')
    userid = cache.get(token)
    user = None
    if userid:
        user = User.objects.get(pk=userid)
    return render(request, 'mine/mine.html', context={'user':user})


def login(request):
    return render(request, 'mine/login.html')


def logout(request):
    request.session.flush()
    return redirect('axf:mine')


def generate_password(param):
    md5 = hashlib.md5()
    md5.update(param.encode('utf-8'))
    return md5.hexdigest()


def generate_token():
    temp = str(time.time()) + str(random.random())
    md5 = hashlib.md5()
    md5.update(temp.encode('utf-8'))
    return md5.hexdigest()


def register(request):
    if request.method == 'GET':
        return render(request, 'mine/register.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        passoword = generate_password(request.POST.get('password'))
        user = User()
        user.email = email
        user.password = passoword
        user.name = name
        user.save()
        token = generate_token()
        cache.set(token, user.id, 60*60*24)
        request.session['token'] = token
        return redirect('axf:mine')