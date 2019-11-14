#Import EnglishDictionary to check if a string is a word
#Import math to calculate the order for the squares
import EnglishDictionary
import math


#This function prints the main menu options
def print_menu():
    print("Main Menu:")
    print("1. Check a palindrome")
    print("2. Check a crossword square")
    print("3. Quit")

#This function gets the user's inputed option
#Make sure that only 1-3 can be used in input
def get_menu_choice():
    choice = int(input("Please select an option: "))
#If the user doesn't enter a number between 1-3 then loop until they do
    while choice < 1 or choice > 3:
        print("Please input with the options given.")
        choice = int(input("Please select an option: "))
#Return the choice the user inputs
    return choice

#This function gets user input of a phrase
#Validate that at least one character is entered otherwise repeat instruction
def get_phrase():
    phrase = input("Please enter a phrase: ")
    while phrase is "":
        phrase = input("Please enter a phrase: ")
#return the phrase user inputs
    return phrase

#This function checks if the string is a palindrome
#Convert the user's phrase to lowercase
#j = len(phrase)-1 so it checks the letters backwards
#While i < j means that i cannot go past where j is or has been
def is_palindrome(phrase):
    phrase = phrase.lower()
    i = 0
    j = len(phrase) - 1
    while i < j:
#While iterating to the right (i) is less than the iteration to the left (j)
#Must check whether the character is a letter or not
#If it is not a letter the computer will iterate to the next character
        if not phrase[i].isalpha():
            i += 1
        elif not phrase[j].isalpha():
            j -= 1
        else:
#When both i and j are letters check if they are equal if not return false
#Otherwise add 1 to i and subtract one from j to continue iterating
            if phrase[i] != phrase[j]:
                return False
            i += 1
            j -= 1
#If all letters are equal return true
    return True

#This function calls for the get_phrase function to get the returned user input
#Then it calls the function is_palindrome with the inputed phrase to check if it
#is a palindrome or not
def menu_check_palindrome():
    phrase = get_phrase()
    palindrome = is_palindrome(phrase)
#Depending on if the returned value is True or False it prints the
#original phrase the user inputed and a statement
    if palindrome == True:
        print('"' + phrase + '"',"is a palindrome!")
    else:
        print('"' + phrase + '"',"is not a palindrome.")

#This function asks user to input the first line and based on that line's length
#they are asked to input the number of lines equal to the length of the first
def get_crossword_square():
    square = input("Please enter the first line: ")
#The crossword square needs at least one character
    while square is "":
        square = input("Please enter a word with at least one character: ")
#Calculate the order with the length of the word entered
    order = len(square)
    for i in range(order - 1):
        square_next = input("Please enter the next line: ")
#The next words should be as long as the first if not then ask again
        while len(square_next) != order:
            print("The length must match")
            square_next = input("Please enter the next line: ")
#Returns the inputs as a concatinated value
        square = square + square_next
    return square

#This function checks if the user's concatenated inputs are words
#Make sure every letter is lowercase so the EnglishDictionary module can work
#To find the order take the square root of the length of the inputs
def check_crossword_square(square):
    square = square.lower()
    order = int(math.sqrt(len(square)))
#Use for loop and slices to check each horizontal input
#based on the order if it is a word
#Use the EnglishDictionary module and is_word function
#If one of the inputs is not a word return false
    for i in range(0,len(square),order):
        word = square[i:i + order]
        if not EnglishDictionary.is_word(word):
            return False
#Use another for loop to check the vertical inputs notice the patern
#Use the EnglishDictionary module and is_word function
#If one of the inputs is not a word return false
    for i in range(order):
        word = square[i:len(square):order]
        if not EnglishDictionary.is_word(word):
            return False
#If every thing is a word return true
    return True
    
#This function starts the crossword option
#It calls the get_crossword_square function and reveives the value
#Calls the check_crossword_square function with the reveived value
#Find the order
def menu_check_crossword_square():
    square = get_crossword_square()
    crossword = check_crossword_square(square)
    order = int(math.sqrt(len(square)))
#If the value of check_crossword_square is true then print the orignal
#lines on separate lines using for loop and print a statement
    if crossword == True:
        for i in range(0,len(square),order):
            word = square[i:i + order]
            print(word)
        print("is a crossword square!")
#Else print the words on separate lines and print it is not a square
#The for loop will help printing the values based on the order on seperate lines
    else:
        for i in range(0,len(square),order):
            word = square[i:i + order]
            print(word)
        print("is not a crossword square")
        
#This is the main function that calls the menu to be printed
#Calls the get_menu_choice function to get the returned option input
def main():
    print_menu()
    choice = get_menu_choice()
#While the choice is <= 3 the function will continue to run
#Based on the input there are three outcomes
    while choice <= 3:
#1. will call the function menu_check_palindrome
#It will then ask the user to enter another option from the menu
        if choice == 1:
            menu_check_palindrome()
            print_menu()
            choice = get_menu_choice()
#2. will call the menu_check_crossword_square function
#It will then ask the user to enter another option from the menu to loop
        elif choice == 2:
            menu_check_crossword_square()
            print_menu()
            choice = get_menu_choice()
#3. If the user enters 3 the program will end
        elif choice == 3:
            print("Goodbye.")
            break

#This calls the main function and starts the whole program
main()





