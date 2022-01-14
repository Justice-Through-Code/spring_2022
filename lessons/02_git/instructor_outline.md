## 1. Diagram what Git and Github are
* The problem without version control
* Pictures of cloud & local versions
* Also your code portfolio
    * Stress that this is very important, will be used in many many settings

## 2. Demonstrate making new repo on Github

* Make empy public repo `example_git` with readme
* Show how the repo link works
* Stress that this is the 'remote' or 'main' and is on the cloud

## 3. Do git setup stuff on computer

Set up git config file username/email

```console
$ git config --global user.name "Paul Bloom"
```

```console
$ git config --global user.email "paul.bloom@columbia.edu"
```

Set defaut code editor to VSCode

```console
$ git config --global core.editor "code --wait"
```

## 4. Use `git status` to make sure we're not already in a git repo

* Explain that bad things happen with git inside git

## 5. Clone repo with `git clone`

* Show how syntax is always `git clone https://github.com/{your github username}/{name of the repository}.git`
* Show how once we clone, files are on the local computer
* Explain that this only needs to be done once (`git pull` comes later)

## 6. Run `git status` again 
* explain how we are up to date

## 7. Introduce `git add`
* First make a new .txt file, run git status -- show that it is unstaged
* Introduce `git add` as 'telling git what we want it to snapshot'
* Run `git status` again after adding the file

## 8. Introduce `git commit`
* This is now 'taking the snapshot' of our repo at one point in time
* Each commit saves what is different from the last time
* Introduce principle of good commit messages
* Commit adding the text file
* Show that commit does NOT make changes to the remote
* Show that `git status` says we're up to date after a commit

## 9. Demonstrate more changes, staging, and committing
* Show what happens when changing files
* Add a python script
* We don't have to stage/commit all files at once
* Explain that it is important to get the workflow down

## 10. `git push` changes back to remote
* Show how we can use `git push` to update the remote cloud version with our local changes
* Show the changes on the remote, and tools for viewing commit history and diffs
* Explain that this commit history tool will be especially useful when we start using git collaboratively...coming soon!

