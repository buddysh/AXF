from django.conf.urls import url

from axf import views

urlpatterns=[
    url('^$',views.home,name='home'),
    url('^market/$',views.market,name='market'),
    url('^cart/$',views.cart,name='cart'),
    url('^mine/$',views.mine,name='mine'),
]