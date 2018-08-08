#Author: Christopher Bond
#Email: CKBO222@g.uky.edu
#Date: October 27, 2017
#Section: 401
#Pre-conditions: The user will give an angle and initial velocity when prompted
#                  by the program.  As well as the level of difficulty and 
#                  number of rounds that they want to play.  These inputs will
#                  used to try to hit a pig at a random distance between 100 and
#                  150 meters.
               
#Post-conditions:  The program will determine and output the number of pigs that
#                  were hit with the given inputs. 

#Purpose: To make a game similar to angry birds, where you launch birds 
#         and hit pigs.

from math import *
from random import *
def main():
#    Pre-Conditions: Inputs by the user will be given for angle, velocity, 
#                    difficulty, and rounds played .
#    Post-Conditions: The number of times the pig was hit will be calculated
#                     and displayed.
#    Purpose: To make a game similar to angry birds.    
    
    #seed function
    seed(25)

#Print the introduction
    
    print('\nAngry Birds!')
    print('Bird is at the left edge of the screen.')
    print('Pig is at the right edge of the screen.')
    print('Enter angle and velocity to catapult the bird and make it land',end='')
    print(' on the pig\n')
    
#get the input for the number of rounds
    rounds = int(input('How many rounds do you want to play? '))
    
#get the input for the level of difficulty
    diff = int(input('Level of difficulty? (smaller is harder) '))

    #create the variable for the number of times the pig was hit.  It will be 
    #used in the loop.
    pig_hits = 0

#create the for loop that will last for however many rounds the user chose.

    for i in range(1, rounds + 1):
        
        #create the random pig distance
        
        pig_distance = randint(100, 150)        
        
        #Create the outputs
        print('\nRound #', i)
        print('The pig is', pig_distance, 'meters away')
        angle = float(input('What angle? '))
        velocity = float(input('Initial velocity? '))   
        
        #Convert degrees to radians
        
        angle = radians(angle)
        
        #create the distance formula and round it
        distance = ((velocity**2) * sin(2 * angle)) / 9.8
        distance = round(distance)
            
        #create the height formula and round it.       
        height = ((velocity**2) * (sin(angle)**2)) / (2 * 9.8) 
        height = round(height)
        
        
        #prince the distance flown and height reached.
        print('\nThe bird flew', distance, 'meters')
        print('and reached a height of', height, 'meters')
        
        #create the formula that determines whether or not the pig was hit
        if pig_distance - diff <= distance <= pig_distance + diff:
            print('you got the pig!')
            pig_hits += 1
            
        else:
            print('you missed')
   
    #These if statements will print out a specific statement depending on the 
    #amount of pig hits.
    if pig_hits == 1:
        print('you got one pig')
            
    if pig_hits == 0:
        print('You got none!')
            
    if pig_hits >= 2:
        print('you hit the pig', pig_hits, 'times')
            
        
main()    