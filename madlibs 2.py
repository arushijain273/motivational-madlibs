from tkinter import *
import datetime

name= input("Whats your name hun? ")
workVerb= input("What are you passionate about bub? ")
roleModel= input("Who do you look up to?" )
goodAdj= input("Gimme a good adjective :)" )

madlibs= f"Hey {name}, everything will be alright. You'll be back to your work of {workVerb}.\nYou're a genius. {roleModel} believes in you and so does this {goodAdj} programmer.\nYOU GOT THIS!!"
now= datetime.datetime.today()
print(madlibs)
print(now)