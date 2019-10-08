# volunteer-fsf-project

A site for volunteers to find volunteering opportunities around the world.
Data from volunteer work camps will be displayed and can be applied to by paying a small fee.

## License

The project is shared for use with the [GNU General Public License v3](https://github.com/Pattern-Projects/oireachtas-ifd-project/blob/master/LICENSE)

>   This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.


## UX

<!--Responsive Views of Home Page-->
![Responsive image missing](documentation/Responsive.png)

### Users

Expected users of the website include

### User Stories

1.

### Design

<!--- Gold circles representing the seats of the Oireachtas-->
![Website Logo Missing](documentation/logo.png)
- Colour scheme consists of complementary colours
- roboto font used throughout the website
    - font-family: 'Roboto', 'helvetica' sans-serif;

### Mockups

The web app is a single page with different displays given for different functions:
- [Mockup Missing]()
- [Mockup Missing]()
- [Mockup Missing]()


## Features

Features planned, implemented and outlined for later development

### Planned Features
- Camps list
- Filters
    - Region
    - Country
    - Topic
    - Type of Work
    - Setting
    - Dates
    - Special requirements
    - Number of Places Available
- Searchable
- Translatable Pages
- Membership Sign Up
- Newsletter and Blog
- Newsletter Signup
- Login Authentication
- Documentation
    - README
    - Doc Strings


### Implemented Features
- Camps list
- Authentication
    - Logout
    - Login
### Features Left to Implement


## Technologies Used

This project makes use of the following technologies:
- [Python 3.6.8](https://www.python.org/) is a general purpose programming language.
- [Django 1.11](https://docs.djangoproject.com/en/1.11/) is an open-source fullstack development framework.
    - [django.test](https://docs.djangoproject.com/en/1.11/topics/testing/) extends Python's unittest.
    - [Coverage.py 4.5.4](https://coverage.readthedocs.io/en/v4.5.x/) generates interactive HTML reports on the coverage of running a function across the project code. Used here for gauging effectiveness of testing
- [PostgreSQL](https://www.postgresql.org/) is an open-source relational DBMS that works well with **Heroku** and **Django**
- [gunicorn 19.9.0](https://gunicorn.org/) is a web server gateway interface that runs on **Python**
- [psycopg2 2.7.3.2](https://pypi.org/project/psycopg2/) is a PostgreSQL database adapter for **Python**
- [dj_database_url 0.5.0](https://pypi.org/project/dj-database-url/) is a simple helper to configure Django database using db url
- [Heroku](http://heroku.com) is a cloud platform as a service which allows easy deployment of this project and database
- [Heroku Toolbelt](https://devcenter.heroku.com/articles/heroku-cli) connects to Heroku through a terminal
- [Gitpod](gitpod.io) is an in browser IDE that can open and setup git repositories directly from github
- [AWS Cloud9](https://www.awseducate.com/signin/SiteLogin) IDE services from Amazon and connecting into their suite of products.

## Developement

### Heroku
Heroku provides a number of useful tools to aid in development

#### Heroku Postgres Add-on
Databases can be created and hosted on heroku using their built in PostgreSQL add-ons.

#### Dataclips
The Heorku Postgres add-on allows for secure links to SQL quries of the database known as dataclips. They are great for quick referencing of the database and sharing of specific data across teams.
Following the provided links quickly exports and downloads the current data quiry results to you computer or a Google Sheets account.
Example:
- All available camps
    - [CSV](https://data.heroku.com/dataclips/sedlidytgswqyydiviezgqoozuql.csv?access-token=d2641951-1bcf-4669-b49f-04efebb0c44c)
    - [JSON](https://data.heroku.com/dataclips/sedlidytgswqyydiviezgqoozuql.json?access-token=d2641951-1bcf-4669-b49f-04efebb0c44c)
    - Google Sheets - paste provided macro into your sheet:
        ```=IMPORTDATA("https://data.heroku.com/dataclips/sedlidytgswqyydiviezgqoozuql.csv?access-token=d2641951-1bcf-4669-b49f-04efebb0c44c")```


## Testing

The site was tested through a number of means:

### User Stories

### Django TestCase

You can run theses tests by first following the steps in Deployment to get the project running.
Ensure that the dependencies are installed.
Next in a terminal inside the project type:
    `coverage manage.py test`
When the tests are complete you will be provided a report on the pass rate of the program methods. This should be 100%.
To view an interactive HTML display of the coverage of code tested run this in the terminal:
    `coverage html`
When the command completes open the report in a web browser:


## Deployment

To deploy your own instance of volunteer-fsf-project take a little effort.
It is suggested that you use [Heroku](http://heroku.com) for your deplyment as the project was developed with that in mind.

>>> Some work required here - with config vars some of these steps aren't required <<<

Deployment requires some preparation. Before following the steps below ensure you have done the following:
1. A development environment with Python 3.6.8 or higher installed
1. Open or Create a Heroku account at heroku.com
2. Have an existing Github account from github.com
3. Fork a copy of volunteer-fsf-project to you github
4. You have generated a secret key - can be generated [here](https://miniwebtool.com/django-secret-key-generator/)

### Deploying to Heroku hosting service

There are two ways of deploying to Heroku:
1. [Through Heroku's Web Dashboard](#Heroku-Web-Dashboard-Deployment) available on most OS
2. [Through the Heroku Toolbelt](#Heroku-Toolbelt-Deployment) available on Ubuntu 16+

#### Heroku Web Dashboard Deployment

1. Create a new app on heroku.com - this will require a unique name
2. In the Overview tab add the **Heroku Posgres: Hobby Dev** add-on
3. In the Settings tab Reveal Config Vars add the following values:
    - `DISABLE_COLLECTSTATIC : 1`
    - `HOSTNAME : your_app_name.herokuapp.com`
    - `SECRET_KEY : your_secret_key`
4. On the Deployment tab set deployment method to Github
5. In the connect to Github section sign in then connect your fork of the project
6. With master branch selected, turn on Automatic Deploys
7. In the Manual Deploy section, with the master branch selected, click Deploy Branch for your first deployment

Your project is now deployed! To view the running app click Open App at the top of the page. It may take a moment to open when visiting after a time of inactivity.

#### Heroku Toolbelt Deployment

1. Clone your fork of the volunteer-fsf-project git repo onto your developement environment
2. Navigate inside the project:
    `cd volunteer-fsf-project`
3. Open a new terminal in the local repo and install heroku toolbelt with:
    `sudo snap install --classic heroku`
4. Login to heroku using the toolbelt:
    `heroku login`
5. Create a new app project:
    `heroku create your_app_name`
6. Point toolbelt to the created project with:
    `heroku git:remote -a your_app_name`
7. Connect a Postgres: Hobby Dev Add-on with:
    `heroku addons:create heroku-postgresql:hobby-dev`
8. Retrieve the DATABASE_URL to ensure it is connected:
    `heroku config:get DATABASE_URL`
9. Set the following config vars:
    - `heroku config:set DISABLE_COLLECTSTATIC=1`
    - `heroku config:set HOSTNAME=your_app_name.herokuapp.com`
    - `heroku config:set SECRET_KEY=your_secret_key`
10. Push to heroku using:
    `git push heroku master`

Your project is now deployed! Visit `https://your_app_name.herokuapp.com/` to view the site. It may take a moment to open when visiting after a time of inactivity.

### Running Locally
To run the project locally.
Using a development environment with Python 3.6.8 or higher installed
Clone your fork of the volunteer-fsf-project git repo onto your developement environment
Open the project and install the dependencies:
    `pip3 install -r requirements.txt`
Apply any migrations:
    `python3 manage.py migrate`
In the terminal export the following values:
    `export DEVELOPMENT=1`
    `export SECRET_KEY='your_secret_key'`
Next run the project:
    `python3 manage.py runserver`

Your project is now running! To view the project open it in a web browser.

### Running with Gitpod
Open the forked volunteer-fsf-project page on github.com
Prefix the url with the following:
    `gitpod.io/#`
Gitpod will create an environment for you in a couple minutes
When the IDE is ready, in the terminal install dependencies:
    `pip3 install -r requirements.txt`
Apply any migrations:
    `python3 manage.py migrate`
In the terminal export the following values:
    `export DEVELOPMENT=1`
    `export SECRET_KEY='your_secret_key'`
Next run the project:
    `python3 manage.py runserver`

Your project is now running! To view the project open it in Preview.

## Credits

### Useful Links
- [`$ pip freeze > requirements.txt` considered harmful](https://medium.com/@tomagee/pip-freeze-requirements-txt-considered-harmful-f0bce66cf895)
- [django.test](https://docs.djangoproject.com/en/1.11/topics/testing/)
- [Process Types and the Procfile](https://pythonhosted.org/deis/using_deis/process-types/)
- [Github Markdown Header Anchors](https://gist.github.com/asabaylus/3071099)
- [.gitignore not ignoring the files specified.](https://github.community/t5/How-to-use-Git-and-GitHub/gitignore-not-ignoring-the-files-specified/td-p/11055)
- [How can I change the author name / email of a commit?](https://www.git-tower.com/learn/git/faq/change-author-name-email)
- [VI Text Editor with Commands: Linux/Unix Tutorial](https://www.guru99.com/the-vi-editor.html)
- [Gitpod - Environment Variables](https://www.gitpod.io/docs/47_environment_variables/)
- [Docstrings in Python](https://www.datacamp.com/community/tutorials/docstrings-python)

### Content
The text on the website has been copied and edited from:

### Media
The images for the website are taken from:
[Pexels](https://www.pexels.com/)

### Acknowledgements
Thank you to the following for inspiration, motivation and the direction I needed:
- Seun Owonikoko    @seun_mentor
- Samantha Dartnall @Sammy Dartnall
- Code Institute