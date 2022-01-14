# NBA Challenge: Storing and calculating 2020 NBA playoff statistics 

<img src="https://clutchpoints.com/wp-content/uploads/2020/04/nba-9.jpg" width="800">


In this challenge, we're giving you a script called `nba_challenge.py` that you'll be working on to calculate some 2020 NBA playoff stats. You'll use this to practice your skills at working with primitive data types in python.

*To get started put `nba_challenge.py` in your personal folder inside your pod repo.*

In the 2020 NBA playoffs, Jamal Murray, Fred VanVleet, and James Harden rank #1, #2, and #3 respectively for the number of 3-point shots made at 46, 43, and 37. 

## Challenge 2.1: Store the number of three point shots made in variables for each player 

In the file `nba_challenge.py`, create variables to track the number of 3-point shots Fred VanVleet and James Harden have made. There already exists a variable for Jamal Murray.  

### Challenge 2.2: Print out the number of three point shots using f-strings with the variables created for each player in 2.1 

Note: Make sure to use the variables you created in Challenge 2.1 in the print statements! 

#### Challenge 2.3: Store the number of three point shot attempts in variables for each player 

In the 2020 NBA playoffs, Jamal Murray, Fred VanVleet, and James Harden attempted 93, 110, 109 three point shots total. Create variables to store these values in `nba_challenge.py`, similar to what you did in Challenge 2.1. 

### Challenge 2.4: Build on your print statement! 

Copy the print statements you wrote in Challenge 2.2 and extend them by printing both the number of three point shots each player made as well as the number of three point shots each player attempted. Try to use only one `print()` statement for each player and remember that you can use 'f-strings' to insert variables into lines of text (reference the examples above if you forgot how to do this). 

### Challenge 2.5: Calculate and print the three point percentage for each player

The three point percentage is given by the following formula: `3 point shots made/3 point shots attempted`

## Challenge 3: Formatting string information about the Lakers

Below is a big paragraph of text about the Lakers 2020 season from https://www.lineups.com/nba/roster/los-angeles-lakers

*The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. They sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. Those three have made good developments with the Pelicans, especially Brandon Ingram. But, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. Los Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. The Lakers ended the season atop the Western Conference with a record of 49-14. They were narrowly behind the Bucks for the best record in the league. Davis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year. Los Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.*

### Challenge 3.1 Print out the paragraph but with only 1 sentence per line

This is a HUGE chunk of text. Can you add **escape characters** to print out this text from a python script to the command line so that only one sentence is on each line?

### Challenge 3.2 Print out the paragraph with only 1 sentence per line, and all in upper case

### Challenge 3.3 Are the Lakers the best team?

* Make a boolean variable called `lakers_are_best` that indicates, to the best of your knowledge, whether the following statement is true: *The Lakers are the best basketball team in the NBA*
* Using an f-string containing your `lakers_are_best` variable, print out your evaluation of whether the statement was true or not

### Challenge 3.4 Type conversion

* Convert your `lakers_are_best` variable to an integer, and print it out. 
  * Why do you think it takes this value?
* Convert your `lakers_are best` variable to a float, and print it out

### Challenge 3.5 Type conversion part 2
* Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.
  * What do you notice?
* Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.
  * What do you notice here?

### Challenge 4: Pushing to your branch of your pod repo, and submit a pull request

Same as previous challenges! Need a reminder? See [the git collab challenge here](https://github.com/Justice-Through-Code/spring_2021/blob/main/challenges/03_git_collab/03_git_collab.md#step-5-opening-a-pr-in-github)


**Congrats! You finished the NBA-themed primitive data types challenge!**