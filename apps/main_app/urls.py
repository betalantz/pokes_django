from django.conf.urls import url
from . import views

def test(request):
    print '>'*20, 'welcome to main_app urls'

urlpatterns = [
    # url(r'^$', views.test),
    url(r'^main_app/dashboard/$', views.dashboard, name='my_dashboard'),
]