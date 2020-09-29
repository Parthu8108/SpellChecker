# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 19:15:01 2020

@author: prath
"""


from textblob import TextBlob    # importing textblob library

t = 1
while t:
    a = input("Enter the word to be checked:- ")	 # incorrect spelling
    print("original text: "+str(a))     #printing original text

    b = TextBlob(a)  #correcting the text

    # prints the corrected spelling
    print("corrected text: "+str(b.correct()))
    t = int(input("Try Again? 1 : 0 "))