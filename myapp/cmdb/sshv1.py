# -*- coding: utf-8 -*-
import paramiko
import os
import select
import sys




def sshlink(hostname,port,username,password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port, username, password,timeout = 5)
        link = True
        return link
    except:
        link = False
        return link

def sshdev(hostname,port,username,password):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port, username, password,timeout = 5)
    stdin, stdout, stderr = ssh.exec_command('top -bn 1 -i -c | grep -n Cpu')
    cpu = stdout.read().decode() 

    stdin, stdout, stderr = ssh.exec_command('free | grep -n Mem')
    mem = stdout.read().decode()

    stdin, stdout, stderr = ssh.exec_command('df -B 1m | grep -v 文件系统')
    dist =stdout.read().decode()
#    dist_1 =dist.split('\n')
    count = len(dist.split('\n'))
    dist2 = 0
    dist3 = 0
    i = 0 
    while (i < (count-1)):
        dist_1 = dist.split('\n')[i]
        off = dist_1.split( )[3]
        on = dist_1.split( )[2]
        dist2 = dist2 + int(off)
        dist3 = dist3 + int(on)
        i = i + 1
#    return dist2
#    return dist3
   
    stdin, stdout, stderr = ssh.exec_command('cat /proc/cpuinfo | grep -n "model name"')
    cpu_1 =stdout.read().decode()    
    cpu_v = cpu_1.split( )[5]

    stdin, stdout, stderr = ssh.exec_command('lspci | egrep -ci "network|ethernet"')
    net =stdout.read().decode()
    network = net.split('\n')[0]
  
    stdin, stdout, stderr = ssh.exec_command('cat /etc/redhat-release')
    os_1 =stdout.read().decode()
    os_v = os_1.split( )[0] + os_1.split( )[3]      

    
    cpu_off = cpu.split( )[3]
    cpu_on = cpu.split( )[7]
    mem_off = mem.split( )[2]
    mem_on = mem.split( )[3]    
    dist_off = dist2
    dist_on = dist3
    
    list = [cpu_off,cpu_on,mem_off,mem_on,dist_off,dist_on,cpu_v,network,os_v]
    return list
    ssh.close()





