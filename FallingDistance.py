################################################
## Program name: FallingDistance.py

# Author: Logan Carr
# Course: Python Essentials
# Date 11/20/2021
# Assignment: Module 4 - Falling Distance
#####Purpose: When an object is falling from
####gravity, the following forumla can be used 
###to determine the distance the object falls
##in a specific time period:
################################################




# Falling distance = 1/2 * gt^2

# Gravitional acceleration
Gravity  = 9.8

def fallingDistance(time):
    distance = (1/2) * Gravity * time **2
    return distance

#Intro
print('This program tells you how far an object will fall in a number of seconds.')
#Input
time = int(input('Enter the falling time in seconds: '))



print('Number of seconds: ', '\t Falling distance:')
print('- - - - - - - - - - - - - - - - - - - - -')

for seconds in range(0, time+5, 5):
    distance_of_falling = fallingDistance(seconds)
    print('{} seconds '.format(seconds), '\tYou fell {:.1f} meters'.format(distance_of_falling),
    sep='\t')


    ### For an infinite loop add the following
    # while time > 0:
    # print('The distance the object will fall in', time, 'seconds is:', fallingDistance(time), '\n')
    # time = int(input('Enter the falling time in seconds: '))
    ###
    
    