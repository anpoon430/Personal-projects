#! python3
import os,re,sys,tryagain

"""
Created on Tue Mar  6 00:12:01 2018

@author: Andy Poon
"""

def regexSearch(userinput):
    
    
    regsearch=re.compile(userinput)
    
    path="C:/Users/Andy/Documents/Coding stuff/Projects/"
    file_list=os.listdir(path)
    txtf_list=[]
    
    
    
    
    for file in file_list:
        if not file.endswith('.txt'):continue
        fileobj=open(file,'r')
        for line in fileobj:
            
        txtf_list.append(fileobj)
        
    for obj in txtf_list:
        for line 
    
        

    
