# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from cmdb.models import user
from . import models
import sshv1
# Create your views here.

def my_login(func):
    def check_login(request):
       if request.session.has_key('user_id'):
          return func(request)
       else:
          return redirect('/login/')
    return check_login

def login(request):
     if request.session.get('is_login',None):
        return redirect('/index/')
     if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:  
            try:
#                 p = user.objects.get(name = u).password
                user = models.user.objects.get(name = username)
            except:
                return render(request,'login.html')
            if password == user.password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/index/')
     return render(request, 'login.html')    

def logout(request):
    if not request.session.get('is_login',None):
        return redirect('/index/')
    request.session.flush()
    return redirect('/index/')

@my_login
def index(request):
    dev = models.device.objects.all()
    on = models.device.objects.filter(state='True').count()
    off = models.device.objects.filter(state='False').count()    
    on_dev = int(on)
    off_dev = int(off)
    return render(request, 'index.html',locals())



@my_login
def index1(request):
    linklist =models.link.objects.all()
    return render(request, 'index1.html',{"link":linklist})    
   # return render(request, 'index1.html')

def add_link(request):
    if request.method == "POST":
        add_name = request.POST.get('name')
        add_remarks = request.POST.get('remarks')
        add_urls = request.POST.get('urls')
        add =models.link.objects.create(name=add_name,remarks=add_remarks,urls=add_urls)
    
        return redirect('/index1/')

def edit(request):
    if request.method == "POST":
        up_id = request.POST.get('id')
        up_name = request.POST.get('name')
        up_remarks = request.POST.get('remarks')
        up_urls = request.POST.get('urls')
        up = models.link.objects.get(id=up_id)
        up.name = up_name
        up.remarks = up_remarks
        up.urls = up_urls
        up.save()
        return redirect('/index1/')
    
def delete(request):
    try:
        idlist = request.GET['id']
        for i in idlist.split(','):
            info = models.link.objects.get(id=i).delete()
            return redirect('/index1/')
    except:
        return redirect('/index1/')
@my_login
def index2(request):
#    dev = models.device.objects.all()
    
#    for i in dev:
#        link = sshv1.sshlink(i.ip,i.port,i.uname,i.password)
#        up = models.device.objects.get(ip=i.ip)
#        up.state = link
#        up.save()
        
    devlist = models.device.objects.all()    
    
    return render(request, 'index2.html',{"dev":devlist})

def add_dev(request):
    if request.method == "POST":
        add_hname = request.POST.get('hname')
        add_ip = request.POST.get('ip')
        add_uname = request.POST.get('uname')
        add_pwd = request.POST.get('password')
        add_port = request.POST.get('port')
        add_position = request.POST.get('position')
        add_remarks = request.POST.get('remarks')
        port = int(add_port)
        add_state = sshv1.sshlink(add_ip,port,add_uname,add_pwd)
        

        add =models.device.objects.create(hname=add_hname,ip=add_ip,protoclo="SSH",uname=add_uname,password=add_pwd,port=add_port,position=add_position, remarks=add_remarks,state=add_state)

        return redirect('/index2/')

def edit_dev(request):
     if request.method == "POST":
         up_id = request.POST.get('id')   
         up_hname = request.POST.get('hname')
         up_ip = request.POST.get('ip')
         up_uname = request.POST.get('uname')
         up_pwd = request.POST.get('password')
         up_port = request.POST.get('port')
         up_position = request.POST.get('position')
         up_remarks = request.POST.get('remarks')
         port = int(up_port)
         up_state = sshv1.sshlink(up_ip,port,up_uname,up_pwd)
         
         up = models.device.objects.get(id=up_id)
         up.hname = up_hname
         up.ip = up_ip 
         up.uname = up_uname
         up.password = up_pwd
         up.port = up_port
         up.position = up_position
         up.remarks = up_remarks
         up.save()    
         return redirect('/index2/')
         
def del_dev(request):
    try:
        idlist = request.GET['id']
       	for i in idlist.split(','):
       	    info = models.device.objects.get(id=i).delete()
            return redirect('/index2/')
    except:
        return redirect('/index2/')

def web_ssh(request):
    
    return render(request,'web_ssh.html')

def det_dev(request):
    idlist = request.GET['id']
    dev = models.device.objects.get(id=idlist)
    dev_list = sshv1.sshdev(dev.ip,int(dev.port),dev.uname,dev.password)
    cpu_off =int(float(dev_list[0])*10)
    cpu_on = int(float(dev_list[1])*10)
    mem_off = int(dev_list[2])
    mem_on = int(dev_list[3])
    dis_off = dev_list[4]
    dis_on = dev_list[5]
    cpu_v = dev_list[6]
    mem = (mem_off + mem_on)/1024
    dist = dis_off + dis_on
    network = dev_list[7]
    os_v = dev_list[8]
    return render(request,'det_dev.html',locals())

@my_login
def index3(request):

    return render(request, 'index3.html')




def index4(request):
    dev = models.user.objects.all()

    return render(request, 'index4.html',{"list":dev})    

def add_user(request):
    if request.method == "POST":
        add_uesr = request.POST.get('name')
        add_pwd = request.POST.get('password')
        add =models.user.objects.create(name=add_user,password=add_pwd)
        return redirect('/index2/')

def edit_user(request):
    if request.method == "POST":
        up_id = request.POST.get('id')
        up_user = request.POST.get('name')
        up_pwd = request.POST.get('password')
        up = models.user.objects.get(id=up_id)
        up.name = up_user
        up.password = up_pwd
        up.save()
        return redirect('/index2/')

def del_user(request):
    try:
        idlist = request.GET['id']
        for i in idlist.split(','):
            info = models.user.objects.get(id=i).delete()
            return redirect('/index4/')
    except:
        return redirect('/index4/')

@my_login
def index5(request):

    return render(request, 'index5.html')

@my_login
def home(request):
    link = sshv1.sshdev('192.168.0.105',22,'root','root')


    return render(request, 'home.html',locals())
