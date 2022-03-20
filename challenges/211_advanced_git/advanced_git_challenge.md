# Git Collab Challenge!

In this challenge, you will:

* Modify your local Git settings to use your preferred text editor
* Add collaborators to a Git repository
* Practice dealing with merge conflicts

## Step 1: Updating your local Git settings
When you first open Git, it is going to make some assumptions about your default preferences. These settings can be viewed by typing `git config --list` from your terminal session.

You can see all possible options for things you could set by typing `git config`.

In the earlier lesson on Git, you used `git config` to modify your username and email address.

Because today you will be working a lot with commit messages, another helpful configuration setting might be to set your default text editor. If you don't do this, Git will usually default to using a command line text editor like [Vim](https://www.vim.org/), [Vi](https://en.wikipedia.org/wiki/Vi), or [emacs](https://www.gnu.org/s/emacs/).

While [some people](https://en.wikipedia.org/wiki/Editor_war#:~:text=vi%20is%20a%20smaller%20and,vim%20is%20almost%20as%20fast.&text=Emacs%20uses%20metakey%20chords.) love these text editors, they can be a bit cumbersome to learn especially when you are new to using terminal.

Luckily, we can configure our Git session to use whatever text editor we prefer. Here are some options for other text editors you have used in class so far:
- Atom `git config --global core.editor "atom --wait"`
- Sublime (on a Mac) `git config --global core.editor "/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl -n -w"`
- Sublime (on a 64 bit PC) `git config --global core.editor "'c:/program files/sublime text 3/sublime_text.exe' -w"`

A full list for other common text editors can be found [here](http://swcarpentry.github.io/git-novice/02-setup/index.html).

## Step 2: Creating a Git repo for this challenge
In order to practice merge conflicts today, but not mess up any of your existing Git repositories, we're going to create a fresh repo to work with today.

Since we're working on collaborative coding, you'll want to break into small groups of 2-3 people. 

### One person creates the repository
Only one person needs to make the repository (the others will get access to it by `cloning` in a little while).

1. Navigate to [github.com](https://github.com/). You may need to login to your account.

2. On the left-hand side of the navigation bar, there should be an option to create a new repository.

<img src="images/new-repo.png" width="300">

3. This should take you to a page where you can give this new repository. Give your repo a name, decide if it's going to be public or private, and initialize it with a README.

<img src="images/create-page.png" width="700">

4. For your first commit, make some changes to the README. This could be a description of the project (always a good idea to have this in your README - see [here](https://github.com/matiassingers/awesome-readme) for examples of quality READMEs), or just some junk text to get us going.

Note: this process can also be [done from the command line](https://www.codegrepper.com/code-examples/shell/how+to+initialize+a+git+repository+command+line).


## Step 3: Adding collaborators
In order to work with someone else on a GitHub repository, you must grant them write access to the code.

This can be done on GitHub as long as you know the other person's username.

1. Go to your project's settings
<img src="images/01-settings.png" width="700">

2. Select `manage access`
<img src="images/02-manage-access.png" width="300">

3. You may need to confirm your login to GitHub - this is the password you initially used to login.
<img src="images/03-confirm-login.png" width="300">

4. Select `invite a collaborator`
<img src="images/04-invite-collab.png" width="700">

5. Find the person you want to collaborate with via their username, and actually send the invite!
<img src="images/05-actual-invite.png" width="300">

Great! Now your collaborator should have full push/pull access to your repository.

In order for your collaborator to start working in your repository, they will need to accept the collaborator invitation. Usually, github will send them an email with a link to follow. If not, they should be able to see the invitation in their [notifications](https://github.com/notifications).



## Step 4: Collaborators clone the github repository

Now that the collaborators all have access to the repository, they can 'clone' it to their own computers. Remember, to **make sure NOT to clone the repository inside another git respository**. Collaborators can run `git status` first before cloning to make sure that they aren't already in a git repository (i.e. it should say 'fatal: not a git repository (or any of the parent directories)'). 


To clone, collaborators go to the repo on github, and click the green 'code' button. Then, they can copy the link in the box that pops down.

<img src="images/clone.png" width="300">

Finally, to clone, collaborators can then run from the command line:

```console
$ git clone [copy link to repo here]
```
<img src="images/git-clone-command-line.png" width="800">


Then, you should see the repo clone to your computer! Run `ls` to see the files, they should all be there!



## Step 5: Each collaborator add 1 new file to the repo.

Remember, the **first** thing you should do when collaborating is to check that you are not missing out on any updates from the remote by running `git fetch` or `git pull` first. This will make sure that you don't get off track with the remote repo.

1. Then, make a new file and add it, commit it, and push! 
2. Look around your repo to see all the things your collaborators have added


## BONUS CHALLENGE: Creating a merge conflict
You can see another example of creating a merge conflict [here.](http://swcarpentry.github.io/git-novice/09-conflict/index.html)

1. Within your new shared repository, we will need to modify a file to use for our merge conflict example.

From terminal, let's create a new file:

```
touch merge-test.txt
```

Test yourself: what would happen if you did a `git status` right now?

In order for these changes to be tracked by Git, you will first need to add the file to what Git is watching. We will do this with `git add merge-test.txt`

What is the next step in making this commit?

2. Let's share this new file we created with our collaborator by pushing our commit with `git push`.

3. In order for your collaborator to see these changes on their computer, we will need to `git pull`.

If they have not yet cloned this repository to their computer and are just looking at the changes on GitHub, they will immediately be able to see this file once they refresh the page.

If the have not yet cloned the repository, this would be a good time to do so that they have a copy on their local machine.

They can copy the link to the repository from GitHub.

<img src="images/git-clone.png" width="300">

From terminal, they can then clone this to their local machine.

Make sure that you are doing this in the directory where you want the repository's folder to live. One suggestion is to create a folder where you will put all of your Git repos - that way you won't get confused with your operating system's default organization scheme (e.g.,  the `Documents` folder on a Mac).

<img src="images/git-clone-command-line.png" width="800">

4. Now, let's make a change to the file that we just created. You can do this by opening the file in your favorite text editor, adding some text, and saving the file.

Once again, we will need to have Git track the changes we have made in our repository.

```
git add -p
```

The `-p` allows us to add changes to the file in a piecemeal fashion. This option is very helpful when we start making lots of changes to a file.

Sometimes, we will want to break up our changes in separate commit messages and this `-p` option makes this easy to do. It also forces us to think about the changes we are committing by reviewing each change in the file as we add it to our commit.

After we have added all of the elements we want into the commit, we need to write our commit message:

```
git commit -m "A short, but clear message so that our future selves know what we did in this commit"
```

5. If we were actually working on our code, we might choose to make several commits before pushing our changes. (Remember the squirrel with their cheeks full of commit "nuts" we talked about before?) However, to move this example along, we are going to push our changes to the remote.

```
git push
```

6. Alright, now let's be bad collaborators and cause a conflict! Have your collaborator follow the above steps (i.e., create a file with the same name, make a change, and push that to GitHub).

For this example to work, your collaborator will need to use the *same filename* and add text that is on the same line(s) as you, but has different content.

For example, you might have written the following text in your file: `this is a piece of test code`

And your collaborator might instead say something like: `mwahahaha I'm going to be a crummy collaborator and cause a merge conflict!`

7. Have your collaborator commit their changes locally using `git commit -m`

8. Now, have your collaborator try to push their commit and see what happens.

Were you able to successfully push your code?

## Step 5: Resolving merge conflicts
1. In this case, your collaborator forgot to `git fetch` and then `git pull` at the beginning of their workflow so you both inadvertently made changes to the same file.

If they had fetched and pulled prior to making there changes, there would be no merge conflict. However, now we need to resolve where your workflows have diverged before we can continue.

If you've been reading the Git messages closely, you may have noticed that it is offering you a way forward:
<img src="images/git-merge-message.png" width="500">

2. If you look at the file in your text editor, you'll notice that the lines where there is a discrepancy are marked with `<<<<<<<` and `>>>>>>>`. This may look different depending on your text editor, but in Atom mine looked something like this:
<img src="images/merge-conflict-in-atom.png" width="500">

In order to move forward, you will need to edit the file so that only the text you want in the final version remains. This will also mean removing the tags surrounding the text that marks the zone of conflict.

After making these changes, your file might look something like this:
<img src="images/merge-conflict-in-atom-post-resolve.png" width="500">

3. Once you have modified the code in your text editor, you will be able to finish making this commit by using `git add`.
<img src="images/git-merge-message.png" width="500">

4. You can either write your own commit message, or accept the default.
<img src="images/merge-commit-message.png" width="500">

## Advanced options
### Git stash
Sometimes you have local changes that you are not yet ready to formalize into a commit, but you still need to pull changes from the remote location. In this case, it can be helpful to `stash` your changes.

This essentially temporarily hides away your local changes so that they remain unaffected when you pull changes from the remote.

To do this, you will first need to `git stash` your changes, `git pull`, and then to recover your local edits `git pop stash`.

<img src="images/git-stash.png" width="500">

### Pulling with rebase
If you want Git to try to avoid merge conflicts when you are pulling in remote changes, you can add the option `--rebase`.

This option essentially uses the syntax we would use when working with multiple branches. In brief, pulling is like merging changes into your existing workflow whereas rebasing crushes your work with something new.

[Here](https://stackoverflow.com/questions/36148602/git-pull-vs-git-rebase/36148752#:~:text=git%20pull%20fetches%20the%20latest,local%20copy%20of%20the%20branch.&text=You%20can%20pull%20using%20rebase,merged%20with%20the%20remote%20changes.) is a helpful Stack Overflow post on this topic.
