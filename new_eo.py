# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 20:20:46 2019
Description: check a number if it is odd or even.
version:python 3.7
Testcases- varified with
  even number-->tested-->OK
  odd number-->tested-->OK
  negative number-->tested-->OK
  float number-->tested-->NOT OK
  string input-->tested-->NOT OK
Initial Static Code Analysis Score - 5/10
Final Static Code Analysis Score - 8.75/10

@author: sadiaafrini
"""
try:
    while True:
        VALUE = int(input("Enter a number: "))
        if(VALUE % 2) == 0:
            print(VALUE, " is even.")
        else:
            print(VALUE, " is odd.")
except ValueError:
    print('Please try an int number')       
                 