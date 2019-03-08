from django.db import models

class BaseModel(models.Model):
    img=models.CharField(max_length=100)
    name=models.CharField(max_length=20)
    trackid=models.CharField(max_length=10)

    class Meta:
        abstract=True

class Wheel(BaseModel):
    class Meta:
        db_table='axf_wheel'


class Nav(BaseModel):
    class Meta:
        db_table='axf_nav'

class Mustbuy(BaseModel):
    class Meta:
        db_table='axf_mustbuy'

class Shop(BaseModel):
    class Meta:
        db_table='axf_shop'
# insert into axf_mainshow\
# (trackid,name,img,categoryid,brandname,img1,childcid1,
#  productid1,longname1,price1,marketprice1,img2,childcid2,
#  productid2,longname2,price2,marketprice2,img3,childcid3,
#  productid3,longname3,price3,marketprice3)

class Mainshow(models.Model):
    trackid=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    img=models.CharField(max_length=100)
    categoryid=models.CharField(max_length=10)
    brandname=models.CharField(max_length=50)

    img1=models.CharField(max_length=100)
    childcid1=models.CharField(max_length=50)
    productid1=models.CharField(max_length=10)
    longname1=models.CharField(max_length=50)
    price1=models.CharField(max_length=10)
    marketprice1=models.CharField(max_length=10)

    img2=models.CharField(max_length=100)
    childcid2=models.CharField(max_length=50)
    productid2=models.CharField(max_length=10)
    longname2=models.CharField(max_length=50)
    price2=models.CharField(max_length=10)
    marketprice2=models.CharField(max_length=10)

    img3=models.CharField(max_length=100)
    childcid3=models.CharField(max_length=50)
    productid3=models.CharField(max_length=10)
    longname3=models.CharField(max_length=50)
    price3=models.CharField(max_length=10)
    marketprice3=models.CharField(max_length=10)

'''
insert into axf_foodtypes(typeid,typename,childtypenames,typesort) 
values("104749","热销榜","全部分类:0",1)
'''
class Foodtypes(models.Model):
    typeid=models.CharField(max_length=20)
    typename=models.CharField(max_length=20)
    childtypenames=models.CharField(max_length=200)
    typesort=models.IntegerField()
    class Meta:
        db_table='axf_foodtypes'



