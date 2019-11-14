/*
Tonya Shulkey
import the scanner to get user inputs
write the first statement of the program public class __title__
 */
import java.util.Scanner;
public class Increasing_order {

//This method takes an array of values and finds whether it is increasing
//It returns 1 if it is increasing and -1 if not

    public static int isIncreasing(int[] values) {

//Number is the counter for the previous number if the next number is larger then it is increasing still
//Otherwise return -1 because it is in decreasing order
//The for loop continues until i is larger then the length of the array

        int number = 0;
        for (int i = 0; i < values.length; i++){

//values[i] checks the specific place of the array and checks if it is larger

            if (values[i] > number){
                number = values[i];
            }
            else{
                return -1;
            }
        }
        return 1;
    }

//This method gets the user input a positive number
//Declare the scanner function
//Print instructions

    public static int getNumber() {
        Scanner scan = new Scanner(System.in);
        System.out.println("Please enter a positive number: ");
        int integers = (scan.nextInt());

//Get user input and while it is a negative number or 0 continue to ask for it

        while (integers <= 0) {
            System.out.println("Please enter a positive number: ");
            integers = (scan.nextInt());
        }

//return the input

        return integers;
    }

//This method creates an array of the numbers inputed

    public static int[] getDigits(int number){

//Find out how many digits are in the input
//Create an array called values with a length of how many digits there were
//Math.log10(number) gives you a double which should be converted to int and it will give you how many digits - 1


        int digits = (int) Math.log10(number);
        int[] values = new int[digits + 1];

//The for loop uses modulo to take the last digit of the number and put it in the right most spot
//Of the array then cuts out the last number for the next iteration

        for (int i = 0; i < values.length; i++){
            values[digits - i] = number % 10;
            number = number / (int) Math.pow(10,1);
        }
//Return the array
        return values;
    }

//This is the main function

    public static void main(String[] args){

//call getNumber() to get the user input and set it to a int variable
//Call getDigits() to convert the numbers into an array and set it to a int array variable
//Call the isIncreasing() to find wither the numbers are in increasing order set to int variable

        int numbers = getNumber();
        int[] values = getDigits(numbers);
        int order = isIncreasing(values);

//If the return value is True (1) then print that the numbers are increasing order
//Otherwise print that it is not in increasing order

        if (order == 1) {
            System.out.println("The digits " + numbers + " are in increasing order.");
        }
        else{
            System.out.println("The digits " + numbers + " are not in increasing order.");
        }
    }

}
