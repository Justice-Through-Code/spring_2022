# Todo List Part 2: Comments and Tags

In this challenge, you'll build on the Django todo list app from yesterday, adding the features gone over today in class.

## Challenge steps

### Setup

1. Download [this zip file](https://courseworks2.columbia.edu/courses/152667/files/folder/django_templates?preview=14099081) from Canvas containing the `todoproject_2.zip`. This is the code from the start of class today (with the forms and related content updated to use `ModelForm`s).
    - Unzip the file and make sure to put the whole directory into the `django_projects` directory
    - Run `python manage.py migrate` in the terminal to create and populate a database file
2. Make sure you have activated your virtual environment for django (and downloaded django inside of it)
3. Add a task or two to make sure they are populating correctly

### Build the Comment Model


`Comments Table`

-   `Task`s have a **one-to-many relationship** with Comments

| id | comment                        | task_id (foreign key) | created_at                       |
| -- | ------------------------------ | --------------------- | -------------------------------- |
| 1  | This was really rewarding!     | 1                     | 2022-04-12 19:51:58.105669+00:00 |
| 2  | Great book                     | 2                     | 2022-04-12 21:51:58.105669+00:00 |

1. Create a model called `Comment` that contains fields representing the columns in the table above. For `task` use the [ForeignKey](https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_one/) to manage this one-to-many relationship with the `Task` model.

2. Use the django shell to add some comments to specific tasks in the database (creating a comment form is out of scope for the challenge, but feel free to do so for practice!)
3. In your `TodoDetailView` view, after you get the `Task` object from the database, also get all of the comments for that task (`filter` the `Comment.objects` to only find the ones where `task=task`)
4. Send these comments to your HTML template via the context variable
5. In your `detail.html` template, display each comment for the given task, similarly to how we display all of the tasks on the `list.html` homepage


That's it! That's all that's required for this challenge, but we highly recommend also creating a `Tag` model and completing that portion of content from tonight's class as well, so that you've had practice with Many-to-Many relationships in Django as well.

## Nice work! Commit your work, push, and submit the link to the github repo on canvas

Nice job, you finished the challenge!
