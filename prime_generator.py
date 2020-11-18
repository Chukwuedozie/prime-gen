# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 17:11:50 2020

@author: Dozie
"""

def prime_generator(n):
      
            prime=[]
            for x in range(1,n +1):
                  for y in range(2,x):
                        if x%y == 0: 
                              break
                  else:
                        prime.append(x)
            return prime
print(prime_generator(10))
                     
                              
                              
                              
                        
      
            
                  
      

