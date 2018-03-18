"""
Created on Sat Mar 10 23:36:40 2018

This program scrapes jobsdb.com for job listings.
It gathers all the links on each page to each posting,
then scrapes each listing for all the relevant information and
stores it in a dictionary. Finally, a CSV file containing the date,
title, company name, company information and job posting details
(responsibilities and requirements) is outputted.

@author: Andy Poon
"""
import requests,os,bs4,time,csv

def page(page_url):
    '''
    This function receives a the url of the main job listings page.
    then it loops through the page collecting a list of all the job postings links.
    After collecting the links it loops through each job posting link and writes the
    data into a CSV file as 1 row of data. This function repeats this for every link
    on the main page.
    '''
    
    headers={'user-agent':'''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'''
            }
    res=requests.get(page_url,headers=headers,timeout=10)
    res.raise_for_status()
    linkSoup=bs4.BeautifulSoup(res.text,"html.parser")
    
    #get the links to each job posting from the main page    
    linkElems=linkSoup.select('.job-title a')
        
    print("Scraping job listings for: "+str(page_url))#prints the current page url it is scraping
    links=list()  
    
    for link in linkElems:
        links.append(link.get('href'))#accumulated list of all job posting links
    data=dict()
    
    
    
    for e in links:  #loops through each job listing and writes data into csv file

        res=requests.get(e,headers=headers,timeout=10)
        res.raise_for_status()
    
        soup=bs4.BeautifulSoup(res.text,"html.parser")
        
        
        data['url']=data.get('url',e)
#these if statements checks each tag if it exists
#jobsDB has listings that sometimes have no company name, etc. so I have added
#if statements to check for each tag that I am searching for to avoid an error
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

def looppages(current_page,number_of_pages):
    '''
    Receives a url of the main listings page, which is the first page to be looped
    This function calls the page() function defined above for each page and loops
    through all the pages
    '''
    pagecount=0
    
    while pagecount<number_of_pages: # total number of pages
        
        page(current_page)
        
        print('Page '+str(pagecount+1)+' done') #pagecount starts at 0 so need +1 before this statement
        pagecount=pagecount+1
        next_page=current_page[:-1]+str(pagecount)#strip lastnum of url and replace with new url
        current_page=next_page
     
    
if __name__=='__main__':
    start=time.clock()
    
    job_page="https://hk.jobsdb.com/hk/jobs/entry-level?AD=30&Blind=1&Career=4&Host=J%2cS&JSRV=1&Key=data&KeyOpt=COMPLEX&SearchFields=Positions%2cCompanies&page=0"
    totalpages=input('How many pages?')
    
    original_path=os.getcwd()
    #set your path for output of the CSV file
    target_path=r"C:\Users\Andy\Documents\Coding stuff\Projects"
    os.chdir(target_path)
    
    looppages(job_page,totalpages)    
    path=os.chdir(original_path)
    
    print('finished')
    
    print('Time elapsed: '+str(time.clock()-start)+' seconds')
    
    
    