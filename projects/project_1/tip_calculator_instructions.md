# Tip Calculator

The goal of this project is to make a *tip calculator* program in python and put together a new Github repo for it. **To submit your project, you will simply submit the link to your Github repo on Canvas**

The expectations for your finished project are:

1. Set up a public Github repo that contains your code, and a `README.md` file. This repo with your program will be part of your code portfolio from this class, so keep it neat, and make the README file look nice using [markdown formatting](https://www.markdownguide.org/cheat-sheet/). Be sure to give it a title, and provide a brief summary of what your code does, and how to run it. *To submit your project, you will simply submit the link to your Github repo on Canvas.* Your completed project will be part of your code portfolio on Github, so go ahead and make it look good, and feel free to put your own spin on it!
2. Your program must run properly in python from the command line, and should not require any software or external libraries.
3. Your tip calculator must *be interactive and take user input* at the command line. This means that your python code must respond appropriately based on what the user enters.
4. Your code must be well-commented. Demonstrate how much you understand!
5. After a tip has been calculated, your program should ask the user if they would like to enter another tip, and run again if the answer is yes.
6. Your code should be split into functions, logically broken up and well named. (It's recommended that you do this part last, after you get it running!)
7. This project is an *individual* one! You can talk to your classmates for ideas, but all code should be your own.

*Feeling stuck?*
*   You can always reference the [course Github repo](https://github.com/Justice-Through-Code/fall_2021) and use any lessons or challenges there to guide you
* Googling when you are stuck is encouraged! If you find a snippet of code on the internet you want to use, just make sure that you put a link in acknowledging the source, and *comment* it to make sure you understand it.
* Check in with others in the class, your TAs, and your instructors! Remember that the more proactive you are about seeking out resources, the easier it will be to get on track.


## The Tip Calculator

In a new folder, completely separate from both your pod repo and your class code, make a python script `tip_calculator.py` that takes a user's input at the command line for:
* Cost of the food
* Number of people splitting the bill
* Percentage of the tip


Then, the script should output:
* The total bill (including tip)
* how much each person should pay (you can assume all people will split the bill evenly)

Assume there is a 10% sales tax. Don't forget to add this into the total bill (although this shouldn't be included in calculating the tip itself)!

**Note:** your tip calculator should be able to handle a bill of any amount of many money, with any number of people splitting the bill, and with any tip percentage (including 0% tip)

## Cases your program should be able to handle:

#### A meal for 1

Inputs
* Food costs $15
* 1 person paying
* 20% tip

Expected output:
* `Total bill: $19.50`

#### A feast to remember

Inputs
* Food costs $25000000
* 3 people paying
* 31% tip

Expected output:
* `Total bill: $35,250,000.00`
* `Each person should pay $11,750,000.00`

#### No tip

Inputs
* Food costs $78.99
* 6 people paying
* 0 tip

Expected output:
* `Total bill: $86.89`
* `Each person should pay $14.48`

#### Sharing the bill among many

Inputs:
* Food costs $5000
* 876 people paying
* 12% tip

Expected output:
* `Total bill: $6,100.00`
* `Each person should pay $6.96`


^ Use the examples above as _test input_ to check if your code is working as expected.

### Want to add more features?

* You **may** add extra features to your tip calculator app as long as they do not require any external libraries or software, and don't interfere with following all of the requirements above. You won't get any extra points for these in the class, but if you want to challenge yourself and add your own flair to the app, go ahead!

Have fun!
