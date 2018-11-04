#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 09:51:50 2018

@author: nikhilkonijeti
"""

from bs4 import BeautifulSoup
import urllib2

list=['visakhapatnam','hyderabad']
roc=[]
for k in range(0,len(list)):
    url="https://www.pickmyphotographer.com/" + list[k] + "/wedding-photography"
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    data = opener.open(url).read()

    foc=[]
    hoc=[]
    soup=BeautifulSoup(data)
    
    for strong_tag in soup.find_all('h2', class_="profile-title"):
        foc.append(strong_tag.text)

    for i in range(0,len(foc)):
        foc[i]=foc[i].replace(" ","-")    
        foc[i]=foc[i].replace("'", "")
    
    url1="https://www.pickmyphotographer.com/" + list[k] + "/"
    main_url=[]
    
    for i in range(0,len(foc)):    
        main_url.append(url1 + foc[i] + "#profile-reviews")
        data1 = opener.open(main_url[i]).read()
        soup1=BeautifulSoup(data1)    
        for strong_tag1 in soup1.find_all('span', itemprop="streetAddress"):
            hoc.append(strong_tag1.text)
        for strong_tag1 in soup1.find_all('span', class_="user",itemprop="author"):
            roc.append(strong_tag1.text + " from " + foc[i] + " in " + hoc[i] + list[k] )