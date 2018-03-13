"""
Created on Sat Mar 10 23:36:40 2018

@author: Andy Poon
"""
import requests,os,bs4,time,csv

def page(page_url):
    headers={'user-agent':'''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'''
            }
    res=requests.get(page_url,headers=headers,timeout=5)
    res.raise_for_status()
    linkSoup=bs4.BeautifulSoup(res.text,"html.parser")
    
    
    linkElems=linkSoup.select('.job-title a')
        
    print("Scraping job listings for: "+str(page_url))
    links=list()  #accumulated list of all job posting links
    
    for link in linkElems:
        links.append(link.get('href'))
    data=dict()
    
    for e in links:  #loops through each job listing and writes data into csv file

        res=requests.get(e,headers=headers,timeout=5)
        res.raise_for_status()
    
        soup=bs4.BeautifulSoup(res.text,"html.parser")
        
        
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
        
        if soup.find('meta',itemprop='datePosted')!=None:
            date=soup.find('meta',itemprop='datePosted').get('content')[:10]#extract date only, no time
        else:
            date='N/A'
        data['date']=data.get('date',date)
        
        file_exists=os.path.exists('jobdata.csv')
    
        with open('jobdata.csv','a', encoding= 'utf-8',newline='')as csvfile:
            fieldnames=['date','company','company info','title','posting','url']
            writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow(data)
        
        data.clear()
        time.sleep(1)
        
    
    #return datalist

def looppages(current_page):  
    pagecount=0
    
    while pagecount<5: # total number of pages=5
        
        page(current_page)
        
        print('Page '+str(pagecount+1)+' done') #pagecount starts at 0 so need +1 before this statement
        pagecount=pagecount+1
        next_page=current_page[:-1]+str(pagecount)#strip lastnum of url and replace with new url
        current_page=next_page
     
    
if __name__=='__main__':
    job_page="https://hk.jobsdb.com/hk/jobs/entry-level?AD=30&Blind=1&Career=4&Host=J%2cS&JobCat=1&JSRV=1&Key=data&KeyOpt=COMPLEX&SearchFields=Positions%2cCompanies&page=0"
    
    original_path=os.getcwd()
    target_path=r"C:\Users\Andy\Documents\Coding stuff\Projects"
    os.chdir(target_path)
    
    looppages(job_page)    
    
    print('finished')
    
    path=os.chdir(original_path)