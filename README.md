# volunteer-fsf-project [![Build Status](https://travis-ci.org/Pattern-Projects/volunteer-fsf-project.svg?branch=master)](https://travis-ci.org/Pattern-Projects/volunteer-fsf-project)

A site for volunteers to find volunteering opportunities around the world.
Data from volunteer work camps will be displayed and can be applied to by paying a small fee.

- [Development Pipeline Version](https://volunteer-fsf-development.herokuapp.com/)  
- [Evaluation Pipeline Version](https://volunteer-fsf-project.herokuapp.com/)  

Please check the [wiki](https://github.com/Pattern-Projects/volunteer-fsf-project/wiki) for tips on how to use the website.

[Root access login details for Evaluation.](https://github.com/Pattern-Projects/volunteer-fsf-project/wiki/Evaluation)
## License

The project is shared for use with the [GNU General Public License v3](https://github.com/Pattern-Projects/volunteer-fsf-project/blob/master/LICENSE)

>   This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

## UX

<!--Responsive Views of Home Page-->
![Responsive image](media/img/homescreen.png)

### Users

Expected users of the website include volunteer camp organisers, voluntary organisations and volunteers of all kinds. They come to the site to participate in volunteering activities.

### User Stories

1. Volunteer Camp Organisers can notify the voluntary organistaion of their camp.
2. Volunteer organisations can list the camps on the site.
3. Volunteers looking for a work camp experience can apply to work at the camp.

### Design

<!--- Gold circles representing the seats of the Oireachtas-->
- Colour scheme consists of complementary colours
- roboto font used throughout the website
    - font-family: 'Roboto', 'helvetica' sans-serif;
- Icons imported from Font FontAwesome
- Designed for accessibility:
    - Semantic structure
    - Alt text
    - Colour Contrast

### Mockups

The web app was designed with a series of mockups as a dynamic page with different displays given for different views:
- [Base](https://www.figma.com/file/St1YNKFGOfqXLi6pbS0Epc/Volunteer?node-id=0%3A1)
- [Base - Mobile Portrait](https://www.figma.com/file/St1YNKFGOfqXLi6pbS0Epc/Volunteer?node-id=14%3A2)
- [Base - Mobile Landscape](https://www.figma.com/file/St1YNKFGOfqXLi6pbS0Epc/Volunteer?node-id=14%3A305)

- [Camps](https://www.figma.com/file/St1YNKFGOfqXLi6pbS0Epc/Volunteer?node-id=7%3A26)
- [Camp](https://www.figma.com/file/St1YNKFGOfqXLi6pbS0Epc/Volunteer?node-id=7%3A202)
- [Travel](https://www.figma.com/file/St1YNKFGOfqXLi6pbS0Epc/Volunteer?node-id=9%3A1988)
- [News](https://www.figma.com/file/St1YNKFGOfqXLi6pbS0Epc/Volunteer?node-id=7%3A702)
- [News Event](https://www.figma.com/file/St1YNKFGOfqXLi6pbS0Epc/Volunteer?node-id=9%3A1753)
- [Stories](https://www.figma.com/file/St1YNKFGOfqXLi6pbS0Epc/Volunteer?node-id=9%3A2235)
- [Story](https://www.figma.com/file/St1YNKFGOfqXLi6pbS0Epc/Volunteer?node-id=9%3A2157)
- [Profile](https://www.figma.com/file/St1YNKFGOfqXLi6pbS0Epc/Volunteer?node-id=9%3A2405)

### Camp Structure
The camp model is structured in the following way:
#### Camp information:
- title
- region
- country
- continent
- organisation
- description
- image

#### Camp Details:
- positions
- positions_female
- positions_male
- positions_other
- required_language
- start_date
- end_date
- extra_host_country_fee
- extra_host_country_fee_currency

#### Camp Organising Data:
- archived
- created_date
- published_date
- tag

Other models include:
- Order
- News
- Story
- User

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
- Profile Page
- Cart for camps
- Camp checkout
- Strip payments

### Features Left to Implement
- Camp Filtering
- Image uploads

## Technologies Used

This project makes use of the following technologies:
- [Python 3.6.8](https://www.python.org/) is a general purpose programming language.
- [Django 1.11](https://docs.djangoproject.com/en/1.11/) is an open-source fullstack development framework.
    - [django.test](https://docs.djangoproject.com/en/1.11/topics/testing/) extends Python's unittest.
    - [Coverage.py 4.5.4](https://coverage.readthedocs.io/en/v4.5.x/) generates interactive HTML reports on the coverage of running a function across the project code. Used here for gauging effectiveness of testing.
- [PostgreSQL](https://www.postgresql.org/) is an open-source relational DBMS that works well with **Heroku** and **Django**.
- [Heroku](http://heroku.com) is a cloud platform as a service which allows easy deployment of this project and database.
- [Heroku Toolbelt](https://devcenter.heroku.com/articles/heroku-cli) connects to Heroku through a terminal.
- [Gitpod](gitpod.io) is an in browser IDE that can open and setup git repositories directly from github.
- [Azure](https://azure.microsoft.com/) IDE services from Microsoft and connecting into their suite of hosting products.
- [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/) CSS styling from **Bootstrap**.
- [Font Awsome](https://fontawesome.com/) provide neat icons with easy styling.
- [Travis CI](https://travis-ci.org/) Continuous Integration from **Travis**.
- [Stripe](https://stripe.com/) is used for recieving payments.

### Dependencies
- [gunicorn 19.9.0](https://gunicorn.org/) is a web server gateway interface that runs on **Python**.
- [psycopg2 2.7.3.2](https://pypi.org/project/psycopg2/) is a PostgreSQL database adapter for **Python**.
- [dj_database_url 0.5.0](https://pypi.org/project/dj-database-url/) is a simple helper to configure Django database using db url.
- [Django Forms Bootstrap](https://github.com/pinax/django-forms-bootstrap) this plug-in allows for bootstrap styling on django forms.
- [Datepicker](https://fengyuanchen.github.io/datepicker/) popup calander date picker

## Developement

### Git Flow
Development Version Control workflow follows these steps:
- New `feature` branches are branched from the `develop` branch
- `feature` is developed over a development cycle
- `feature` branch is tested with coverage
- `feature` branch is pushed to remote
- `feature` branch is merged into `develop` branch
- `feature` branch is deleted from local
- `release` branch is branched from `develop` branch
- `release` branch is tagged with projects latest release version
- `release` branch is tested with django TestCase
- Bug fixes and patches are added if required
- `release` branch is merged into `develop` branch
- `release` branch is deleted
- `develop` branch is pushed to remote
- `develop` branch is merged into `master` branch
- `master` branch is pushed to remote
- Travis tests Continuous Integration on latest `master` push
- Heroku creates new build from latest `master` push

Note: `feature` branches can be removed from remote after merging with `develop` branch. They have been retained here for assessment purposes.

### Test Driven Development
Features are developed using Test Driven Development practices:
- `feature` branch is branched from `develop` branch
- `feature` branch is tested with Django TestCase for pass standard
- `feature` is broken into stages, tests are written for each stages
- Stages are developed until they pass stage tests
- Good time to commit to git
- When all stages are complete:
    - feature branch is tested with `coverage` to ensure high level of test coverage
    - `feature` branch is ready to merge with develop branch

### Styling
**Bootstrap** CSS is added to the project through a CDN link in the base.html <head> tag.
Icons are imported from **FontAwesome** using their new kit system

### Heroku
Heroku provides a number of useful tools to aid in development

#### Heroku Postgres Add-on
Databases can be created and hosted on heroku using their built in **PostgreSQL** add-ons.

#### Pipeline Developement
Allows for staging of the development version app alongside the production ready app.
New features added to the development app can be tested on the staged apps without directly affecting the
user experience of the production version.

#### Dataclips
The Heorku Postgres add-on allows for secure links to SQL queries of the database known as dataclips. They are great for quick referencing of the database and sharing of specific data across teams.
Following the provided links quickly exports and downloads the current data quiry results to you computer or a Google Sheets account.
Example:
- All available camps
    - [CSV](https://data.heroku.com/dataclips/sedlidytgswqyydiviezgqoozuql.csv?access-token=d2641951-1bcf-4669-b49f-04efebb0c44c)
    - [JSON](https://data.heroku.com/dataclips/sedlidytgswqyydiviezgqoozuql.json?access-token=d2641951-1bcf-4669-b49f-04efebb0c44c)
    - Google Sheets - paste provided macro into your sheet:
        - ```=IMPORTDATA("https://data.heroku.com/dataclips/sedlidytgswqyydiviezgqoozuql.csv?access-token=d2641951-1bcf-4669-b49f-04efebb0c44c")```

## Testing

The site was tested through a number of means:

### User Stories

1. Volunteer Camp Organisers can notify the voluntary organistaion of their camp.
2. Volunteer organisations can list the camps on the site.
3. Volunteers looking for a work camp experience can apply to work at the camp.

### Django TestCase

You can run theses tests by first following the steps in Deployment to get the project running.
- Ensure that the dependencies are installed.
    - `pip3 install -r requirements.txt`
- Next in a terminal inside the project type:
    - `coverage run --source=. manage.py test`
- When the tests are complete you can generate a report on the pass rate of the program methods.
    - `coverage report`
- To view an interactive HTML display of the coverage of code tested run this in the terminal:
    - `coverage html`
- When the command completes open the report in a web browser:

### Travis - Continuous Integration

[![Build Status](https://travis-ci.org/Pattern-Projects/volunteer-fsf-project.svg?branch=master)](https://travis-ci.org/Pattern-Projects/volunteer-fsf-project)
Continuous Integration will run all the written Django TestCases against the latest updates to the project.
You can set up Travis CI with your project by first following the steps in Deployment to get the project running.
- Create an account at [Travis CI](travis-ci.org)
- Connect to your Github account
- From Setting > Repositories activate your project
- Travis will now run CI tests each time you push changes to your repository
Note: You can instruct Heroku to wait for CI to complete before publishing changes to the site by ticking the 'Wait for CI to pass before deploy' checkbox in Heroku's deploy tab.

## Deployment

To deploy your own instance of volunteer-fsf-project takes a little effort.
It is suggested that you use [Heroku](http://heroku.com) for your deplyment as the project was developed with that in mind.

Deployment requires some preparation. Before following the steps below ensure you have the following:
1. A development environment with Python 3.6.8 or higher installed
1. Open or Create a Heroku account at heroku.com
2. Have an existing Github account from github.com
3. Fork a copy of volunteer-fsf-project to you github
4. Generate a secret key - can be generated [here](https://miniwebtool.com/django-secret-key-generator/)

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
    - `AZURE_ACCOUNT_NAME : volunteerfsfproject`
4. On the Deployment tab set deployment method to Github
5. In the connect to Github section sign in then connect your fork of the project
6. With master branch selected, turn on Automatic Deploys
    - Ticking the 'Wait for CI to pass before deploy' checkbox here will help prevent broken deployments.
7. In the Manual Deploy section, with the master branch selected, click Deploy Branch for your first deployment

Your project is now deployed! To view the running app click Open App at the top of the page. It may take a moment to open when visiting after a time of inactivity.

#### Heroku Toolbelt Deployment

1. Clone your fork of the volunteer-fsf-project git repo onto your developement environment
2. Navigate inside the project:
    - `cd volunteer-fsf-project`
3. Open a new terminal in the local repo and install heroku toolbelt with:
    - `sudo snap install --classic heroku`
4. Login to heroku using the toolbelt:
    - `heroku login`
5. Create a new app project:
    - `heroku create your_app_name`
6. Point toolbelt to the created project with:
    - `heroku git:remote -a your_app_name`
7. Connect a Postgres: Hobby Dev Add-on with:
    - `heroku addons:create heroku-postgresql:hobby-dev`
8. Retrieve the DATABASE_URL to ensure it is connected:
    - `heroku config:get DATABASE_URL`
9. Set the following config vars:
    - `heroku config:set DISABLE_COLLECTSTATIC=1`
    - `heroku config:set HOSTNAME=your_app_name.herokuapp.com`
    - `heroku config:set SECRET_KEY=your_secret_key`
10. Push to heroku using:
    - `git push heroku master`

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
Djangos built in server is not meant for deployed hosting. Please consider another server for this.

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

## Bugs

### Resolved
#### Developer Tools Alerts
A number of alerts appeared in developer tools warning of cross-site cookies.  
Resolved: It turns out this was a universal issue across all sites and a number of browsers.  
Fixing this is outside the scope of this project.

#### Server 500 on evaluation site
Clicking any links on the evalutaion site was causing the page to 404.
Resolved: This was an easy fix. Required adding of stripe keys to config vars.

#### Checkout error on cart empty
The checkout process was hitting a snag.
Resolved: Checkout page does not include checkout ability when cart is empty.

## Credits
This project is developed with the aid of resources, advice and care from many others. Here's to them.

### Useful Links
- [Django 1.11 Documentation](https://docs.djangoproject.com/en/1.11/)
- [`$ pip freeze > requirements.txt` considered harmful](https://medium.com/@tomagee/pip-freeze-requirements-txt-considered-harmful-f0bce66cf895)
- [django.test](https://docs.djangoproject.com/en/1.11/topics/testing/)
- [Process Types and the Procfile](https://pythonhosted.org/deis/using_deis/process-types/)
- [Github Markdown Header Anchors](https://gist.github.com/asabaylus/3071099)
- [.gitignore not ignoring the files specified.](https://github.community/t5/How-to-use-Git-and-GitHub/gitignore-not-ignoring-the-files-specified/td-p/11055)
- [How can I change the author name / email of a commit?](https://www.git-tower.com/learn/git/faq/change-author-name-email)
- [VI Text Editor with Commands: Linux/Unix Tutorial](https://www.guru99.com/the-vi-editor.html)
- [Gitpod - Environment Variables](https://www.gitpod.io/docs/47_environment_variables/)
- [Docstrings in Python](https://www.datacamp.com/community/tutorials/docstrings-python)
- [Heroku Case Study - Life.io - Dataclips](https://www.heroku.com/customers/lifeio?c=7013A000002ILZjQAO&utm_campaign=Dataclips%20-%20Email&utm_medium=email&utm_source=nurture&utm_content=customers&utm_term=lifeio#heroku-dataclips)
- [StackOverflow - Git pull from another repository](https://stackoverflow.com/questions/24815952/git-pull-from-another-repository/24816134#24816134)
- [Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
- [Best Practices When Versioning a Release](https://blog.codeship.com/best-practices-when-versioning-a-release/)
- [How to Use Date Picker with Django](https://simpleisbetterthancomplex.com/tutorial/2019/01/03/how-to-use-date-picker-with-django.html#fengyuan-chens-datepicker)

### Content
The text on the website has been copied and edited from:

### Media
The images for the website are taken from:
[Pexels](https://www.pexels.com/)

### Acknowledgements
Thank you to the following for inspiration, motivation and the direction I needed:
- Seun Owonikoko    @seun_mentor

- Samantha Dartnall @Sammy Dartnall
- Alan M.           @Alan Mc Gee
- Anna Greaves      @Anna_G
- Andy              @mormoran
- Libby Henry       @Libby_alumni
- Jorden V          @Jorden
- Samantha Dartnall @Sammy Dartnall_lead
- John Lynch        @John_Lynch_alumnus
- Antonio Augello   @Antonio
- Anybody that I may have forgotten

- Code Institute
