"""
A counting program to help with shiny hunting in Pokemon
A shiny is a rare version of a pokemon whose rate of encounter
is really low
"""

from datetime import *
import os
import sys
from pokemon import *

def menu():
    """
    function that prints out a menu that the user will select from
    """

    print("(0) Quit")
    print("(1) Display list of shiny pokemon caught")
    print("(2) Start a new shiny hunt")
    print("(3) Mark hunt as complete")

def getChoice():
    """
    Function that gets user input, validates, and returns a number corresponding
    to their choice
    """

    menu()
    choice = input("Please choose one of the above options: ")
    while not choice.isdigit() or int(choice) < 0 or int(choice) > 3:
        menu()
        choice = input("Please choose one of the above options: ")
    choice = int(choice)  
    return choice

def new():
    """ 
    Function that creates a new Pokemon object representing a new shiny hunt
    Returns the Pokemon object
    """

    pokemon = input("What pokemon are you hunting for? ")
    while pokemon.isdigit():
        pokemon = input("What pokemon are you hunting for? ")

    date = datetime.now()

    encounter = input("How many encounters do you have so far? ")
    if not encounter.isdigit() or int(encounter) < 0:
        encounter = input("How many encounters do you have so far? ")
    encounter = int(encounter)

    game = input("In which game are you hunting %s? " % (pokemon))

    newPokemon = Pokemon(pokemon, date, game)
    if not encounter == 0:
        newPokemon.setEncounter(encounter)

    probability = 1 - (4095/4096)**(encounter + 1)#of getting a shiny on the next encounter 
    newPokemon.setProbability(probability)

    return newPokemon

def updateHunt(data):
    """
    Function that marks a hunt as finished
    Parameter: data -> Data of Pokemon Objects representing shiny hunts
    """

    for i in range(len(data)):
        data[i].optionCreate(i)

    choice = input("Which shiny hunt would you like to mark as complete? ")
    while not choice.isdigit() or int(choice) < 0 or int(choice) >= len(data):
        choice = input("Which shiny hunt would you like to mark as complete? ")
    choice = int(choice)

    if data[choice].getDateEnd() == "In progress...":
        data[choice].setDate(datetime.now())
        data[choice].setProbability(1 - 4095/4096**data[choice].getEncounter())
    else:
        print("That shiny hunt is already completed!")

def load():
    """
    Function that loads data from file of pokemon
    returns a list of objects representing pokemon
    """

    file = open(os.path.join(sys.path[0], "shinies.txt"), "r")
    data = []
    for line in file:
        temp = line.strip().split(";;")
        data.append(Pokemon(temp[0],temp[1],temp[-1]))
        data[-1].setDate(temp[2])
        data[-1].setEncounter(int(temp[3]))
        data[-1].setProbability(float(temp[4]))
    file.close()
    return data

def saveHunt(data):
    """
    Function that saves newly created shiny hunts into data file
    Parameter: fileName -> string name of file where shiny hunts are stored
    Parameter: data -> list of Pokemon objects to be saved
    count: Count -> integer number of new objects created since last save
    """

    file = open(os.path.join(sys.path[0], "shinies.txt"), "w")
    for i in range(len(data)):
        file.write("%s;;%s;;%s;;%d;;%f;;%s\n" % (data[i].getName(), data[i].getDateStart(), data[i].getDateEnd(), data[i].getEncounter(), data[i].getProbability(), data[i].getGame()))
    file.close()

def main():

    choice = 1
    data = load()
    newPokemon = None

    while choice:
        choice = getChoice()
        if choice == 1: #displays list of hunts
            for i in range(len(data)):
                print (data[i])
        elif choice == 2: #create new hunt
            newPokemon = new()
            data.append(newPokemon)
        elif choice == 3:
            updateHunt(data)

    saveHunt(data)

main()