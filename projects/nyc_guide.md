# Project 2: Build a New York City Guide in Django!

Welcome to the first group project of the semester! Students will work in groups of 2 to create a New York City Guide website. Check out the [link](https://evening-mountain-52044.herokuapp.com/) for the completed website.

<img width="1680" alt="Screen Shot 2021-10-28 at 8 30 23 AM" src="https://user-images.githubusercontent.com/7483633/139255652-20e5e9a3-7528-408c-949e-9b90fc3fbeb5.png">

### Sitemap and URLs

The structure of the web pages corresponds to the following (along with their URL paths):

-   **Home** `/`

    -   **Brooklyn** `/brooklyn`
        -   **Beaches** `/brooklyn/beaches`
            -   **Brighton Beach** `/brooklyn/beaches/brighton%20beach`
            -   **Coney Island** `/brooklyn/beaches/coney%20island`
            -   **Manhattan Beac**h `/brooklyn/beaches/manhattan%20beach`
    -   **Bronx** `/bronx`
        -   **Beaches** `/bronx/beaches`
            -   **Orchard Beach** `/bronx/beaches/orchard%20beach`
        -   **Zoos** `/bronx/zoos`
            -   **Bronx Zoo** `/bronx/zoos/bronx%20zoo`
    -   **Manhattan** `/manhattan`

        -   **Food** `/manhattan/food`

            -   **Cheeky Sandwiches** `/manhattan/food/cheeky%20sandwiches`
            -   **Katz's Delicatessen** `/manhattan/food/katz's%20delicatessen`
            -   **Veselka** `/manhattan/food/veselka`

        -   **Parks** `/manhattan/parks`
            -   **Central Park** `/manhattan/parks/central%20park`
            -   **Riverside Park** `/manhattan/parks/riverside%20park`
            -   **The High Line** `/manhattan/parks/the%20highline`
            -   **Washington Square Park** `/manhattan/parks/washington%20square%20park`

    -   **Queens** `/queens`
        -   **Airports** `/queens/airports`
            -   **John F Kennedy International Airport** `/queens/airports/john%20f%20kennedy%20international%20airport`
            -   **LaGuardia Airport** `/queens/airports/laguardia%20airport`
        -   **Beaches** `/queens/beaches`
            -   **Rockaway Beaches** `/queens/beaches/rockaway%20beaches`
    -   **Staten Island** `/staten%20island`
        -   **Beaches** `/staten%20island/beaches`
            -   **Cedar Grove Beach** `/staten%20island/beaches/cedar%20grove%20beach`
            -   **Midland Beach** `/staten%20island/beaches/midland%20beach`
            -   **South Beach** `/staten%20island/beaches/south%20beach`
            -   **Wolfe's Pond Beach** `/staten%20island/beaches/wolfe's%20pond%20beach`
        -   **Food** `/staten%20island/food`
            -   **Lee's Tavern** `/staten%20island/food/lee's%20tavern`
            -   **Ralph's Famous Italian Ices** `/staten%20island/food/ralph's%20famous%20italian%20ices`
            -   **Royal Crown Bakery** `/staten%20island/food/royal%20crown%20bakery`

# Getting Started

A Django project has already been scaffolded with a `nyc` app in this [repository](https://github.com/Justice-Through-Code/nyc-guide).
-   The data for this website is a dictionary called `boroughs` in `nyc/boroughs.py` already imported into `nyc/views.py`
-   Some parts of the website have already been implemented in Django:
    -   `nyc/urls.py` contain all the URLs required to handle all the route parameters highlighted in the site map
    -   Home and Borough pages are already implemented
        -   `nyc/views.py` has two views implemented for Home `/` and Borough `/<str:borough>` URLs
        -   `nyc/templates` has two templates implemented for the already implemented two views

## Create your group repository
The following steps can be carried out by one member of the team:
1. Download the already scaffolded Django project in this [repository](https://github.com/Justice-Through-Code/nyc-guide). as a zipped folder
<img width="904" alt="Screen Shot 2021-10-28 at 4 59 26 PM" src="https://user-images.githubusercontent.com/7483633/139334764-49f52bc5-4293-45da-a677-736ddfcfd8ce.png">

2. Unzip the contents of the zip folder

4. Delete the existing `README.md`

4. Create a new repository for the group on Github
<img width="801" alt="Screen Shot 2021-10-28 at 4 49 41 PM" src="https://user-images.githubusercontent.com/7483633/139334999-4075825f-e1b7-4462-9b6c-ebd5daa9c0b6.png">

6. Follow the instructions for "or create a new repository on the command line" to push up the Django project unzipped in step 2 to this new repository
<img width="1244" alt="Screen Shot 2021-10-28 at 4 50 20 PM" src="https://user-images.githubusercontent.com/7483633/139335229-2567012c-e79a-41f1-b216-f98ed4af5772.png">

7. Invite your group member(s) to the repository to start collaborating on the project!

# Project Requirements

## Technical

-   Implement the Activity page (view and template) rendered at URL `<str:borough>/<str:activity>` (i.e. list of beaches, parks, etc.)
-   Implement the Venue page (view and template) rendered at URL `<str:borough>/<str:activity>/<str:venue>` (i.e. details of a venue like like Brighton Beach, etc.)

## Submission

-   The link to the group repository will be submitted by one of the group members in [Courseworks](https://courseworks2.columbia.edu/courses/152667/assignments/775312)
-   The group repository must include a `README.md` markdown file. To format your markdown file beautifully, check out this [guide](https://www.markdownguide.org/basic-syntax) on markdown syntax
-   The `README.md` must contain the following information
    -   Name of project
    -   Names of group members and their Github usernames
    -   Instruction on how to create and run a virtual environment using `venv`
    -   Instruction on how to install project dependencies with `pip`
    -   Instruction on how to run the Django application
-   The commit history in Github should show equal contributions from both group members

## Helpful Topics to Review
- Python data structures like Lists, Dictionaries and their methods
- Python Classes and Inheritance
- Django [URLs](https://docs.djangoproject.com/en/3.2/topics/http/urls/) to understand how to capture parameters in your views
- Django [Templates](https://docs.djangoproject.com/en/3.2/ref/templates/language/)

## Rubric For Evaluation (25 points total)

Category | Requirement | Points      |   Description  |
| -----------  | ----------- | ----------- | ----------- |
Github | Github repo is public &  submitted to canvas | 1 | Make sure the JTC team can easily access your submission!
README | Github repo includes `README.md` on main branch | 3 | README uses [Markdown formatting](https://www.markdownguide.org/cheat-sheet/) for clear organization. README has name of project, names of group members, instructions on how to make/run a virtual environment with `venv` and install all code dependencies with `pip` & *instructions on how to run the Django app*.
Documentation | Code is well-commented | 2 | Python code should have comments with relevant explanations where needed. Comments should demonstrate understanding of the code and make functionality clear to anyone new to the project.
Collaboration | Both group members are committing python code | 2 | Github repo commit history shows that both members are contributing to code equally
DRY Design| Templates & dynamic URLs used properly to avoid repeated code | 3 | App should only have 1 HTML template for all activities, and 1 HTML template for all venues. HTML templates should use the [Django URL template tag](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#std:templatetag-url), and *no links should be hard-coded*
Sitemap | All URLs exist | 2 | All links specified in the assignment sitemap (see [Sitemap and URLs](#sitemap-and-urls) above) work without errors
Activity URLs  | Activity URLs linked correctly from borough pages| 3 | All links to activities listed on each borough page go to the correct corresponding activity page (for example clicking "beaches" on the "Brooklyn" page goes to `/brooklyn/beaches`) as created in the nested data structure in [`boroughs.py`](https://github.com/Justice-Through-Code/nyc-guide/blob/main/nyc/boroughs.py)
Activity Display  | Each activity page displays correct info | 3 | Activity pages all display a list of the correct venues for that activity (only in the correct borough -- i.e. `/bronx/beaches` should not display beaches in Brooklyn or Queens) as specified by the data in [`boroughs.py`](https://github.com/Justice-Through-Code/nyc-guide/blob/main/nyc/boroughs.py). Activity page should also have a header displaying the activity type (i.e. "Beaches")
Venue URLs | Venue URLs linked correctly from activities pages | 3| All links to venues listed on each activity page go to the correct corresponding venue page (for example clicking "Brighton Beach" on the `/brooklyn/beaches` page goes to `/brooklyn/beaches/brighton%20beach`) as in [`boroughs.py`](https://github.com/Justice-Through-Code/nyc-guide/blob/main/nyc/boroughs.py)
Venue Display  | Each venue displays correct info | 3 | Venue pages should display a header with the name of the correct venue, and a paragraph of text with the description of the venue specified in the data in [`boroughs.py`](https://github.com/Justice-Through-Code/nyc-guide/blob/main/nyc/boroughs.py)
