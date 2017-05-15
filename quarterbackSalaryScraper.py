# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 18:37:11 2017
Quarterback Salary Scraper
@author: Ibrahim Taher
"""

from bs4 import BeautifulSoup
import requests
import csv
URL='http://www.spotrac.com/nfl/rankings/2015/cap-hit/quarterback/'

def getSectionPage(baseURL):
    response=requests.get(baseURL)
    html = response.text.encode('utf-8')
    return html

def getQuarterbackSalary(html):
    lst=[]    
    soup=BeautifulSoup(html,'html.parser')
    boxes = soup.select('tr')
    for box in boxes:
        qb=box.find("img")
        if qb==None:
            continue
        name=qb.get('alt')
        name=name.split(" ")
        name=name[0][0]+'.'+name[1]
        print(name)
        cap=box.find("span",{"class":"info","title":""})
        print(cap)
        if cap==None:
            cap=box.find("span",{"class":"info","title":"Injured Reserve"})
            print(cap)
            if cap==None:
                continue
        cap=cap.text
        cap=cap.replace('$','').replace(',','')
        cap=int(cap)
        print(cap)
        lst.append([name,cap])
    return lst
def main():
    f=open('qbcaps.csv','w',newline='')
    writer = csv.writer(f)
    writer.writerow(('Name','Cap'))
    html=getSectionPage(URL)
    qbcap=getQuarterbackSalary(html)
    writer.writerows(qbcap)


