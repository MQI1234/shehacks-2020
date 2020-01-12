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

options = ["1. add an item!", "2. search for an item", "3. browse your closet", "4. view statistics", "5. terminate me"]
closet = [] #append clothes to this 


class Garb: #most basic info for each piece of clothing
    global closet
    
    def __init__(self, price, cat, date): #figure out obj types
        
        self.price = price
        self.cat = cat
        self.date = date
        self.worn = 0 #default for new purchases
        
    def getInfo(self): #summary of all factors

        print(f"you paid ${self.price} for this {self.cat} on {self.date}.")
        
    def wear(self): #each time clothing used

        self.worn += 1 #default, might include user input

    def per(self): #price per wear

        if self.worn == 0:
            return "Item has not been used yet, please come back when you wear it! :)"
        return round((self.price/self.worn), 2) #decimal standard for dollar amt


def addGarb():
    global closet

    running = True
    while running:
        
        #for now I'm just assuming the user formats everything legally
        print("How much did this item cost?\n")
        p = float(input())
        print("What type of clothing is this?\n")
        c = str(input())
        print("When did you buy this item?" + "(DD/MM/YYYY)\n") #add option for "today" in system time???
        d = str(input())
        closet.append(Garb(p, c, d)) #adds new item to master closet
        
        print("Would you like to add another item? (y/n) \n")
        choice = str(input())
        if choice == "y":
            print("OK, no problem!\n")
        elif choice == "n":
            print("Alright, back to main menu.\n")
            running = False
    

print("=====WELCOME TO YOUR VIRTUAL CLOSET=====\n")
"short introduction/mission statement I guess"

#menu loop

while True:
    
    print(*options, sep = "\n")
    choice = str(input())

    #integrate into GUI later
    if choice == "1": #adding items to closet
       addGarb() 
        
    elif choice == "2": #searching for an item
        print("I'm sorry, that function has not been completed yet. Please try again later!\n")

    elif choice == "3":
        if len(closet) != 0:
            for c in closet:
                c.getInfo()
        
    elif choice == "4": #statistics and other fun stuff
        print("I'm sorry, that function has not been completed yet. Please try again later!\n")

    elif choice == "5": #end the application
        print("So sad to see you go...Update me next time! :)))\n")
        quit()
    
    else: #improper input
        print("I'm sorry, that didn't make sense. Please enter a proper option.\n")
    
    
        
    

    
