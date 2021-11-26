########################################

#Name: Logan Carr
#Course: Python Essentials
#Assignment: Encryption Lab 11/18/2021
#Description: This program encrypts a message using a Caesar shift with loop

########################################

#Printable character for ASCII is 32 - 126  >126 (subtract 95) and if <32 (add 95)

def Caesar_Shift (Message, key):
    Brute = ""
    for x in Message:
        
#This code helps to wrap around the ASCII values
        Temp = ord(x)+ key
        if Temp >126:
            Temp -= 95
        if Temp < 32:
            Temp += 95
        Brute += chr(Temp)
    return Brute

cont = "yes"


#Loop that will continue conducting Caesar shifts until you answer with q
while cont == "yes":

    U_Message = input("Print unencrypted message here: ")
    Shift = int(input("Print number of shifts here for encryption: "))
    E_Message = Caesar_Shift(U_Message, Shift)
    print ("Encrypted message is",E_Message, sep= " ")
    Orig = Caesar_Shift(E_Message, -Shift)
    print ("Original message is", Orig, sep= " ")
    choice = input("\nTo quit press \"q\" or \"Q\" otherwise type any key and press enter to continue. ")
    if choice == "q" or "Q":
        print ("Have a nice day!")
        cont = "no"
















#input('Please press "Enter" to exit.')
