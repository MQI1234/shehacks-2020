#an attempt
#testingvMQ.py
#Mengyu's version


from tkinter import *
from tkinter.ttk import *

from datetime import datetime 

"""
CONSIDER

representing types of clothing
=================
simple strings as names, linear search, no tagging

adding date components ???

"""

options = ["1. add an item!", "2. search for an item",
           "3. browse your closet", "4. view statistics",
           "5. terminate me"]

closet = [] #master list of all clothes


class Garb: #most basic info for each piece of clothing
    global closet
    
    def __init__(self, price, cat, date): #figure out obj types
        
        self.price = price
        self.cat = cat
        self.date = date
        self.worn = 0 #default for new purchases
        
    #def getCat(self):

        #return self.cat
    def getInfo(self): #summary of all factors

        return (f"you paid ${self.price} for {self.cat} on {self.date}.") #easier string formatting
        
    def wear(self): #each time clothing used

        self.worn += 1 #default, might include user input
        #get date, compare to next wear
        #alert if not worn for x amount of time

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
            print("Alright, back to main menu?\n")
            input()
            running = False

def garbStats(ind): #statistics for a specific piece of clothing
    global closet

    item = closet[ind]
    
    #how many times worn in past month/year?
    #cost/wear "efficiency"

def search(term): #pass in user entry and compare to clothing names in closet
    global closet

    match = []
    for c in closet:
        if term in c.cat: #true if item name contains substring user enters
            match.append(c) 
    return match #array of possible matches to display
    
    

print("=====WELCOME TO YOUR VIRTUAL CLOSET=====\n")
"short introduction/mission statement I guess"

#menu loop
running = True

while running:
    
    print(*options, sep = "\n")
    choice = str(input())

    #integrate into GUI later
    
    if choice == "1": #adding items to closet
       addGarb() 
        
    elif choice == "2": #searching for an item
        print("please enter the item you wish to search")
        for r in (search(str(input()))):
            print(r.cat) 
                        
    elif choice == "3":
        if len(closet) != 0:
            for c in closet:
                print(str(closet.index(c) + 1), c.getInfo(), sep = ". ", end = "\n")
        print("Alright, back to main menu?\n")
        input() #enter to return to menu
        
    elif choice == "4": #statistics and other fun stuff
        print("I'm sorry, that function has not been completed yet. Please try again later!\n")
        #choice of specific garment OR general stats
        #0 for overall stats, index for certain item

    elif choice == "5": #end the application
        print("So sad to see you go...Update me next time! :)))\n")
        running = False
    
    else: #improper input
        print("I'm sorry, that didn't make sense. Please enter a proper option.\n")
    
    
        
    

    
