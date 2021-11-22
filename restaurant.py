###Logan Carr - Initial program, week one. Ultimate goal is to turn this into a tip calculator




total = 47.33
##Cost of meal before tax
tax = round(total*0.0675, 2)
##Cost of tax from the cost of meal
newtotal = round(total + tax, 2)
##Total cost of meal with tax added
tip = round(newtotal*0.18, 2) 
##Tip amount off of total meal with tax @ 18% tip

print("Hello the cost of your meal was: ", total)
print("Hello, your tax cost is:$",tax)
print(" This brings your total to: $",newtotal)
print("  The tip would be: $",tip)
print("   The new total with tip included would be: $",newtotal + tip)
