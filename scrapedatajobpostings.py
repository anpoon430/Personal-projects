"""
Created on Sat Mar 10 23:36:40 2018

@author: test
"""
import requests,sys,os,webbrowser,bs4,time

job_page="https://hk.jobsdb.com/hk/jobs/entry-level?KeyOpt=COMPLEX&JSRV=1&RLRSF=1&JobCat=1&SearchFields=Positions%2cCompanies&Key=data&Career=4&JSSRC=JSRAS&keepExtended=1"

headers={'user-agent':'''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'''
        }

res=requests.get(job_page,headers=headers,timeout=5)
res.raise_for_status()

linkSoup=bs4.BeautifulSoup(res.text,"lxml")

links=linkSoup.select('.job-title a')

for link in links:
    print(link.get('href'))



