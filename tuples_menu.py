# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 16:11:59 2021

@author: kevcodes
"""

tuple1 = ()
def Makea_Change():
        tuple2 = ("red", "blue", "green", "black", "yellow", "pink")
        color = 3
        
        while color != -1:
            color = int(input("Choose a color; 1 = silver, 2 = purple, 3 = gold, 4 = white (-1 to quit) :"))
            
            if color == 1:
                y = list(tuple2)
                y.append("silver")
                tuple2 = tuple(y)
                print("The updated list is: ", tuple2)
            elif color == 2:
                 y = list(tuple2)
                 y.append("purple")
                 tuple2 = tuple(y)
                 print("The updated list is: ", tuple2)
            elif color == 3:
                 y = list(tuple2)
                 y.append("gold")
                 tuple2 = tuple(y)
                 print("The updated list is: ", tuple2)
            elif color == 4:
                 y = list(tuple2)
                 y.append("white")
                 tuple2 = tuple(y)
                 print("The updated list is: ", tuple2)
    
def printlist():
    tuple2 = ("red", "blue", "green", "black", "yellow", "pink")
    print(tuple2)
    
def delete_element():
    tuple2 = ("red", "blue", "green", "black", "yellow", "pink")
    print(tuple2) 
    choice = int(input("Select what colors you want to remove(1 = red, 2 = blue, 3 = green, 4 = black, 5 = yellow and 6 = pink "))
    if choice == 1:
                y = list(tuple2)
                y.remove("red")
                tuple2 = tuple(y)
                print("The updated list is: ", tuple2)
                
    elif choice == 2:
                y = list(tuple2)
                y.remove("blue")
                tuple2 = tuple(y)
                print("The updated list is: ", tuple2)
                
    elif choice == 3:
                y = list(tuple2)
                y.remove("green")
                tuple2 = tuple(y)
                print("The updated list is: ", tuple2)
                
    elif choice == 4:
                y = list(tuple2)
                y.remove("black")
                tuple2 = tuple(y)
                print("The updated list is: ", tuple2)
                
    elif choice == 5:
                y = list(tuple2)
                y.remove("yellow")
                tuple2 = tuple(y)
                print("The updated list is: ", tuple2)

    elif choice == 6:
                y = list(tuple2)
                y.remove("pink")
                tuple2 = tuple(y)
                print("The updated list is: ", tuple2)

            
def listmenu():
        print("\n\n")
        print("1: Add to the list")
        print("2: Print list")
        print("3: Delete an element")
        print("9 to exit")
        choice = int(input("Pick a number: "))
        return choice
    

ch = 2
while (ch != 9):
    ch = listmenu()
    if ch == 1:
            tuple1 = Makea_Change()
    elif ch == 2:
            printlist()
    elif ch == 3:
            delete_element()
    


