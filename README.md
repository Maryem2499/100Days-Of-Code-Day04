#  Heads or Tails

## UPDATE
We've moved away from repl.it for coding exercises.
Check out the new exercises on Coding Rooms with automated submissions.

Login to your Udemy course and head over to the link below to get the sign up link:

[Click here](https://www.udemy.com/course/100-days-of-code/learn/lecture/17825914#questions)

## Instructions

You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails". 

**Important**, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

e.g.
1 means Heads
0 means Tails 

## Example Output

```
Heads
```

or

```
Tails
```


## Solution

[https://repl.it/@appbrewery/day-4-1-solution](https://repl.it/@appbrewery/day-4-1-solution)

#  Who's Paying

## UPDATE
We've moved away from repl.it for coding exercises.
Check out the new exercises on Coding Rooms with automated submissions.

Login to your Udemy course and head over to the link below to get the sign up link:

[Click here](https://www.udemy.com/course/100-days-of-code/learn/lecture/17825914#questions)

## Instructions

You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill. 

**Important**: You are not allowed to use the `choice()` function.

**Line 8** splits the string `names_string` into individual names and puts them inside a **List** called `names`. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

## Example Input

```
Angela, Ben, Jenny, Michael, Chloe
```
Note: notice that there is a space between the comma and the next name. 
## Example Output

```
Michael is going to buy the meal today!
```


## Hint

1. You might need the help of the `len()` function.   

[https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list](https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list)

2. Remember that Lists start at index 0!

## Solution

[https://repl.it/@appbrewery/day-4-2-solution](https://repl.it/@appbrewery/day-4-2-solution)



# Treasure Map

## UPDATE
We've moved away from repl.it for coding exercises.
Check out the new exercises on Coding Rooms with automated submissions.

Login to your Udemy course and head over to the link below to get the sign up link:

[Click here](https://www.udemy.com/course/100-days-of-code/learn/lecture/17825914#questions)

![](https://cdn.fs.teachablecdn.com/wiFJAkZZSG2RpGsxYgDO)
## Instructions

You are going to write a program which will mark a spot with an X.

In the starting code, you will find a variable called ```map```.

This ```map``` contains a nested list.
When ```map``` is printed this is what the nested list looks like:
```
['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
```
In the starting code, we have used new lines (```\n```) to format the three rows into a square, like this:
```
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
```
This is to try and simulate the coordinates on a real map. 

![](https://res.cloudinary.com/dk-find-out/image/upload/q_80,w_1440,f_auto/Co-ordinates_oggjzg.jpg)

Your job is to write a program that allows you to mark a square on the map using a two-digit system. The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:

![](https://cdn.fs.teachablecdn.com/2vnboIYTFFruvl9FJ2w5)

First your program must take the user input and convert it to a usable format. 

Next, you need to use it to update your nested list with an "x". 

## Example Input 1

column 2, row 3 would be entered as:

```
23
```

## Example Output 1

```
['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', 'X', '⬜️']
```
e.g. When you hit **run**, this is what should happen: 

![](https://cdn.fs.teachablecdn.com/5hliFjyIR96LdestyfPd)

## Hint

1. Remember that Lists start at index 0!
2. ```map``` is just a variable that contains a nested list. It's not related to the map function in Python.

## Solution

[https://repl.it/@appbrewery/day-4-3-solution](https://repl.it/@appbrewery/day-4-3-solution)



# Rock Paper Scissors

## Instructions

Make a rock, paper, scissors game. 

Inside the `main.py` file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: `rock`, `paper`, and `scissors`. This will make it easy to print them out to the console. 

Start the game by asking the player:

*"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."*

From there you will need to figure out: 
* How you will store the user's input.
* How you will generate a random choice for the computer.
* How you will compare the user's and the computer's choice to determine the winner (or a draw).
* And also how you will give feedback to the player. 

You can find the "official" rules of the game on [the World Rock Paper Scissors Association website.](https://wrpsa.com/the-official-rules-of-rock-paper-scissors/)

## Debugging challenge

Try running this code and type `5`.

It will give you an `IndexError` and point to line 32 as the issue. 

But on line 38 we are trying to prevent a crash by detecting any numbers great than or equal to 3 or less than 0.

So what's going on? Can you debug the code and fix it?

## Solution to the debugging challenge
[https://repl.it/@appbrewery/rock-paper-scissors-debugged-end](https://repl.it/@appbrewery/rock-paper-scissors-debugged-end)
