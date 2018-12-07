from django.conf.urls import url

from . import views
urlpatterns = [
   
    url(r'^$',views.login),
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
    
    url(r'^index/', views.index),
    
    url(r'^index1/', views.index1),
    url(r'^add_link/', views.add_link),
    url(r'^edit/', views.edit),
    url(r'^delete/', views.delete),

    url(r'^index2/', views.index2),
    url(r'^add_dev/', views.add_dev),
    url(r'^edit_dev/', views.edit_dev),
    url(r'^del_dev/', views.del_dev),
    url(r'^web_ssh/', views.web_ssh),
    url(r'^det_dev/', views.det_dev), 
    url(r'^home/', views.home),

    url(r'^index3/', views.index3),


    url(r'^index4/', views.index4),
    url(r'^add_user/', views.add_user),
    url(r'^del_user/', views.del_user),
    url(r'^edit_user/', views.edit_user),

    url(r'^index5/', views.index5),

]
