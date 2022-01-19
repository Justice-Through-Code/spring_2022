## 1. Show students the Finder/File Explorer, have them interact with it
* Have students use the app to make a new folder
* Break down this process into steps that can be mimicked in the command line


## 2. Show students the command line app/help them get set up
* Terminal on Mac / Command Prompt on PC
* Explain that this will look different for everyone


## 3. Introduce concept of 'working directory'
* 'where you currently are' on your computer
* explain how `/` (or `\`) separate directories in file paths
* `pwd` command -- explain abbreviation
* students will have different working directories
* explain `root` as where the path starts


## 4. Changing the working directory with `cd`
* Expalin that `cd` stands for 'change directory'
* Demonstrate changing working directory to Desktop or Documents
* Explain why we get 'no results' when we change working directory, and that not all commands produce output
* Explain how to 'get out' of a folder using `cd ..`
* Show a few examples of using `cd` with `pwd` and `ls` to explore different directories
* Demonstrate 'tabbing out' once you have typed part of the directory name


## 5. Listing files/directories with `ls`
* Explain the abbreviation
* Demonstrate `ls` command
    * May need to use `dir` for PC
* Show that this is equivalent to looking at files in finder/Windows explorer
* Introduce `ls -l` with flag for detailed file info


## 6. Show how to make directories with `mkdir`
* Explain the abbreviation
* Make a directory `JTC` in Documents and `cd` into the directory


## 7. Break for challenge
* Introduce the terminal through `VSCode` so everyone is on the same page
* Break out into pods for challenge-- this lesson and challenge should be shorter than usual

## 8. VSCode as text editor
* Return students to larger group
* Open up VSCode and explain workflow with text editor
* Open the `JTC` directory in VSCode and create a `hello_world.py` script


## 9. Python workflow
* In VSCode, edit `hello_world.py` to print a message to the user
* Show how python scripts can be run from command line with `python hello_world.py`
* Explain workflow between command line/text editor
* Note the similar process:
    * telling the computer to change directory to `folder-x` vs
    * telling the computer to have python run `file-y`
