# Setting up your Python web development environment

## 0. What is a virtual environment?

-   Virtual environments let us manage _different versions of python_ and different sets of libraries on our computer at the same time
-   This is really helpful when we might need a certain set of python tools for one project, and different set of tools for a different project
-   When you make virtual environments and install new libraries, in general those libraries are only installed _for that environment_ -- so we can avoid conflict!

## 1. Create virtual environment

Virtual environment helps us isolate Python packages from other projects so we don't run into conflicts. Python3 has a module named `venv` to create virtual environments. Check out the [official documentation](https://docs.python.org/3/tutorial/venv.html) for more information on `venv`.

We are going to create a virtual environment with the name `django-env`:

-   FIRST, create the directory you'll want to use your environment in! The files for running the virtual environment will be saved in this directory, so remember its location!

```
mkdir django-projects
cd django-projects
```

Inside `django-projects` run the following:

```
python3 -m venv django-env
```

Now, if you print the contents of the working directory (i.e. with `ls`) you can see that a subdirectory containing the files you need for the environment has been added.

-   You shouldn't ever need to _go into that folder_, but it is important to remember where it is for the next step of activating the environment

## 2. Run virtual environment

### On Windows:

Windows Powershell users:

```
django-env\Scripts\activate.bat
```
Bash users:
```
source django-env/Scripts/activate
```
### On Unix or MacOS:

```
source django-env/bin/activate
```

## 3. Install Django

Django is the Python web framework we will use to build websites!

```
pip install django
```

## 4. Create a `requirements.txt` file

This file will specify all the installed Python packages in the environment. Let's use a pip command to generate this:

```
pip freeze > requirements.txt
```

Take a peek!

```
cat requirements.txt
```

## Just so you know!

You can leave the virtual environment when you are done working by running:

```
deactivate
```

# Conclusion

Great! We've completed setting up our Python web development environment. Now we can move onto the exciting stuff: Building websites!
