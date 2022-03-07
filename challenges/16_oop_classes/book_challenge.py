'''
Object-oriented book challenge!

Your challenge for today is to complete the fill out the missing parts of the Booklist class in book_class.py
Then, test each method for the class Booklist!

Hint: all methods for the Booklist class go in the book_class.py script
This class and the methods are already imported in this script -- test them here for specific cases!
'''

# import the Booklist class and corresponding methods
from book_list_class import Booklist


'''
PART #1.
In book_list_class.py:
Set up the initialization function for class Booklist()
The function should initialize just 1 attribute, called 'books', as an empty list
No parameters needed, other than self

In this script:
Then, create an object of class Booklist called 'my_library'.
Print the books attribute of my_library -- it should be an empty list
Also, print out the type of my_library to see what you get :)
'''
print('PART 1\n')


'''
Part #2:
In book_list_class.py:
Define the add() method to add a book to an object of class Booklist
-The method should take 2 parameters other than self, both strings -- 'title', and 'author'
-The method should create a Book object (it's already imported into the file) with those two attributes
-Then, the method should append this book to books attribute of the the Booklist object  - i.e. self.books.append(book)

In this script:
Once you have finished the method, add the following books to your library:
Just Mercy - Bryan Stevenson
The New Jim Crow - Michelle Alexander
The Truths We Hold - Kamala Harris
My Grandmother's Hands - Resmaa Menakem

Finally, print the books attribute of my_library to make sure your books have been added!
'''
print('\nPart 2\n')



'''
Part #3:
In book_list_class.py:
Define the count_books() method to get the number of books in an object of class Booklist
-the method only needs the self parameter
-the method should return an integer that is the length of the list stored in the books attribute

In this script:
Once you have finished the method, count the books in my_library and print out the result
'''
print('\nPart 3\n')



'''
Part #4:
In book_list_class.py:
Define the remove_title() method which will remove a book by its title from an object of class Booklist
-the method should take the self parameter, plus an additional paramter 'title' (a string for the title of the book to remove)
-the method should remove any books matching the input title from the Booklist
-it does not need to return anything

In this script:
Once you have finished the method, remove 'Just Mercy' from my_library
Then, print out the books attribute to make sure that book is gone
'''

print('\nPart 4\n')


'''
Part #5:
In book_list_class.py:
Instantiate another object of class Booklist called nyt_bestsellers
Then, add 2 books of your choice from the New York Times best sellers lists to nyt_bestsellers using the .add() method
You can find NYT books here: https://www.nytimes.com/books/best-sellers/

In this script:
Then, print out the books attribute of nyt_bestsellers
'''

print('\nPart 5\n')



'''
BONUS Part #6:
In book_list_class.py:
Define a display_titles() method to display all the titles of the books in an object of class Booklist
The titles should be displayed in alphabetical order!
-The method requires no parameters other than self

HINT: there's a quick way to sort a list in alphabetical order

In this script:
Once you have completed this method, test it out on both my_library and nyt_bestsellers
'''

print('\nBONUS Part 6\n')
