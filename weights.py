name = input("Please enter your name: ")

## Ask for input of name

print('Hello', name)

## Hello , inputted name 

x = float(input('Please enter your weight: '))

## X Amount of user's weight

sun = round(x * 27.01, 2)
mercury = round(x * 0.38, 2)
venus = round(x * 0.91, 2)
earth = round(x * 1, 2)
moon = round(x * 0.166, 2)
mars = round(x * 0.38, 2)
jupiter = round(x * 2.34, 2)
saturn = round(x * 1.06, 2)
uranus = round(x * 0.92, 2)
neptune = round(x * 1.19, 2) 
pluto = round(x * 0.06, 2)

print('Your weight on Earth is:', earth)
print('Your weight on the Sun would equal:', sun)
print('Your weight on Mercury would equal:', mercury)
print('Your weight on Venus would equal:', venus)
print('Your weight on the Moon would equal:', moon)
print('Your weight on Mars would equal:', mars)
print('Your weight on Jupiter would equal:', jupiter)
print('Your weight on Saturn would equal:', saturn)
print('Your weight on Uranus would equal:', uranus)
print('Your weight on Neptune would equal:', neptune)
print('Your weight on Pluto would equal:', pluto)


input('Press any key to exit')

