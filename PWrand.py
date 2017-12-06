#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#Developed by Omar [I] Sharki

from random import choice
import sys

def help():
    print ("\n [+] Developed by: Omar [I] Sharki.")
    print (" [-] Usage: PWrand <int>\n" )

def PWrand(insert_by_user):
    chars = 'ABCDEFGHIJKLMNOPQRSTUWXYZabcdefghijklmnopqrstuwxyz0123456789!@#~%&/()='
    GetPW = ''
    for password in range(insert_by_user):
        GetPW += (choice(chars))
    return GetPW
 #Command Line

if __name__ == '__main__':

    if len(sys.argv) is not 2:
        help()

    else:
        try:
            insert_by_user = int(sys.argv[1])
            print ("\n [+] Here's your password: " + PWrand(insert_by_user) + "\n")
        except ValueError:
            print ("\n [-] Error: The argument must be an Integer, Example: 10.\n")
