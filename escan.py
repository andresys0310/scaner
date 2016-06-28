#!/usr/bin/python
 
import nmap
import time

nm = nmap.PortScanner()
host_scan = input('Host scan: ')
while host_scan == "":
    host_scan = input('Host scan: ')
anterior=list()
def escanear():
    global anterior
    nuevo=list()
    nm.scan(hosts=host_scan, arguments='-n -sP')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    for host, status in hosts_list:
        print (host, status)
        nuevo.append(host)
    if len(anterior) > 0 : #si no la primera vez que escanea
          for i in nuevo:
              sumatoria=0
              for j in anterior:
                  if str(i)== str(j):
                     sumatoria+=1
              #print("sumatoria :--"+str(sumatoria))
              if sumatoria==0:
                  print("Se ha conectado el host: "+str(i))
    anterior=nuevo
while True:
    escanear()
    time.sleep(7)
    

        

        
    
