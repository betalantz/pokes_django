from django.conf.urls import url
from . import views

def test(request):
    print '>'*20, 'welcome to users_app urls'

urlpatterns = [
    # url(r'^$', views.test),
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^register/$', views.register, name='my_register'),
    url(r'^login/$', views.login, name='my_login'),
    url(r'^logout/$', views.logout, name='my_logout'),

]