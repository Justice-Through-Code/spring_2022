# Logical and Conditonal Operators - Challenge 3

There are 2 parts to this challenge:
1. Debugging code snippets
2. Playing with the stock market

In this challenge, we are providing you 2 incomplete scripts - `snippets_challenge.py` and `stocks_challenge.py`. You will be working on these files to debug some code snippets and also perform some basic stock market calculations.

## Challenge 3.1 - Debugging code snippets

<img src="https://img.freepik.com/free-photo/technology-binary-code-number-data-alert-system-error-message-display-screen_73523-1311.jpg" width="800">

### Overview of the challenge

There are 5 code snippets in `snippets_challenge.py` here that throw errors or give incorrect outputs as of now. Based on the lecture, try to debug these code snippets so that the errors are resolved and we have the correct output. Snippets should be done in order. When a snippet is debugged, the program will run to the next snippet to debug. 

Pay attention to the types of errors displayed in the terminal. 
* Syntax errors means the program cannot run.
* `AssertionError` means there is a logical error in the code caused by `assert()`. 
* `assert()` is a way to test if a condition in your code returns `True`.

The last line `print("CHALLENGE COMPLETED!")` will run when all the errors have been debugged.

## Challenge 3.2 - Playing with the stock market

<img src="https://image.freepik.com/free-photo/financial-stock-market-graph-chart-stock-market-investment-trading-screen_9693-990.jpg" width="800">

### Overview of the challenge

You need to work with the `stocks_challenge.py` file for this challenge.

Imagine that you are managing money for your clients and investing it into the stock market. You are only concerned with 5 stocks - Amazon, Apple, Facebook, Google and Microsoft.

The market price of these stocks is available to you as different variables. For every client, you need to tell him (print out) the number of stocks of a particular company that can be purchased with his current savings.

The name of the client, savings of the client and the stock under consideration need to be taken as user input.

For example, one of your clients named Alex has $5000 in savings. He is interested in knowing how many Apple shares can he buy with his current savings. You need to print the number of Apple stocks that Alex can purchase with his savings at the current market price of Apple.

#### Challenge 3.2.1 - Taking user input
* Write code to take in the name of the client as the user input.
* Write code to get his savings as user input.
* Write code to find out which stock does the client is interested in as user input.

#### Challenge 3.2.2 - Perform user-specific calculations
* Based on the 3 user inputs, calculate the number of stocks that can be purchased by using conditional (if-elif-else) statements.
* Bonus points for handling erroneous user input or inputs out of the scope of this challenge.

#### Challenge 3.2.3 - Output
* Print the output in this format

```console
Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.
```

### Challenge 3.3 - Push to Github

Great job! Now, as the final part of your workflow for this challenge, let's stage, commit, and push the `snippets_challenge.py` and `stocks_challenge.py` scripts you worked on to your branch of your pod's repo!


* Remember to check your pod Github repo online at the end to make sure this worked