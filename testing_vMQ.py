#an attempt
#testingvMQ.py
#Mengyu's version


#GUI functionality
from tkinter import *
from tkinter.ttk import *

from datetime import datetime

import pickle

"""
CONSIDER

representing types of clothing
=================
simple strings as names, linear search, no tagging

adding date components ???


catchy name:
===========
laundry list
Pydrobe
Worth the Wear/Ware
object-oriented outfitting
<start> New Thread
the conscious closet (tm)
tag: stretch the wear-time, not your budget


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
        #self.date = date
        self.worn = 0 #default for new purchases
        self.lastWorn = date #sauce in current date i guess
        
    def getInfo(self): #summary of all factors
        return (f"you paid ${self.price} for {self.cat} and last wore it on {self.lastWorn}.") #easier string formatting
        
    def wear(self): #each time clothing used
        self.worn += 1 
        curDate = datetime.date(datetime.now()) #uses real time date of update
        self.lastWorn = curDate #changes to new wear date

    def wearGap(day): #must pass in datetime obj
        wearGap = datetime.strptime(day, "%Y-%m-%d") - datetime.strptime(self.lastWorn, "%Y-%m-%d") 
        return wearGap.days #difference in whole day value

    def per(self): #price per wear
        if self.worn == 0:
            return "Item has not been used yet, please come back when you wear it! :)"
        return round((self.price/self.worn), 2) #decimal standard for dollar amt

def save_obj(obj, file): #closet data will be preserved in a file 
    with open(file, 'wb') as out:
        pickle.dump(obj, out, pickle.HIGHEST_PROTOCOL)
        
def addGarb():
    global closet
    while True:
        #for now I'm just assuming the user formats everything legally
        print("How much did this item cost?\n")
        p = float(input())
        print("What type of clothing is this?\n")
        c = str(input())
        print("When did you wear this item?" + "(YYYY-MM-DD)\n") #add option for "today" in system time???
        d = str(input())
        closet.append(Garb(p, c, datetime.strptime(d, "%Y-%m-%d"))) #adds new item to master closet
        
        print("Would you like to add another item? (y/n) \n")
        choice = str(input())
        if choice == "y":
            print("OK, no problem!\n")
        elif choice == "n":
            print("Alright, back to main menu?\n")
            input()
            break #ends loop 

def garbStats(ind): #statistics for a specific piece of clothing
    global closet
    item = closet[ind]
    return (item.wearGap, item.per) #days since last worn and cost/wear "efficiency" in a tuple

def search(term): #pass in user entry and compare to clothing names in closet
    global closet
    match = []
    for c in closet:
        if term in c.cat: #true if item name contains substring user enters
            match.append(c) 
    return match #array of possible matches to display

def browse(): #edit/update entries
    global closet
    if len(closet) != 0:
        for c in closet:
            print(str(closet.index(c) + 1), c.getInfo(), sep = ". ", end = "\n")
    while True:
        n = int(input())
        if n == -1: #"back button" to main menu
            break
        else:
            closet[n].wear() #"clicking wear button" at different places changes wore counter, lastWorn
        


print("=====WELCOME TO YOUR VIRTUAL CLOSET=====\n")
"short introduction/mission statement I guess"

with open('closet_data.pkl', 'rb') as inp: 
    closet = pickle.load(inp)

#menu loop

while True:
    
    print(*options, sep = "\n")
    choice = str(input())

    #integrate into GUI pls
    
    if choice == "1": #adding items to closet
       addGarb() 
        
    elif choice == "2": #searching for an item
        print("please enter the item you wish to search")
        for r in (search(str(input()))):
            print(r.cat) 
                        
    elif choice == "3": #display/browse whole closet
        browse() 
        print("Alright, back to main menu?\n")
        input() #enter to return to menu
        
    elif choice == "4": #statistics and other fun stuff
        print("I'm sorry, this function is only partially complete. Check back later!\n")
        #choice of specific garment OR general stats somehow, not yet
        print(garbStats(int(input())))
        
    elif choice == "5": #end the application
        print("So sad to see you go...Update me next time! :)))\n")

        break
    
    else: #improper input
        print("I'm sorry, that didn't make sense. Please enter a proper option.\n")
    

#IDEALLY: preserve and output the closet (data integrity between sessions) 
save_obj(closet, 'closet_data.pkl')
    
    

    
