# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 17:29:28 2018

@author: test
"""
import sys

def loop():
    while True:
        tryagain=input("Try again (Y/N)?: ")
        if tryagain=='Y'or tryagain=='y':
            return True
        elif tryagain=='N'or tryagain=='n':
            return False
        else:
            print("Unaccepted input")
            sys.stdout.flush()
            continue
if __name__=='__main__':
    loop()
    