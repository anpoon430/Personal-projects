#! python3
import re
import sys
'''

'''
# and and r'[a-z]+'
def passwordDetection(password):
    passwordRegex=re.compile(r'\w{8}'and r'\d+')# check for 8 char length and atleast 1 digit
    mo=passwordRegex.search(password)

    if mo!=None:
        passwordRegex2=re.compile(r'[A-Z]+')#Check for atleast 1 uppercase letter
        mo2=passwordRegex2.search(password)
        if mo2!=None:
            passwordRegex3=re.compile(r'[a-z]+')#Check for atleast 1 lowercase letter
            mo3=passwordRegex3.search(password)
            if mo3!=None:
                print("Your password is strong")
                sys.stdout.flush()
    if mo==None or mo2==None or mo3==None:     #If conditions aren't met let user know 
        print('''Your password can be improved:
                 1.Minimum 8 characters in length (including symbols)
                 2.Atleast 1 number
                 3.Atleast 1 uppercase letter
                 4.Atleast 1 lowercase letter
            ''')
        sys.stdout.flush()


if __name__=='__main__':
    while True:
        password=input("Please enter a password to be validated: ")
        passwordDetection(password)
        while True:
            try:
                tryagain=str(input("Try again (Y/N)?: "))
                if tryagain=='Y'or tryagain=='y':
                    break
                elif tryagain=='N'or tryagain=='n':
                    break
                else:
                    raise ValueError
                    print("Unaccepted input")
                    sys.stdout.flush()
            except ValueError:
                continue
        if tryagain=='Y'or tryagain=='y':
            continue
        elif tryagain=='N'or tryagain=='n':
            break
        
    
