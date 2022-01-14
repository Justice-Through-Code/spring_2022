# Before class

* Install the text editor [VSCode](https://code.visualstudio.com/)
* Install Anaconda

# Outline of class agenda

By the end of this class, you'll:
* Feel comfortable working at the command line
* Know what a working directory is, and how to identify your *current working directory*
* Be able to change working directories from the command line
* Be able to find files you are working on from the command line in the file browser (finder) and vice versa

# Class

## 1. The command line

The "command line" is a way to interact with your computer just like using the mouse to click on programs and run them. Although the command line might be a steep learning curve at first, it is REALLY useful for many things in programming, and it is something you will use a lot and get very comfortable with during this course.

If you're using a Mac, you can open Terminal to get to your command line prompt. If you're using a PC, open the Anaconda PowerShell Prompt.

Either way, when you open your command line prompt, you should see a `$` symbol at the end of the line.

<img src="images/command_line_1.png" width="500">

This is the **'prompt'**, indicating that it is ready for you to input a command. It will look a bit like this, but a bit different based on your username on your computer.

#### How to run things from the command line?
  * You pretty much always interact with the command line by typing a 1 line command. Then you run it by hitting enter!

## 2. The working directory

The **working directory** is a concept we will use a LOT in this class! So, we're going to do a lot of practice to get comfortable with it.

**Essentially, the working directory is the folder that you are currently 'in' on your computer.** In fact, the word 'directory' basically always means 'folder' for the purposes of this class.

To check your working directory from the command line, you can type `pwd` and press enter.

<img src="images/command_line_2.png" width="500">


Here, I can now see that I'm in the folder `/Users/paul`

**What do the slashes mean?**
* Each slash means that part to the right is *inside* the folder to the left (in this example, the `paul` folder is inside the `Users` folder)
* These slashes might go the other direction depending on your operating system, but they work the same way

You can verify for yourself how this works by looking at your folders in the finder (Mac) / file explorer (Windows). Here, in my finder we can see that the `paul` folder is inside the `Users` folder

<img src="images/command_line_3.png" width="500">


## 3. Listing files / folders

To see what files and folders are in your **working directory**, you can run the command `ls`. `ls` stands for 'list', so this prints out a list of the files and folders in your working directory:

<img src="images/command_line_4.png" width="700">


This is equivalent to opening up the same folder in your finder/file explorer and looking around. For example, if I go in finder to this folder, it has the same contents, just displayed a little differently:

<img src="images/command_line_5.png" width="300">


#### An additional flag

You can also add what is called a ['flag'](https://en.wikipedia.org/wiki/Command-line_interface#Command-line_option) to modify the output of a command you run at the prompt. With `ls`, we can add a `-l` flag to get more deatiled info on each folder/file in the working directory (like the file size, when it was created or last updated, etc) as below:


```console
$ ls -l
```

The output looks like this:

<img src="images/command_line_6.png" width="500">

We won't go into the details of what each output is now, but this more detailed printout can help us find a lot of information about our files and folders. If you'd like to know more about this output, [check out this link.](https://linoxide.com/linux-command/20-ls-command-linux/)

## 4. Displaying contents of file

#### Mac
To display the contents of a file in your Terminal window, you can use several commands, with `cat`, short for "concatenate" being one of the most popular for Mac users.

```
$ cat filename
```
The result of `cat JFK.txt`, where JFK.txt is a text file with a description of the John F. Kennedy International Airport, looks like this:

<img src="images/command_line_15.png" width="500">


The `cat` command can also be used to create files or concatenate (string together) the contents of multiple files. For more details about the command and how to use it, [read this](http://www.linfo.org/cat.html).

#### Windows
The Windows equivalent of the `cat` command to display file contents is called `type`. Similarly, you can use:

```
$ type filename
```

## 5. Changing working directory

Changing your working directory basically means **'moving to another folder'**. To do this, we can use the command `cd`, which stands for 'change directory'. To change directory to any folder, we can run the command
`cd` followed by the folder that we want to go into:

I'll change my working directory to the `Desktop` folder inside `/Users/paul`

<img src="images/command_line_7.png" width="500">

We actually get **no printout** here, it just returns us to the next command prompt. So, we can check whether we actually made it into the folder we wanted to by running `pwd` again to show the working directory

<img src="images/command_line_8.png" width="500">

So, we can see that we are actually at the Desktop folder. If we run `ls`, we will now see the contents of this folder instead, and we can confirm this in finder/file explorer:

<img src="images/command_line_9.png" width="800">

We can see the same thinks in the `Desktop` directory whether we look in finder (left) or via the command line (right)


### Getting out of a directory

There is a special set of symbols for the directory outside the one you are in, it is `..` (two periods). So, if we want to **get out of the current folder** (or 'go up one level'), we can run `cd ..`

If I'm still in my `Desktop` folder, then I go out of this folder with `cd ..`, I'll be back in `/Users/paul/`

<img src="images/command_line_10.png" width="500">
