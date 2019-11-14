#Tonya Shulkey
#Import the musicbox so that the program can make sound
#At the top write the assign the musicbox function to my_music so it can be used

import musicbox

my_music = musicbox.MusicBox()

#Notes C through B length of 7 with integers
NOTES = [('C', 60), ('D', 62), ('E', 64), ('F', 65),('G', 67), ('A', 79), ('B', 71)]
#Major scales intervals (integers)
MAJOR_INTERVALS = [2, 2, 1, 2, 2, 2, 1]
#Minor scales intervals (integers)
MINOR_INTERVALS = [2, 1, 2, 2, 1, 2 , 2]


#This function validates the notes given by users and converts to integers
#number is set to 0 and will be added up depending on the note
def note_to_int(note):
    number = 0
#This loop will check each note whether it has a letter in the NOTES list
#It unpacks the notes given assigning it to a letter and number
    for i in range(len(NOTES)):
        NOTE_LETTER, NOTE_NUMBER = NOTES[i]
        if NOTE_LETTER in note:
            number = NOTE_NUMBER
            letter = NOTE_LETTER
#If the length is greater then 1 it will check if it has #,b, or ^
            if len(note) > 1:
                for i in range(len(note)):
#if the character is equal to the letter continue because the number is already counted
                    if note[i] == letter:
                        continue
#If the character is # then add 1 to the number
                    elif note[i] == '#':
                        number += 1
#If the character is b then subtract 1 from number
                    elif note[i] == 'b':
                        number -= 1
#If the character is ^ add 12 to the number
                    elif note[i] == '^':
                        number += 12
#If the character is none of the above the input is invalid return -1
                    else:
                        return -1
#If all characters are valid return the number
                return number
#If it is just one character the note letter and it is valid return the number
            return number
#If there is no note letter then the input is invalid return -1
    return -1


#This function prints the menu for users to choose from
def print_menu():
    print("Menu:")
    print("1. Play Scale")
    print("2. Play Song")
    print("3. Quit")

#This function gets the menu choice from user and validates it until they enter correctly
def get_menu_choice():
    choice = int(input("Please select an option :"))
    while choice < 1 or choice > 3:
        choice = int(input("Please select an option in the menu :"))
    return choice

#This function asks the user to input a scale
#The Note should be followed by major or minor
def get_scale():
    name_scale = input("Please enter the name of a scale :")
    name_scale = name_scale.split(' ')
    scale_type = name_scale[1]
    note = name_scale[0]
    number = note_to_int(note)
#This function validates the input by sending the note part of the input to the function
#note_to_int() and then check if the scale_type entered is valid
    while number == -1 or scale_type != 'major' and scale_type != 'minor':
        name_scale = input("Please enter the name of a scale correctly :")
        name_scale = name_scale.split(' ')
        scale_type = name_scale[1]
        note = name_scale[0]
        number = note_to_int(note)
#Once the input is valid it will be set in a tuple of integer of note and scale type
#Then returns that value
    value_type = (number, scale_type)
    return value_type


#This function creates a list with all the integers on the scale based on the type
def scale_to_ints(scale):
#Unpack the tuple and set the first input of the list to number (the int of the note)
    number, scale_type = scale
    notes = [number]
#If the type is major scale then the numbers will be added depending on the major intervals
#then it will be appended to the list
    if scale_type == 'major':
        for i in range(len(MAJOR_INTERVALS)):
            number += MAJOR_INTERVALS[i]
            notes.append(number)
#If the type is minor scale then the numbers will be added depending on the minor intervals
#then it will be appended to the list
    elif scale_type == 'minor':
        for i in range(len(MINOR_INTERVALS)):
            number += MINOR_INTERVALS[i]
            notes.append(number)
#The list will be returned
    return notes


#This function will play the scale the user inputs
#It will call get_scale to receive the input then send it to scale_to_ints
#which will convert the note to an integer
def menu_play_scale():
    scale = get_scale()
    notes = scale_to_ints(scale)
#This for loop will play a note for every single note in the notes list at 500 milisec
    for i in range(len(notes)):
        my_music.play_note(notes[i], 500)

#This function will ask the user to enter a song file assuming they enter it correctly
#Then returns the song file
def get_song_file():
    song = input("Please enter a file name to play a song :")
    return song


#This function will open the file given
#It will read each line of the file skipping any line starting with // as it is a comment
def play_song(file_name):
    for line in open(file_name):
        if '//' in line:
            continue
#The line will be split by the spaces
#The length will find the last term of the list
#If the length is greater than one then that means there is a chord
        line_split = line.split(' ')
        length = len(line_split) - 1
        if length > 1:
#Create a list for the chords calling it numbers
#The for loop will loop through the length
            numbers = []
            for i in range(length):
#Set the note to line_split[i] which will be one note at a time
#Duration will be set to line_split[length] for the last term and take out the \n part
#Convert duration to an integer and append the note integer to the numbers list
                note = line_split[i]
                duration = int(line_split[length].strip('\n'))
                numbers.append(note_to_int(note))
#After the loop finishes play the chord with the list and duration
            my_music.play_chord(numbers, duration)
        else:
#If the length is only 1 then it is only one note
#Therefore note will be the first term and duration will be the last taking out \n
#After converting the duration to an integer convert the note to an integer by calling
#note_to_int function
            note = line_split[0]
            duration = int(line_split[length].strip('\n'))
            numbers = note_to_int(note)
#This for loop checks if the letter is a P or an I
#If the letter is P then that means it is a pause so use the pause function of musicbox
#If the note is I then use the change_instrument function of the musicbox
            for i in range(len(note)):
                if note[i] == 'P':
                    my_music.pause(duration)
                elif note[i] == 'I':
                    my_music.change_instrument(duration)
#If the note is not P or I then play the note
            my_music.play_note(numbers, duration)

#This function calls the get_sont_file function and assigns it to song then sends it
#to play_song
def menu_play_song():
    song = get_song_file()
    play_song(song)


#This is the main function that calls the print_menu function
#Also calls the get_menu_choice function which will continue until user enters 3
def main():
    print_menu()
    choice = get_menu_choice()
    while choice >= 1 and choice <= 3:
#If user enters 1 it will call menu_play_scale then print the menu and recieve a choice
        if choice == 1:
            menu_play_scale()
            print_menu()
            choice = get_menu_choice()
#If user enters 2 then it will call menu_play_song then print the menu and receive a choice
        elif choice == 2:
            menu_play_song()
            print_menu()
            choice = get_menu_choice()
#If the choice is a 3 prints goodbye and the program will end
        else:
            print("Goodbye.")
            break

#This calls the main function to begin the program
#my_music.close will close the musicbox and prevent an error
main()
my_music.close()