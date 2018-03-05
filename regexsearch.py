#! python3
import os,re,tryagain
"""
Created on Tue Mar  6 00:12:01 2018

@author: Andy Poon
"""

def regexSearch(userinput):
    
    
    regsearch=re.compile(userinput)
    
    path="C:/Users/Andy/Documents/Coding stuff/Projects/"
    file_list=os.listdir(path)
    
    for file in file_list:
        if not file.endswith('.txt'):continue
        with open(file,'r') as f:
            
            print("Search results within: "+file)
            for line in f:
                if regsearch.search(line)==None:continue
                print((str(' '.join(regsearch.findall(line)))))

if __name__=="__main__":
    while True:
        
        expression=input("Input a regular expression: ")
        regexSearch(expression)
        
        if tryagain.loop()==True:
            continue
        else:
            break


    
