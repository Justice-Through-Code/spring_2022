# Before class

# Outline of class agenda
1. Lesson
  * Learn about using git with another user (i.e., collaborating on code)
  * The importance of `git fetch` and `git pull`
2. Challenge
  * Setting up Git preferences on our computers
  * Trying out some collaborative coding
  * Dealing with merge conflicts

# Class
## 1. Refresher on Git
In one of the first weeks, we covered Git. It is a tool for version control. That is, it's responsible for "watching" our files and tracking changes (usually to the cloud, i.e., GitHub).

Unlike systems that do this in a totally automated fashion (e.g., Dropbox, GoogleDrive), Git requires some manual input from the user. Although you may initially find this annoying to have to manually mark changes and move files from your local version to remote version, it is helpful because it grants you complete control and also enables you to make notes about the changes being made.

If you are working on your own repository, a typical Git workflow might look something like this:

```console
$ touch testfile.md
$ git status testfile.md
$ git add -p testfile.md
$ git commit -m "helpful message about the changes you just made"
```

This now means that Git has tracked the changes in your file, but these changes have not yet been shared ("pushed") to the remote location (usually, this is GitHub).

You can push your changes at any time using `git push`, however, it can be advantageous to wait to push your changes until you are satisfied that whatever code you are working on works and will not introduce problems in other parts of the code.

It's also a good idea to push your changes at the end of your working session (just in case anything happens to your computer!) 


When you are working on your own, when you push your code really only impacts you. However, when you are working with someone else, anytime you push your code you are basically telling the other people you are working with that your work is in a semi-final state where combining ("pulling") your code into theirs will not cause any breaking changes.

We will talk about good practices for Git collaboration in the next sections.

## 2. Why use Git to collaborate?
Git was actually designed solely to facilitate collaboration. It was created to help when people were working on building the Linux cluster, a common open-source operating system.

(You can read more about the history of Git [here](https://git-scm.com/book/en/v2/Getting-Started-A-Short-History-of-Git) if you're interested.)

Version control systems, which is the general name for programs like Git, allow people to be simultaneously editing code and documents. If you have ever tried to open a Word document or another shared file in a Dropbox folder, you can probably see why this is a real benefit!

<img src="images/dropbox-conflict.png" width="500">

Instead, Git allows each user to have a local version of the code's folder ("repository"). You get this local version by "cloning" a version from a centralized location, usually GitHub.org

<img src="images/git-clone.png" width="500">

You can make some local changes, committing as you go, and then `push` your changes back to GitHub when you're ready.

We're now going to take a look at some of the nitty gritty of how this collaboration process works, and some typical problems you might encounter. You'll also practice this in the challenge exercise late.

## 3. What are the basic steps of collaborating on Git?
The first step of collaborating with Git is controlling who has edit access to the code. We will work on this in the challenge later.

The other major consideration is how to amend your standard workflow to enable collaboration and try to avoid problems. Earlier, we talked about a typical work flow that looked like this:

```console
$ touch testfile.md
$ git status testfile.md
$ git add -p testfile.md
$ git commit -m "helpful message about the changes you just made"
```

### Checking changes on the remote with `git fetch`
However, if you are working with someone else, they might have made changes since the last time you were working on the project. Therefore, we need to add a very important first step of checking to see if there are any changes on the remote branch.

```console
$ git fetch
$ git status
```

Fetching essentially "sniffs" the remote location to see whether your local version and the remote version are at the same place or not. Importantly, fetching does not actually accept the changes from the remote location. Checking the status tells you the result of this comparison.

Why do you think it might be helpful to check for changes before actually accepting them?

We will talk more in the next section about what to do after fetching.

## 4. Merging the files from the remote to your local version with `git pull`

After seeing that there are some updates on the remote we want to bring to our local version, we can run the following to get them on our local computer:

```console
$ git pull
```


## 5. How to avoid Git collaboration headaches: The importance of pulling before working
In the previous section, we talked about a modification that we will add to the start of our Git workflow.

Now, every time we sit down in our computer to code we will first check to see if anyone else has made changes in the meantime using `git fetch`.

In order to check whether there are changes on the remote version of the code, we then need to use `git status` to show us a comparison between our version of the world and what exists on the remote.

Typically, you will either already be in sync with the remote branch or you will need to "pull" the changes.

Here is an example of what your system might look like after fetching:

<img src="images/git-fetch_up-to-date.png" width="500">

It looks like there are no new changes that you need to integrate with your local copy of the code so there is no need to perform a `git pull` at this time.

Here is another possibility of how your system might appear after fetching:

<img src="images/git-fetch_behind.png" width="500">

In this case, the changes made to the local version and the one from GitHub were done in separate sections of the code so it's easy to simply `git pull` those changes to your local copy of the repository.

Pulling the changes means that you are accepting the current state of the code at the remote location.

```console
$ git pull
```

Sometimes, you will try to pull the code but will get an error message that you have local changes that you need to commit first so they don't get trampled on when you pull in your collaborator's changes.

<img src="images/git-pull_local-changes.png" width="500">

In this case, you can either do a `git commit` if you are ready to accept this bite of work you've done or you can temporarily `git stash` your changes so that they are protected when you pull in the new code and then `git pop stash` and continue where you left off.

<img src="images/git-stash.png" width="500">

However, sometimes you and your collaborator will step on each others' toes and will edit the same part of the code at the same time. Then, when you do your `git fetch`, you might instead see a message like this:

<img src="images/git-merge-conflict.png" width="500">

This is a merge conflict. We will talk about how to deal with these in the challenge.

Remember that Git is always keeping track of changes to files so pulling might overwrite your work if you and your collaborator were editing the same part of the code, but you can always recover your work. In the challenge, we will talk about how to handle these kinds of conflicts.

## 6. Wrap up
Today we talked about the basics of collaborating using Git. The most important addition to our workflow is checking for changes before we start our own work. This looks like:

```console
$ git fetch
$ git status
$ git pull
```

## Sidebar: A quick note on terms
The convention in Git is to call the copy of the code on your own computer the `local` version (or, more precisely, `branch`) and the remote point the `master`.

There has been [substantial debate](https://mail.gnome.org/archives/desktop-devel-list/2019-May/msg00066.html) about whether this use of the word master in this context is derived from the context of slavery or not. In light of this, [GitHub](https://www.bbc.com/news/technology-53050955) has pledged to replace the term master in upcoming releases of Git.

If you would like to change the name of your primary branch away from the term master in the meantime, [here](https://dev.to/damcosset/replacing-master-in-git-2jim) are some straightforward instructions for doing so.

In the challenge exercise, we are going to review how to handle merge conflicts. There are lots of helpful resources online that cover this topic. Here are just a few:

- [an example that includes how to create a merge conflict](https://www.atlassian.com/git/tutorials/using-branches/merge-conflictsEE)
- [basic](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging#_basic_merge_conflicts) and [advanced](https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging) merge conflicts
- [a blog post on handling and avoiding merge conflicts](http://weblog.masukomi.org/2008/07/12/handling-and-avoiding-conflicts-in-git/)
- [an example on merging using a guacamole recipe](https://coderefinery.github.io/git-intro/08-conflicts/)
