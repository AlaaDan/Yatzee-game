# Yatzee-game
This task involves writing a program to play the first rounds of Yatzy for one person. The game should have a simple menu with two choices, 
which are presented before the game begins. These choices should be:

1: Play
2: Exit the program

When the game round is over, the menu should appear again so that you can make a new choice, until you choose to end the program.
The program must be divided in such a way that the following two functions are implemented and used in an appropriate manner. You can divide your code into more functions 
if you want.

A function for printing menu selections and receiving input from the user. The entered value must be  returned from the  function. If an input selection is not valid, 
an error message should be printed and a new entry requested. This is done until an acceptable value has been entered.  

A function that simulates a roll of the dice with a six-sided dice, and  returns the  number of the outcome (a number in the range 1 to 6).

The game is played over six rounds where the first round is about getting ones, the second round is about getting twos and so on ...

Each round allows the player to make a maximum of three rolls of 5 dice. The dice that have been given the "correct number for the round" are not rolled again. 
If all dice get the "correct number for the round" and you have one or two rolls left, the last rolls in the round are not made.

The final sum of a game round is given by the total sum of all rounds and must be presented on the screen. If the game round ends with a score of at least 63 points, 
a bonus of 50 points will also be awarded.
