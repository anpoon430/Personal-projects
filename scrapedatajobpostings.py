"""
Created on Sat Mar 10 23:36:40 2018

@author: Andy Poon
"""
import requests,os,bs4,time,csv,copy,io
#from selenium import webdriver

def page(jobpage):
    headers={'user-agent':'''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'''
            }
    res=requests.get(job_page,headers=headers,timeout=5)
    res.raise_for_status()
    linkSoup=bs4.BeautifulSoup(res.text,"lxml")
    
    
    linkElems=linkSoup.select('.job-title a')
        
    print("Scraping job listings...")
    links=list()  #accumulated list of all job posting links
    
    for link in linkElems:
        links.append(link.get('href'))
    data=dict()
    #datalist=list()
    for e in links:

        res=requests.get(e,headers=headers,timeout=5)
        res.raise_for_status()
    
        soup=bs4.BeautifulSoup(res.text,"lxml")
        
        
        data['url']=data.get('url',e)
        
        if soup.find(itemprop='title')!=None:
            title=soup.find(itemprop='title').text
        else:
            title='N/A'
        data['title']=data.get('title',title)
        
        if soup.find(itemprop='hiringOrganization')!=None:    
            company=soup.find(itemprop='hiringOrganization').text
        else:
            company='N/A'
        data['company']=data.get('company',company)
        
        if soup.find(class_='primary-profile-detail')!=None:
            companyDetails=soup.find(class_='primary-profile-detail').text
        else:
            companyDetails='N/A'
        data['company info']=data.get('company info',companyDetails)
        
        if soup.find(itemprop='responsibilities',class_='jobad-primary-details')!=None:
            posting=soup.find(itemprop='responsibilities',class_='jobad-primary-details').text
        else:
            posting='N/A'
        data['posting']=data.get('posting',posting)
        
        #datalist.append(data.copy())
        
        #file=open('jobdata.csv','a', encoding= 'utf-9',newline='')
        file_exists=os.path.exists('jobdata.csv')
    
        with open('jobdata.csv','a', encoding= 'utf-8',newline='')as csvfile:
            keys=data.keys()
            writer=csv.DictWriter(csvfile,fieldnames=keys)
            if not file_exists:
                writer.writeheader()
            writer.writerow(data)
        
        data.clear()
        
        time.sleep(1)
    #return datalist

def looppages(job_page):
    headers={'user-agent':'''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'''
            }
    res=requests.get(job_page,headers=headers,timeout=5)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text,"lxml")
  
    pagecount=0

    #accumdatalist=list() 
    
    
    ### NOT OPENING NEW PAGE PROPERLY## 
    while soup.find(class_='CurrentPage'+str(pagecount+1))!=None: #check next page exists
        
        #print('datafromapage: '+str(datafromapage))
        #accumdatalist.extend(datafromapage)
        page(job_page)
        print('Page '+str(pagecount+1)+' done')
        pagecount=pagecount+1
        #job_page=soup.find(class_='CurrentPage'+str(pagecount)).get('href')##investigate
        joblinklist=soup.select('.CurrentPage'+str(pagecount)+' a')
        job_page=joblinklist[0].get('href')
        print(job_page)
    #return accumdatalist
    
if __name__=='__main__':
    job_page="https://hk.jobsdb.com/hk/jobs/entry-level?KeyOpt=COMPLEX&JSRV=1&RLRSF=1&JobCat=1&SearchFields=Positions%2cCompanies&Key=data&Career=4&JSSRC=JSRAS&keepExtended=1"
    #jobdata=looppages(job_page)
    
    #with open('jobdata.csv', 'w', newline='') as csvfile:
    #    keys=jobdata[0].keys()
    #    writer = csv.DictWriter(csvfile, fieldnames=keys)
    #    writer.writeheader()
    #    writer.writerows(jobdata)
    original_path=os.getcwd()
    target_path=r"C:\Users\Andy\Documents\Coding stuff\Projects"
    os.chdir(target_path)
    
    looppages(job_page)
    #print(page(job_page)[10])    
    
    print('finished')
    
    path=os.chdir(original_path)