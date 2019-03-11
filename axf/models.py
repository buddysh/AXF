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

# 商品 模型
class Goods(models.Model):
    # 商品ID
    productid = models.CharField(max_length=10)
    # 商品图片
    productimg = models.CharField(max_length=100)
    # 商品名称
    productname = models.CharField(max_length=100)
    # 商品长名字
    productlongname = models.CharField(max_length=256)
    # 是否精选
    isxf = models.IntegerField()
    # 是否买一送一
    pmdesc = models.IntegerField()
    # 商品规格
    specifics = models.CharField(max_length=100)
    # 商品价格
    price = models.DecimalField(max_digits=6,decimal_places=2)
    # 商品超市价格
    marketprice = models.DecimalField(max_digits=6, decimal_places=2)
    # 分类ID
    categoryid = models.IntegerField()
    # 子类ID
    childcid = models.IntegerField()
    # 子类名称
    childcidname = models.CharField(max_length=100)
    # 详情页ID
    dealerid = models.CharField(max_length=10)
    # 库存
    storenums = models.IntegerField()
    # 销售
    productnum = models.IntegerField()

    class Meta:
        db_table = 'axf_goods'

class User(models.Model):
    # 邮箱
    email = models.CharField(max_length=40, unique=True)
    # 密码
    password = models.CharField(max_length=256)
    # 昵称
    name = models.CharField(max_length=100)
    # 头像
    img = models.CharField(max_length=40, default='axf.png')
    # 等级
    rank = models.IntegerField(default=1)

    class Meta:
         db_table = 'axf_user'


# 购物车 模型类
class Cart(models.Model):
    # 用户 [添加的这个商品属于哪个用户]
    user = models.ForeignKey(User)
    # 商品 [添加的是哪个商品]
    goods = models.ForeignKey(Goods)
    ## 具体规格 [颜色、内存、版本、大小.....]
    # 商品数量
    number = models.IntegerField()
    # 是否选中
    isselect = models.BooleanField(default=True)
    # 是否删除
    isdelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'axf_cart'



