# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:00:42 2017

@author: tahereh
"""
#%%
import random
dic= {"1":1 , "2":1 , "3" : 1}

def solver_function(dic):
    
    
    
    print(dic)
    which=random.choice([1,2,3])
    
    print("which: ", which)
    if which ==1:
        
        a1= str(which)
        total_list=[1,2,3,4,5,6]
        total_list.remove(dic["1"])
        print("total_list: ",total_list)
        c1=random.choice(total_list)
        dic[a1]=c1
                
    if which==2:
        a2=str(which)
        if dic[a2]==dic["1"]:
            print(" 2 go to :")
            return solver_function(dic)
        else:
            total_list=[1,2,3,4,5,6]
            print("total_list: ",total_list)
            total_list.remove(dic["1"])
            total_list.remove(dic["2"])
            print("choice_list: ",total_list)
            c2=random.choice(total_list)
            print("c2",c2)
            dic[a2]=c2
            print("dic[",a2,"]: ",dic[a2])
    if which==3:
        
        
        a3=str(which)
        if dic[a3]==dic["1"] or dic[a3]==dic["2"]:
            
            print("3 go to :")
            return solver_function(dic)
        else:
            
            
            
               
            total_list=[1,2,3,4,5,6]
            print("total_list: ",total_list)
            if dic["1"]==dic["2"]:
                
                total_list.remove(dic["1"])
                total_list.remove(dic["3"])
            else:
                
                total_list.remove(dic["1"])
                total_list.remove(dic["2"])
                total_list.remove(dic["3"])
                    
                    
                
        print("choice_list: ",total_list)
        c3=random.choice(total_list)
        print("c3",c3)
        dic[a3]=c3
        print("dic[",a3,"]: ",dic[a3])
                
                 
                         
              
    print("dic: ",dic) 
    return dic


        
#%%
   
#%%
def solve():
    dic1= {"1":1 , "2":1 , "3" : 1} 
 
    for i in range(1,21):
        new_dic=solver_function(dic1)
        print("i= ",i)
        print("new_dic= ", new_dic)
        dic1=new_dic
        dic[i]=new_dic
        print("dic[",i,"]",dic[i])
    #%%
    solve()
#%%
def stan_dev():
    
    dic1= {"1":1 , "2":1 , "3" : 1} 
 
    for i in range(1,21):
        new_dic=solver_function(dic1)
        print("i= ",i)
        print("new_dic= ", new_dic)
        dic1=new_dic
        dic[i]=new_dic
        print("dic[",i,"]",dic[i])
        
    for i in range(1,21):
        print("dic[",i,"]",dic[i])
        
  #%%     
    
        
            
            
        
      
        
#%%
  
    
        
    
    
        
        

        