# Blog app: Django challenge

In this challenge, you'll build on the Django blog app demonstrated in today's lesson to add a few more features!

## Challenge steps

### Setup

1. Download [this zip file](https://courseworks2.columbia.edu/courses/141443/files/folder/django_templates?preview=12442208) from Canvas containing the `blogproject-challenge.zip`. This is the code demonstrated during class today.
    - Unzip the file and make sure to put the whole directory into the `django_projects` directory inside personal directory in your pod repo
2. Make sure you're on a new branch in your pod repo _and_ make sure you have activated your virtual environment for django
3. In the project directory create a superuser and log into admin view
4. In the admin view, a) create two tags and b) create two posts and select one or two tags for each post. `http://127.0.0.1:8000/blog` should now display two posts and their tags

### Build the 'Create Post' page

5. Similar to the Edit Post page, build the Create Post page at `http://127.0.0.1:8000/blog/create` that contains a form to create new posts. Use the `EditorForm` to do this.

6. Update the `blog.html` template to now have a hyperlink on this page to the 'Create Post' page you made! Use an  anchor tag to point to `http://127.0.0.1:8000/blog/create` dynamically

7. Use the Create Post page to create some posts

### Adding comments related to a post

`Comments Table`

-   Posts have a **one-to-many relationship** with Comments
-   For the sake of simplicity, user information is not included in this table

| comment_id | comment                        | post_id (foreign key) |
| ---------- | ------------------------------ | --------------------- |
| 1          | Great post!                    | 1                     |
| 2          | A lot of insight in this post! | 2                     |

8. Create a model called `Comment` that contains fields representing the columns in the table above. For `post` use the [ForeignKey](https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_one/) to manage this one-to-many relationship with the `Post` model.

9. Register the `Comment` model to the admin view. 

10. Use the admin view to some comments to specific posts and you're done! (Don't worry about rendering comments on any of the pages in the blog, that's out of the scope of this challenge)

## Nice work! Commit your work, push, and send a pull request for your TA to review!

Nice job, you finished the challenge!
