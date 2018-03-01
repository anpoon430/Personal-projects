#! python3
import re,sys,tryagain
'''

'''
def passwordDetection(password):
    re1=re.compile(r'[^\n\r\f]{8}' )# check for 8 char length
    re2=re.compile(r'[A-Z]+')#Check for atleast 1 uppercase letter
    re3=re.compile(r'[a-z]+')#Check for atleast 1 lowercase letter
    re4=re.compile(r'(\d+)')#Check for atleast 1 number
     
    passwordregex=[re1,re2,re3,re4]
    mobjects=[]
    for regex in passwordregex:
        mobjects.append(regex.search(password))

    if all(e!=None for e in mobjects):
        print("Your password is strong")
        sys.stdout.flush()
    #If conditions aren't met let user know 
    else:    
        print('''Your password can be improved:
                 1.Minimum 8 characters in length (including symbols and whitespace)
                 2.Atleast 1 number
                 3.Atleast 1 uppercase letter
                 4.Atleast 1 lowercase letter
            ''')
        sys.stdout.flush()


if __name__=='__main__':
    while True:
        password=input("Please enter a password to be validated: ")
        passwordDetection(password)
        
        if tryagain.loop()==False:
            break
            if tryagain.loop()==True:
                continue
        
    
