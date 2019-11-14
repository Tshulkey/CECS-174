#Constants
EXPONENT = (10 / 3)
SPEED_OF_LIGHT = 299_792_458
SPACEX_INSURANCE= .30
ULA = 14_830
SPACEX_CHARGE = 2_720
LIGHT_YEAR = (10 ** 15) * 9.4607
YEARS = 365
DAYS = 86400
#Print the main menu and choices for the user to choose from
print("Main Menu:")
print("1. Warp Speed")
print("2. Cost of Launch")
print("3. Time Dilation")
print("4. Quit")
#import math to use square root function
import math
#Operation allows users to input which choice they want from main menu
#While loop to keep the program going until the user chooses to quit
operation = int(input("Please choose a function: "))
while(operation >= 1 or operation <= 4):
#If the user chooses 1 calculate warp speed
#Varify the user input of warp factor
#Warp speed formula
    if operation == 1:
        warp_factor = float(input("Please enter warp factor: "))
        if warp_factor > 0:
#Warp speed formula
            warp_speed = warp_factor ** EXPONENT * SPEED_OF_LIGHT
            print(warp_factor)
            print("Warp speed: ","{0:,.2f}".format(warp_speed),"meters per second")
#Once again ask for user operation input for the ongoing loop
#Else statement to remind user the restriction for input
            operation = int(input("Please choose a function: "))
        else:
            print("The speed must be a non-negative number.")
#If user chooses 2 calculate the cost to launch
#Varify user input of satellite mass
    elif operation == 2:
        satellite_mass = float(input("Please enter the satellite's mass:"))
        if satellite_mass > 0:
#Use while loop to continue asking until the input is correct
#Varify second input of satellite cost
            while(satellite_mass > 0):
                satellite_cost = float(input("Please enter the satellite's manufacture cost: $"))
                if satellite_cost > 0:
                    break
#Else statement to remind user of restrictions for input
                else:
                    print("Cost must be a non-negative number")
#Calculate cost to launch for both places
            SpaceX_per_mass = SPACEX_CHARGE * satellite_mass
            cost_to_launch_ULA = ULA * satellite_mass
            cost_to_launch_SpaceX = SpaceX_per_mass + SPACEX_INSURANCE * satellite_cost
#Conditions if ULA is cheaper subtract from Spacex for amount saved
            if cost_to_launch_ULA < cost_to_launch_SpaceX:
                save = cost_to_launch_SpaceX - cost_to_launch_ULA
                print("ULA will save you",end='')
                print(" $""{0:,.2f}".format(save))
#If ULA and SpaceX cost the same amount
            elif cost_to_launch_ULA == cost_to_launch_SpaceX:
                print("ULA and SpaceX cost the same amount")
                print(" $""{0:,2f}".format(cost_to_launch_ULA),end='')
                print(" $""{0:,2f}".format(cost_to_launch_SpaceX))
#If SpaceX is cheaper subtract from ULA for amount saved
            elif cost_to_launch_ULA > cost_to_launch_SpaceX:
                save = cost_to_launch_ULA - cost_to_launch_SpaceX
                print("SpaceX will save you", end='')
                print(" $""{0:,.2f}".format(save))
#Operation input to continue the loop
#Else statement for restriction of input
            operation = int(input("Please choose a function: "))
        else:
            print("Satellite mass must be a non-negative number")
#If the user operation input is 3 calculate Time Dilation
#Varify the user input of ship_distance
    elif operation == 3:
        ship_distance = float(input("Please enter travel distance in light years: "))
        if ship_distance > 0:
#Use while loop to ask user for input until correct
            while ship_distance > 0:
                ship_speed = float(input("Please enter ship velocity as a fraction of the speed-of-light: "))
#Varify the user input of ship speed
#Else statement to remind user of restricted input
                if ship_speed > 0 and ship_speed < 1:
                    break
                else:
                    print("Speed must be less than 1 and greater than 0")
#convert ship distance in light years to meters
#Multiply ship speed by speed of light for velocity
#Use distance formula to calculate time in earth's perspective
            distance_meters = ship_distance * LIGHT_YEAR
            ship_speed *= SPEED_OF_LIGHT
            earth_time = distance_meters / ship_speed
#Calculate dilation with the formula
#Multiply by earth time for perspective of the ship time
            dilation = math.sqrt(1 - (ship_speed ** 2) / (SPEED_OF_LIGHT ** 2))
            space_time = dilation * earth_time
#Convert seconds to days
            earth_time /= DAYS
            space_time /= DAYS
#Check if there are years and find the amount of days with the remainder from years
            earth_years = earth_time // YEARS
            earth_days = earth_time % YEARS
            space_years = space_time // YEARS
            space_days = space_time % YEARS
#Conditions if there are years and days or just years or just days
#If there are earth days and years
            if earth_years > 0 and earth_days > 0:
                print("An observer on earth ages: ",end='')
                print("{0:.0f}".format(earth_years), "years and","{0:.0f}".format(earth_days), "days.")
#If there are only earth years
            elif earth_years > 0 and earth_days < 0:
                print("An observer on earth ages: ",end='')
                print("{0:.0f}".format(earth_years), "years.")
#If there are only earth days
            else:
                print("An observer on earth ages: ",end='')
                print("{0:.0f}".format(earth_days), "days.")
#If there are space years and days
            if space_years > 0 and space_days > 0:
                print("A passenger on the ship ages: ",end='')
                print("{0:.0f}".format(space_years),"years and","{0:.0f}".format(space_days), "days.")
#If there are only space years
            elif space_years > 0 and space_days < 0:
                print("A passenger on the ship ages: ",end='')
                print("{0:.0f}".format(space_years),"years.")
#if there are only space days
            else:
                print("A passenger on the ship ages: ",end='')
                print("{0:.0f}".format(space_days), "days.")
#Operation input to continue the loop
#Else statement to remind user of the restriction of the input
            operation = int(input("Please choose a function: "))
        else:
            print("The distance must be positive")
#If the user chooses 4 end the program
    elif operation == 4:
        print("Goodbye")
        break
#If the user chooses a number greater than 4 or less than 1
#Ask the user to try again
    elif operation > 4 or operation < 1:
        print("Please choose a function from the main menu")
        operation = int(input("Please choose a function: "))
            
        


















                
