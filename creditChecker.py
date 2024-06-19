#Below is an algorithm that I created for task one: Using Llun algorithm to validate a credit card number.
import re
from time import sleep

cardNumber = input("Input the credit card number for validation: ")

#Below are the four formats that will be accepted for cardNumber.
while True:
    cardFormat1 = r'^[0-9]{4.4} [0-9]{4.4} [0-9]{4.4} [0-9]{4.4}$' #ex 0000 0000 0000 0000
    cardFormat2 = r'^[0-9]{4.4}-[0-9]{4.4}-[0-9]{4.4}-[0-9]{4.4}$' #ex 0000-0000-0000-0000
    cardFormat3 = r'^[0-9]{4.4}\.[0-9]{4.4}\.[0-9]{4.4}\.[0-9]{4.4}$' #ex 0000.0000.0000.0000
    cardFormat4 = (14<=len(cardNumber)<=16 and cardNumber.isdigit()) #ex 00000000000000

#The loop breaks when one of the format criteria is met, otherwise the programme prints an error message and the program closes.
    if any([re.search(cardFormat1, cardNumber), re.search(cardFormat2, cardNumber), re.search(cardFormat3, cardNumber), cardFormat4]):
        break
    else:
        print("Card Number is invalid. Closing Window")
        sleep(3)
        exit()

#Find the card type
if cardNumber.startswith("4"):
    cardType = "Visa"
elif 51 <= int(cardNumber[:2]) <= 55:
    cardType = "Master Card"
elif cardNumber.startswith("36") or cardNumber.startswith:
    cardType = "Diners Club"
elif cardNumber.startswith("6011"):
    cardType = "Discover"
elif cardNumber.startswith("35"):
    cardType = "JCB"
elif cardNumber.startswith("34"):
    cardType = "Amex"
else:
    cardType = "Unknown"

#Removes unwanted characters.
cardNumber = cardNumber.replace("-","").replace(".","").replace(" ","")

#Creates an array containing each of the card numbers.
cardNumber = list(map(int, cardNumber))

#Remove the check diget.
checkDigit = cardNumber[-1]
cardNumber = cardNumber[:-1]
#Reverse the list.
cardNumber.reverse()

#Using Llun Algorithm.
for i in range(len(cardNumber)):
    if i%2 == 0:
        cardNumber[i] = cardNumber[i]*2
        if cardNumber[i] > 9:
            cardNumber[i] = cardNumber[i] - 9

if (sum(cardNumber) + (checkDigit)) %10 ==0:
    print(" Card number: Valid")
    print( " Card Type: ", cardType) #ex. Master Card OR Visa
else:
    print(" Invalid Card number")

#Keeps the window open while the user reads the output
input(" Enter any key to close...")