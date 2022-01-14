## 1. Visualize git collaboration
* Expand diagram to include multiple users
* Introduce dev scenario: want to keep working on code, but not break the working version

## 2. Talk about `git pull` for getting updates from remote to local
* Emphasize workflow of pulling before pushing
* Emphasize that pulling is regular (unlike `git clone` which is only done once)
* Make a change directly online from the `example_git` repo from last class, and show that it only appears on the local repo once you have pulled

## 3. Show collaboration demo! 
* 2 different instructors take turns using `git pull`, then making and committing changes, then `git push` to the same repo
* Show that different collaborators show up in the commit history

## 4. Introduce branching with `git checkout`
* Show use of `-b` flag for creating a new branch to check out
* Make new branch called `dev`
* Commit a change to a file on the `dev` branch

## 5. Introduce using `git show-branch -a` to see schematic of branches
* Talk about order of commits on different branches
* Which one is 'ahead'?

## 6. Show how to *switch* branches with `git checkout`
* Show switching between `main` and `dev` branches

## 7. Show how to push to a certain branch with `git push --set-upstream origin <branch name>`
* Show how to navigate branches on Github.com
* Explain how when we have multiple branches it is important specify which to push too
    * i.e. `git pull origin main` will pull from main, while `git pull origin dev_branch` will pull from dev

## 8. Pull requests
* Explain concept of pull request
* One person wants their changes from a branch pulled to main, others can review
* A way to introduce review & testing into collaboration
* Emphasize that understanding pull requests is essential for collaborative work


## 9. Pull requests & review
* Introduce concept of assigning pull request for review
* Instructor demonstrating pull request assign the other instructor from the demo to review
* Second instructor show review, then merging pull request into main, deleting branch

