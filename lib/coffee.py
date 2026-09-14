#!/usr/bin/env python3
sizes=["Small","Medium","Large"]
class Coffee:
    def __init__(self,size:str,price):
        self.size=size
        self.price=price
    @property
    def Size(self,size):
        if not isinstance(size,str):
            print("Must be a string")
        elif size not in sizes:
            print(f"Sizes must be either {sizes}")
        else:
            self.size=size
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price+=1