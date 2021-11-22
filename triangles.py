######################################################
# Program name: Triangles.py

# Author: Logan Carr
# Course: Python Essentials
# Date 11/14/2021
# Assignment: Module 3 - Distance Traveled
# Purpose: Determine Type of Triangle from user input
#######################################################


#Enter sides of triangle for floating input

print('Hello. This program accepts 3 separate values for triangles and then informs you of the results.\nPlease press "Enter" to continue')
input()
side1 = float(input('Please enter the length of the first side: '))
side2 = float(input('Please enter the length of the second side: '))
side3 = float(input('Please enter the length of the third and final side for the triangle: '))


#Turns the sides into a list
TriList = [side1,side2,side3]

#This sorts the list that was made, Descending order
TriList.sort()

side1=TriList[2]
side2=TriList[1]
side3=TriList[0]

if side1 <= 0 or side2 <= 0 or side3 <= 0:
    print('Entries of 0 or less than are not valid...\n Please try again')
### I was trying to immediately display an error when anything =< 0 was entered so more inputs were not necessary 
##elif side2 <= 0:
##   ('Entries of 0 or less than are not valid...\n Please try again')
    
##elif side3 <= 0 :
##   print('Entries of 0 or less than are not valid...\nPlease try again')

elif (side1**2)==(side3**2)+(side2**2):
    print("These inputs form a triangle! A Right Triangle.")

elif side1 == side2 and side1 == side3 and side2 == side3:
    print("These inputs form a triangle! An Equilateral Triangle!")

elif side1 == side2 or side1 == side3:
	print("These inputs form a triangle! An Isosceles Triangle!")

else: 
	print('This is not a: "Right Triangle, Equalateral Triangle, or an Isosceles Triangle...')
    
    
input('Press any key to continue')
