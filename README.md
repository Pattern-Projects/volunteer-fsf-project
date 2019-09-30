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

### Implemented Features

### Features Left to Implement


## Technologies Used

This project makes use of the following technologies:
- [Django 1.11](https://docs.djangoproject.com/en/1.11/) is an open-source fullstack development framework.
    - [django.test](https://docs.djangoproject.com/en/1.11/topics/testing/) extends Python's unittest.
    - [Coverage.py 4.5.4](https://coverage.readthedocs.io/en/v4.5.x/) generates interactive HTML reports on the coverage of running a function across the project code. Used here for gauging effectiveness of testing
- [PostgreSQL](https://www.postgresql.org/) is an open-source relational DBMS that works well with **Heroku** and **Django**
- [gunicorn 19.9.0](https://gunicorn.org/) is a web server gateway interface that runs on **Python**
- [psycopg2 2.7.3.2](https://pypi.org/project/psycopg2/) is a PostgreSQL database adapter for **Python**
- [dj_database_url 0.5.0](https://pypi.org/project/dj-database-url/) is a simple helper to configure Django database using db url
- [Heroku](http://heroku.com) is a cloud platform as a service which allows easy deployment of this project and database

## Testing

The site was tested through a number of means:

### User Stories


## Deployment

To deploy your own instance of volunteer-fsf-project with a little effort.
It is suggested that you use [Heroku](http://heroku.com) for your deplyment as the project was developed with that in mind.

There are two ways of depling to heroku:
1. [Through heroku's web dashboard](#Heroku Web Dashboard Deployment) available on most OS
2. [Throught the heroku toolbelt](#Heroku Toolbelt Deployment) available on Ubuntu 16+

### Preparation for deployment

Deployment requires some preparation:
1. Clone the volunteer-fsf-project git repo onto your local machine
2. Open or Create a heroku account at heroku.com
3. Have an existing github account from github.com
 

### Heroku Web Dashboard Deployment

1. Create a new app on heroku.com - this will require a unique name
2. In the local repo open volunteer-fsf-project/volunteer-fsf-project/settings.py
3. Add the following to ALLOWED_HOSTS in the settings file:
    `'your_app_name.herokuapp.com'`
4. Save changes and commit with an apporpriate message.
5. Push to a new github repository in your account
6. In heroku app dashboard set automatic deplyment and select your repository
7. Click deploy branch

### Heroku Toolbelt Deployment

1. Open a new terminal in the local repo and install heroku toolbelt with:
    `sudo snap install --classic heroku`
2. Login to heroku using the toolbelt:
    `heroku login`
3. Create a new app project:
    `heroku create your_app_name`
4. In the local repo open volunteer-fsf-project/volunteer-fsf-project/settings.py
3. Add the following to ALLOWED_HOSTS in the settings file:
    `'your_app_name.herokuapp.com'`
4. Save changes and commit with an apporpriate message.
5. Push to heroku using:
    `git push heroku master`


## Credits

### Useful Links
[`$ pip freeze > requirements.txt` considered harmful](https://medium.com/@tomagee/pip-freeze-requirements-txt-considered-harmful-f0bce66cf895)
[django.test](https://docs.djangoproject.com/en/1.11/topics/testing/)

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