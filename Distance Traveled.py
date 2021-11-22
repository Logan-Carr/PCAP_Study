###########################################
# Program name: Distance.py

# Author: Logan Carr
# Course: Python Essentials
# Date 11/14/2021
# Assignment: Module 3 - Distance Traveled
# Purpose: Determine Distance Traveled
###########################################

##Intro
print('Hello, this program takes the mph of your vehicle and\ndisplays the accumulative distance.')

##Empty input
input('Please press "Enter" if you wish to proceed...')

### Enter the speed of the traveling vehicle 

speed = int(input('Please enter the speed of the vehicle in mph:'))

time = int(input('How many hours has the vehicle traveled? '))


#### Can't figure out how to input validate correctly with a for loop
####if speed or time <1:
    ###print('You need to enter a positive value greater than 0')

###Takes the range adds 1, then speed * i = the  amount of hours and distance traveled

for i in range(1, time +1):
    distance = float(speed * i)
    print(i,'\t', distance)


input('Press "Enter" to exit...')
##print('The speed and/or hours has to a positive number and not 0...')    
##elif:
  #  for num in range(1, time+1):
   #     distance = num * mph
  #  print(
#     '''          
  #  Hour   Distance Traveled
   # ---------------------------- 
  #      1            
   #     2            (mph * 2)
    #    3            (mph * 3)      
        
    #
    #    ''')
    
