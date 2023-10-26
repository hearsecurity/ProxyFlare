#!/usr/bin/python

import httplib
import sys
import concurrent.futures
from colorama import Fore, Back, Style
import socket

paths = []

def main_function(path):
    
    path = path.strip('\n')
    url = sys.argv[1]
    url = path+"."+url 
    
    print "Trying: "+url

    c = httplib.HTTPSConnection(url)
    c.request("GET", "")
    r = c.getresponse()
    
    print r.status

    if r.status == 200 or r.status == 301 or r.status == 302:

      ip_address = socket.gethostbyname(url)

      if "104" not in ip_address:
        print("[FOUND]: "+url+" IP: "+ip_address)
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

print("\n")
with concurrent.futures.ThreadPoolExecutor(max_workers = 25) as executor:
    executor.map(main_function, paths)


