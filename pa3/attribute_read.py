# -*- coding: utf-8 -*-
"""
Created on Tue May 11 14:43:13 2021

@author: Lenovo
"""

import pandas as pd
import ast
import math

def isnan(value):
  try:
      return math.isnan(float(value))
  except:
      return False
  
    
if __name__ == '__main__':
    file_path = 'data/business.csv'
    bussiness = pd.read_csv(file_path)
    print(bussiness["attributes"])
    for i,dict_str in enumerate(bussiness["attributes"]):
        # check for nan
        if(isnan(dict_str)):
            print(f'line {i+1} has nan index')
            print('**'*20)
            print(dict_str)
        else:
            dict_str = dict_str.replace('"','')
            temp_dict = ast.literal_eval(dict_str)
            #### put your own code here
            



