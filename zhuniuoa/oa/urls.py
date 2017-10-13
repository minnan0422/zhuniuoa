from django.conf.urls import url
from . import views

app_name = 'oa'
urlpatterns = [

    url(r'^overtime', views.work_time, name='overtime'),
    url(r'^list/(?P<oa_user>(.*)+)/$', views.work_list, name='list'),
    url(r'^select', views.select, name='select'),
    url(r'^offtime', views.off_time, name='offtime'),
    url(r'^offlist/(?P<oa_user>(.*)+)/$', views.off_list, name='offlist'),
    url(r'^totaltime/(?P<oa_user>(.*)+)/$', views.total_time, name='totaltime'),

]