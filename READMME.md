# URL Shortener With Django

This repo is used to make your own url shortener website, escpesially for my website, hehe. This project is using django in a simple way.

## Live Demo

[gpr.web.id](http://gpr.web.id/)

## Prereq

1. Create and activate your virtual environment
2. Install requirements
   ```bash
   pip install -r requirements.txt
   ```
3. Add your own secret key in virtual environment
   ```text
   SECRET_KEY="yoursecretkey"
   export SECRET_KEY
   ```

## How to use

1. Migrate database
   ```python3
   python manage.py migrate
   ```
2. Create super user for admin login
   ```python3
   python manage.py createsuperuser
   ```
3. Run your django app
   ```python3
   python manage.py runserver
   ```
4. Go to admin dashboard
   ```text
   http://<yourlocalserver>/admin/
   ```
5. Add your shorten url in shorten links database
6. You can also edit template html in `/shorten/templates`
7. If you want to deploy this app, just change the settings according to your
   needs

## How to contribute

There is a bug or you want to contribute?

Just make pull request in this repo.
