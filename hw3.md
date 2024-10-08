Make a directory named 'hw3'，and any related files should be placed in it and have to be named with head of 'p' plus a problem number, such as 'p1.sh' which represent a code for problem 1. and etc. As a result, the file named 'p1.sh' should be \~/hw3/p1.sh （‘~' represend the root directory of you account).


1. Write a Python to allow users input a number, and decide whether the number is even or odd, and print your results on the terminal.
2. read the following python, which is a number-guessing game. Note that this program will throw an error if you enter text that isn’t a number. you need to fix it through using a try statement to catch it.
```
import random
secret = int(random.uniform(0,10))
print("I'm thinking of a number between zero and ten."
 , "Can you guess what it is?")
guess = 11

while guess != secret:
    guess = int(input("Take a guess: "))
print("Well done!")
```
a try statement way is
```
try:
 code where there might be a problem
except type_of_error:
 code to run if there's an error
``` 
3. Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is
between 0.0 and 1.0, print a grade using the following table:
```
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6  F
Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
```
Run the program repeatedly as shown above to test the various different values for
input

4. Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count,
and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error
message and skip to the next number.
```
Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333
```


