# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 01:37:08 2021

@author: Serg
"""


class Converter:
    def __init__(self, value, back_value=None,default=None):
        self.value = value
        self.back_valuev = back_value
        self.default=default 

   
        
    def to_int(self):
        if self.value.isdigit():
            try:
    
                back_valuev=int(self.value)
                print(back_valuev)
                return(back_valuev)
            except (TypeError ,ValueError):
                print(self.default)
            
        else:
                print(self.default)
    
    def to_list(self):
        try:
    
            back_valuev=list(self.value)
            print(back_valuev)
            return(back_valuev)
        except (TypeError ,ValueError):
                print(self.default)
    
    def to_string(self):
        back_valuev=str(self.value)
        print(back_valuev)
        return(back_valuev)
        


c1 = Converter("2")

c1.to_int() # вернет 2 как int
c1.to_list() # вернет ["2"]
c1.to_string()  # вернет "2"


c2 = Converter("A")
c2.to_int() 
# вернет None, так как нельзя конвертировать и не задано значение по умолчанию


c3 = Converter("A", default="Can't convert")
c3.to_int() # вернет "Can't convert"
