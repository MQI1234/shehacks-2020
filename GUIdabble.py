
'''
An attempt at GUI 



References/ Credits
class, stack structure taken from
https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
'''



#GUI functionality
import tkinter as tk                
from tkinter import font  as tkfont

from datetime import datetime 

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
        self.lastWorn = datetime.date(datetime.now())
        
        
    def getInfo(self): #summary of all factors
        return (f"you paid ${self.price} for {self.cat} and last wore it on {self.lastWorn}.") #easier string formatting
        
    def wear(self): #each time clothing used
        self.worn += 1 
        curDate = datetime.date(datetime.now()) #uses real time date of update
        self.lastWorn = curDate #changes to new wear date

    def wearGap(self): #must pass in datetime obj
        wearGap = datetime.strptime(str(datetime.now()), "%Y-%m-%d") - datetime.strptime(str(self.lastWorn), "%Y-%m-%d") 
        return wearGap.days #difference in whole day value

    def per(self): #price per wear
        if self.worn == 0:
            return "Item has not been used yet, please come back when you wear it! :)"
        return round((self.price/self.worn), 2) #decimal standard for dollar amt


def addGarb(price, cat, date):
    if price== None or cat == None or date == None:
        return
    price = float(price)
    cat = str(cat)
    date=str(date)
    global closet
    closet.append(Garb(price, cat, date)) #adds new item to master closet
    return 


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
    return match

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
            closet[c].wear(n) #"clicking wear button" at different places changes wore counter, lastWorn
        
'''

print("=====WELCOME TO YOUR VIRTUAL CLOSET=====\n")
"short introduction/mission statement I guess"

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
        garbStats(int(input()))
        
    elif choice == "5": #end the application
        print("So sad to see you go...Update me next time! :)))\n")
        break
    
    else: #improper input
        print("I'm sorry, that didn't make sense. Please enter a proper option.\n")
    
    
'''       
    
class SampleApp(tk.Tk):
    global closet
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):

        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    global closet
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Conscious Closet", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        option1 = tk.Button(self, text="Add Item",
                            command=lambda: controller.show_frame("PageOne"))
        option2 = tk.Button(self, text="Search for an Item",
                            command=lambda: controller.show_frame("PageTwo"))
        option3 = tk.Button(self, text="Browse your Closet",
                            command=lambda: controller.show_frame("PageThree"))
#        option4 = tk.Button(self, text="View Statistics",
#                            command=lambda: controller.show_frame("PageFour"))
        option1.pack()
        option2.pack()
        option3.pack()
#        option4.pack()


class PageOne(tk.Frame):
    global closet
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        def clicked():
            addGarb(price.get(),category.get(),date.get())
            controller.show_frame("StartPage")
            
        priceLabel = tk.Label(self, text="Enter the price:", font=controller.title_font).pack()
        price = tk.Entry(self,width = 10)
        price.pack()
        
        catLabel = tk.Label(self, text="Enter the category:", font=controller.title_font).pack()
        category = tk.Entry(self,width = 10)
        category.pack()
        
        dateLabel = tk.Label(self, text="Enter the date purchased YYYY-MM-DD:", font=controller.title_font).pack()
        date = tk.Entry(self,width = 10)
        date.pack()
       # lastWornLabel = tk.Label(self, text="Enter the date last worn:", font=controller.title_font).pack()
      #  lastWorn = tk.Entry(self,width = 10).pack()
        
        button = tk.Button(self, text="add item",
                           command=clicked )
        button.pack()
        
        button1 = tk.Button(self, text="Go to main menu",
                           command=lambda: controller.show_frame("StartPage"))
        button1.pack()


class PageTwo(tk.Frame): #search
    global closet
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Search your closet", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        searchLabel = tk.Label(self, text="Type your search keyword:", font=controller.title_font).pack()
        term = tk.Entry(self,width = 10)
        term.pack()
        
        def clicked():
            if len(search(term.get()))==0:
                report = tk.Label(self, text="No Results!", font=controller.title_font).pack()
            else:
                for item in search(term.get()): #----------HELP need to format it so wont overlap
                    label = tk.Label(self, text=item.cat, font=controller.title_font).pack()
                    stats = tk.Label(self, text=(f"Total Wears: {item.worn}, Cost per Wear: {item.per()}/wear"), font=controller.title_font).pack()
               #controller.show_frame("StartPage")
        
        button1 = tk.Button(self, text="search",
                           command=clicked ).pack()
            
        button2 = tk.Button(self, text="Go to main menu",
                           command=lambda: controller.show_frame("StartPage")).pack()

class PageThree(tk.Frame): # Browse closet
    global closet
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Closet", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        def clicked():

            for item in closet: #----------HELP need to format it so wont overlap
                name = tk.Label(self, text=item.cat, font=controller.title_font).pack()
                stats = tk.Label(self, text=(f"Total Wears: {item.worn}, Cost per Wear: {item.per()}"), font=controller.title_font).pack()
                

        button1 = tk.Button(self, text="show items",
                           command=clicked ).pack()
            
        button = tk.Button(self, text="Go to main menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()


