#an attempt

from datetime import datetime

"""
CONSIDER

representing types of clothing
=================
append into array and track that way? 

[subject to change]
multiples in each category?
top (short, long, casual, dressy)
bottom (shorts, pants, skirts)
shoe (sneaker, boot, heel, sandal)
accessory (hat, jewellery, glasses, bag)

adding date components 

"""

class Garb: #most basic info for each piece of clothing

    def _init_(self, price, cat, date): #figure out obj types
        
        self.price = price
        self.cat = cat
        self.date = date
        self.worn = 0 #default for new purchases
        
    def wear(self): #each time clothing used

        self.worn += 1 #default, might include user input

    def per(self): #price per wear

        if self.worn == 0:
            return "Item has not been used yet, please come back when you wear it! :)"

        return round((self.price/self.worn), 2) #decimal standard for dollar amt

        
    

    
