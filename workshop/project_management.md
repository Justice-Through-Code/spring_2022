# Project Management Challenge

# Initial Setup

The following steps must be carried out by **one member** of the group (over screenshare with the rest of the group):

## Create a group repository

This will be your group's repository for your WOW project and where you will collaborate together and contribute code!

### Let's create the repository!

-   Click on the `+` icon in the top navigation bar and select `New repository`
-   Enter your project name as the repository name
-   Select the `public` option
-   Under `Initialize this repository with:` select `Add a README file`

<img width="801" alt="Screen Shot 2021-10-28 at 4 49 41 PM" src="https://user-images.githubusercontent.com/7483633/139334999-4075825f-e1b7-4462-9b6c-ebd5daa9c0b6.png">

## Create a project

Projects are a customizable, flexible tool for planning and tracking work on GitHub. The "work" here is a combination of using `issues` and `pull requests` for individual group members to contribute to the repository

### What are `issues`?

In the wider Github community, `issues` are a way to request for new features, ask technical questions and report bugs for open source projects. You will be using `issues` to outline technical task.

The typical workflow to contribute to the codebase is:

-   An `issue` is created. Here's an example of an `issue` related to [implementing a Django form](https://github.com/Justice-Through-Code/project-management-demo/issues/8).
    -   Django work can be split into multiple issues: Creating a model, creating a form, creating a view and so on. See more examples of issues [here](https://github.com/Justice-Through-Code/project-management-demo/issues)
-   An `issue` is assigned to one of the group members to work on. This is like assigning a task.
-   A new branch must be created to work on the assigned `issue`.
-   Once all of the code has been committed, the assigned group member will create a `pull request` to merge the new branch into `main`
-   Reviewers are assigned to review the pull request
-   Once the code is approved by group members, merge into the `main` branch

### Let's create the project!

-   Go to `Projects` tab and click `Create a project` button
-   Enter `Project board name`
-   Set `Automated kanban` as the project template and click `Create project`

Once you've created your project, you should see three boards: `Todo, In progress and Done`. Your group's `issues` and `pull requests` will appear as cards and move across the board. See this [example project's](https://github.com/Justice-Through-Code/project-management-demo/projects/1) boards.

<!-- <img width="1680" alt="Screen Shot 2021-11-16 at 9 00 58 AM" src="https://user-images.githubusercontent.com/7483633/142001615-b96051a1-99e3-423d-86d1-bea02a37174e.png"> -->

<img width="1680" alt="Screen Shot 2021-11-16 at 9 04 27 AM" src="https://user-images.githubusercontent.com/7483633/142001653-40d19112-f22c-4b1b-bfe5-c8d0242127d1.png">

## Create a template for issues

In the `Settings` tab:

-   Click on `Options` on the vertical menu on the left side of the screen
-   Under `Features` section, you should see `Issues` checked
-   Click on `Set up templates`

<img width="1680" alt="Screen Shot 2021-11-16 at 9 07 03 AM" src="https://user-images.githubusercontent.com/7483633/142002172-702962dd-9bef-4c01-b0f4-347bfd699b7c.png">

A new view will be displayed with a lone dropdown:

-   Open the `Add template: select` dropdown and select `Custom template`

A row with a title of `Custom issue template` should appear.

-   Click `Preview and edit`

A new section appears under the row

-   Click on the pencil icon next to the `Issue: Custom issue template` title

<!-- <img width="1680" alt="Screen Shot 2021-11-16 at 9 07 19 AM" src="https://user-images.githubusercontent.com/7483633/142002186-60483885-6af5-419e-9ea6-f10e45cfc07e.png"> -->

<!-- <img width="1680" alt="Screen Shot 2021-11-16 at 9 07 29 AM" src="https://user-images.githubusercontent.com/7483633/142002210-54f30143-c2c4-4eb2-bea4-d79634352730.png"> -->

<img width="1679" alt="Screen Shot 2021-11-16 at 9 07 40 AM" src="https://user-images.githubusercontent.com/7483633/142002261-92684cb7-432d-40b4-a3c4-e2be224e4157.png">

Paste the section below into the `template content`:

```
## Overview
<!-- Add description of the task -->
<!-- Add screenshots related to the task -->

## Technical Notes
<!-- Add details to relevant implementation that you think might be helpful -->
<!-- Add links to documentation -->
```

When you create issues later, it'll be a guide of what to write into an issue for your group members

<img width="1680" alt="Screen Shot 2021-11-16 at 9 08 04 AM" src="https://user-images.githubusercontent.com/7483633/142002276-4d8dca0e-b2de-40e6-a7bf-d1ac0caca1bc.png">

<img width="1680" alt="Screen Shot 2021-11-16 at 9 10 47 AM" src="https://user-images.githubusercontent.com/7483633/142002303-917ef6c6-56c1-4c2c-b8f7-5f8305b6e5f9.png">

-   Click `Commit changes`


## Update `main` branch rules

The `main` branch is the default branch where the most current working version of your code should exist. Therefore, it's good practice to set some restrictions in how new code gets into the `main` branch (i.e. all code should pass through a careful review process before being merged to `main`).

You may want to add rules for:

-   Requiring a pull request to merge new code and prevent group members to directly push code into `main`
-   Requiring that a certain number of members in your group approve the pull request before the code is merged into `main`

### Let's add some rules!

In the `Settings` tab:

-   Click on `Branches` on the vertical menu on the left side of the screen
-   Click 'Add rule' to define branch protection rules to the `main` branch
-   Enter `main` in Branch name pattern
-   Select `Require a pull request before merging`
-   Select `Require approvals`, set required number of approvals as 2

We're off to a great start. Let's add some more rules:

-   Select `Dismiss stale pull request approvals when commits are pushed`. This rule makes sure that if a pull request was approved and then new code was committed to the branch later that the approvals are removed and have to be requested again!
-   Scroll down and select `Include administrators`
-   Click `Create` and you're done!

<!-- <img width="1680" alt="Screen Shot 2021-11-16 at 9 05 03 AM" src="https://user-images.githubusercontent.com/7483633/142002092-7955c2ad-9259-4777-a523-acfa5c8ae6ea.png"> -->

<img width="1680" alt="Screen Shot 2021-11-16 at 9 05 50 AM" src="https://user-images.githubusercontent.com/7483633/142002107-b106671e-1bab-472a-896c-ea71e6950d7d.png">

<!-- <img width="1680" alt="Screen Shot 2021-11-16 at 9 06 22 AM" src="https://user-images.githubusercontent.com/7483633/142002124-9595a0e7-9ceb-4b4b-8871-5f586d05450b.png"> -->

# Group Practice

The follow steps will be performed by **all members** of the group:
## Make sure all group members & your TA are collaborators for the repository

* Using the Manage Access tab, the person who set up the repo should add all other group members and your TA as collaborators
* Everyone should accept the invites to be able to collaborate
<img width="1175" alt="Screen Shot 2021-11-18 at 4 18 28 PM" src="https://user-images.githubusercontent.com/16904546/142498266-223a661f-76f4-4ebe-8d33-dc8ed614d7f6.png">



## Create a new issue

In order to demonstrate what it's like to work with issues, you're going to create and assign yourself your first issue

### Let's get started

In the `Issues` tab:

-   Click `New Issue`
-   An option to select `Custom issue template` that you created earlier will appear
-   Click `Get started`

<!-- <img width="1680" alt="Screen Shot 2021-11-16 at 9 11 12 AM" src="https://user-images.githubusercontent.com/7483633/142002348-bba49d20-b1c2-4e91-9db8-6901690f056a.png"> -->

<img width="1680" alt="Screen Shot 2021-11-16 at 9 11 25 AM" src="https://user-images.githubusercontent.com/7483633/142002362-73f8332e-1dc9-4b76-912e-b28269d84d00.png">

-   Add the title: `Add [Your name] to README`
-   Fill out the details of the issue, use the template content as a guide (for the sake of learning tonight, this doesn't have to be a "real" issue -- you can make stuff up)

```
## Overview
<!-- Add description of the task -->
The project rubric requires that members add their names to the README.md
<!-- Add screenshots related to the task -->

## Technical Notes
<!-- Add details to relevant implementation that you think might be helpful -->
<!-- Add links to documentation -->
```

On the right-hand side of the page

-   Under `Projects`, link the project that you created earlier
-   Under `Assignees`, click `assign yourself`
-   Click `Submit new issue`

## Clone group repository

All members of the group clone the repository on their respective machines

## Create a branch for your assigned issue

Make sure you're on your local `main` branch by running:

```
git branch
```

Create a new branch that branches off your local copy of `main`

```
git checkout -b readme-update-[your first name]
```

Update `README.md` with your name

To stage your changes:

```
git add .
```

To commit your changes:

```
git commit -m "updated README with my name"
```

If you try to run:

```
git push
```

You will see an error like:

```
fatal: The current branch random has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin readme-update-[your first name]
```

This is because your branch only exists in your local repository and not the remote repository. Run the suggested command in the error message to both push up your new branch and its commits, you only have to push this way once!

## Create a pull request

In `Pull Requests` tab:

-   Click `New Request`
-   Select your branch from the dropdown so it looks like `base: main <- compare: your branch name`

On the right-hand side of the page

-   Under `Projects`, link the project that you created earlier
-   Under `Assignees`, assign all of your group members
-   Click `Create pull request`

More on creating [pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) from Github's documentation.

## Merge conflicts and you're off to a great start!

If there are merge conflicts with `main` your pull request will say `This branch has conflicts and must be resolved` above the `Merge pull request` button.

Resolve them and re-request review from your group members!

## Reviewing a pull request

Your group members may have requested your review, make sure to view `File Changes` to read over all the lines of code added in the pull request.

Click on `Review Changes` button and select `Approve` if you think it's ready to go! If the pull request has conflicts make sure to let your group member know with a comment.

More on reviewing [pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews) from Github's documentation.

# Follow up issues to work on

## Add `.gitignore` to your repository.

`.gitignore` helps you define the types of files and directories in your local repository that you do not want to push as part of your changes.

For example: virtual environment related files, your local sqlite instance after installing Django, pycache files generated by your python interpreter, etc.

Create the file:

* Open up your git repo locally from your computer and make a new file at the top level of the repo (i.e. where `README.md` is) called `.gitignore` 
* Make sure to start the filename with `.` -- this is a 'hidden' file

Open `.gitignore` in your editor and paste everything from the following [link](https://www.toptal.com/developers/gitignore/api/django).
* This stuff looks complicated, but it is really a huge list of different files/folders that can cause difficulties with git, and should not be tracked. Putting these in the `.gitignore` file will mean you won't have to deal with them!

Commit this new file and create a pull request!

Note: Make sure to call your virtual environment "venv" since`.gitignore` ignores this directory!

## Install dependencies and generate a `requirements.txt` file

This will be the file all members of the group will rely on to install exactly the same python packages to run Django!

Once other group members have created their virtual environment, they can install the same dependencies with:

```console
pip install -r requirements.txt
