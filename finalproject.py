#Maya Griffith
#Python Final Project
#12/01/20

import time
import random
import threading

def main():
    play=False
    print("Welcome to the countries and capitals guessing game.")
    question=0;
    
    while play==False:
        choice = int(input("Press...\n1 <- to hear the rules\n2 <- to play with countries\n3 <-to play with states\n4 <- to quit\n"))
        if choice==1:
            play=True
            readrules()
        elif choice==2:
            question= int(input("Press...\n1 <- to guess the capital \n2 <- to guess the countries\n"))
            if question==1:
                capitals=loadcountries() #loads to guess the capitals
            elif question==2:
                capitals=loadcountrycaps()
            else:
                print("please choose a valid option")
            playgame(capitals, question)
            play=True
        elif choice==3:
            question= int(input("Press...\n1 <- to guess the capital \n2 <- to guess the states\n"))
            if question==1:
                question=3
                capitals=loadstates() #loads to guess the capitals
            elif question==2:
                question=4
                capitals=loadstatecaps()
            else:
                print("please choose a valid option")
            playgame(capitals, question)
            play=True
        elif choice==4:
            play=True
            print("see you next time!")
        else:
            print("Please pick a number")
    
                    

def loadcountries():
    capitals={}
    try:
        readfile= open("countriesandcaps.txt", "r")
    except IOError:
        print("could not open")
    line = readfile.readline()
    while line != "":
        clist = line.strip().rsplit("—")
        country=clist[0].rstrip()
        cap=clist[1].lstrip()
        capitals[country]=cap
        line=readfile.readline()
    return capitals

def loadcountrycaps():
    capitals={}
    try:
        readfile= open("countriesandcaps.txt", "r")
    except IOError:
        print("could not open")
    line = readfile.readline()
    while line != "":
        clist = line.strip().rsplit("—")
        cap=clist[0].rstrip()
        country=clist[1].lstrip()
        capitals[country]=cap
        line=readfile.readline()
    return capitals

def loadstates():

    capitals={}
    try:
        readfile= open("statesandcaps.txt", "r")
    except IOError:
        print("could not open")
    line = readfile.readline()
    while line != "":
        clist = line.strip().rsplit(",")
        state=clist[0].rstrip()
        cap=clist[1].lstrip()
        capitals[state]=cap
        line=readfile.readline()
    return capitals

def loadstatecaps():
    capitals={}
    try:
        readfile= open("statesandcaps.txt", "r")
    except IOError:
        print("could not open")
    line = readfile.readline()
    while line != "":
        clist = line.strip().rsplit(",")
        cap=clist[0].rstrip()
        state=clist[1].lstrip()
        capitals[state]=cap
        line=readfile.readline()
    return capitals


  
def readrules():
    print("Here are the rules:")
    print("A random place pops up, and you have to guess the country, state, or capital.")
    print('"help" for hints\n"quit" to quit\n"skip" to skip\n')
    print("Each hint costs 1 life")
    main()


def playgame(capitals, question):

    points=0

    incorrect_answers={}
    
    print ("Learning Capitals!\n")
    print('"help" for hints\n"quit" to quit\n"skip" to skip\n')

    quitit=0
   
        
    while len(capitals)>0 and quitit!=1:#while dictionary is not empty
            
        correct=False
       
        key = random.choice(list(capitals))
        value = capitals[key]
        del capitals[key]
        
        lives=3

        hints=3
        

        while correct==False and lives>=0:

            
            if question==1:    
                print ('Country:',key)
                answer=input("Capital: ")
            elif question==2:
                print ('Capital:',key)
                answer=input("Country: ")
            if question==3:    
                print ('State:',key)
                answer=input("Capital: ")
            elif question==4:
                print ('Capital:',key)
                answer=input("State: ")
            else:
                print("oops")
            
            if answer.lower().strip()==value.lower():
                print ("That's Correct!\n")
                points+=1
                correct=True
            elif answer.lower().strip() == "skip":
                incorrect_answers[key]=value
                correct=True
            elif answer.lower() == "help":
                length= len(value) #how many letters in correct capital
                if hints==3:
                    print("here is your hint!:\n")
                    word = "_ "
                    word=(word*(length-1))
                    word=value[0]+word
                    print(word)
                    hints-=1
                elif hints==2:
                    print("here is your hint!:\n")
                    word = "_ "
                    length-=2
                    word=(word*(length))
                    word=value[0]+word+value[length+1]
                    hints-=1
                    print(word)
                    
                elif hints==1:
                    print("here is your hint!:\n")
                    word = "_ "
                    length-=3
                    word=(word*(length))
                    word=value[0]+word[:int(length/2)]+value[int(length/2)]+word[int(length/2):]+value[length+2]
                    hints-=1
                    print(word)
                else:
                    print('Sorry, you have ran out of hints. type "skip"\n to find out capital if you have no more guesses.')
                
               
            elif answer.lower() == "quit":
                print("See you next time!")
                correct=True
                quitit=1
            else:
                print ("That's Incorrect.\n")
                lives-=1
                print("Lives:", lives)
                incorrect_answers[key]=value
                

        print ("The correct answer is",value, "\n")
            
                    
        print("**********************************************************************")


    print("All done!")
    reschoice=int(input("Would you like to see your results? 1 for yes and 2 for no.\n"))

    if reschoice==1:
        print("Points:", points)
        print("You need to study:")
        for key in incorrect_answers:
            print(key,',',incorrect_answers[key])
    elif reschoice==2:
        print("bye!<3")




main()
