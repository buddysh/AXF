from django.conf.urls import url

from axf import views

urlpatterns=[
    url('^$',views.home,name='home'),
    url('^market/$',views.market,name='market'),
    url('^market/(\d+)/(\d+)/$', views.market, name='marketbase'),
    url('^cart/$',views.cart,name='cart'),
    url('^mine/$',views.mine,name='mine'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^checkemail/$', views.checkemail, name='checkemail'),

]