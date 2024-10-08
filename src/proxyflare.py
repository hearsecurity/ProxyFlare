#!/usr/bin/python

import httplib
import sys
import concurrent.futures
from colorama import Fore
import socket
from time import sleep 


paths = []

def banner(): 

  print """                                                       
                             __ _                 
  _ __  _ __ _____  ___   _ / _| | __ _ _ __ ___  
 | '_ \| '__/ _ \ \/ / | | | |_| |/ _` | '__/ _ \ 
 | |_) | | | (_) >  <| |_| |  _| | (_| | | |  __/ 
 | .__/|_|  \___/_/\_\\__, |_| |_|\__,_|_|  \___| 
 |_|                  |___/                       

  """

def main_function(path):
    
    path = path.strip('\n')
    url = sys.argv[1]
    url = path+"."+url 
    
    url=url.replace('http://','')
    url=url.replace('https://','')
    url=url.replace('www.','')

    print "Trying: "+url 

    c = httplib.HTTPSConnection(url)
    c.request("GET", "")
    r = c.getresponse()

    if r.status == 200 or r.status == 301 or r.status == 302:
      ip_address = socket.gethostbyname(url)
      if "104" not in ip_address:
        print(Fore.GREEN+"[FOUND]: "+url+" IP: "+ip_address+Fore.WHITE)
        f = open("found.txt", "a")
        f.write(url+" IP: "+ip_address+"\n")
        f.close() 
    
def load_domains(domains):

  count = 0
  with open(domains) as file:
    lines = file.readlines()
    for line in lines:
      count = count + 1
      paths.append(line)


load_domains("subdomains.txt")

if len(sys.argv) < 2: 
  banner()
  print "  Usage: python2 proxyflare.py <domain>\n"
else:
  banner()
  print " [*] Wait a few seconds... \n"
  sleep(2)
  with concurrent.futures.ThreadPoolExecutor(max_workers = 25) as executor:
    executor.map(main_function, paths)


