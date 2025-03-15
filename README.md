# Neo Portfolio

## DJ Start Guide

* Main files you will work on are in `core/templates`, `core/templatetags` and `static/scss/main.scss`
* Django, unlike React, does not have components, instead it is a template language, which can basically work the same but is slightly different. Template languages usually "extend" an existing form of text editing to make it more powerful. That is what Django does with `.html` files, it lets you write if-statements, for loops, etc. in `.html` files. React lets you write `.html` in `.js` files, which is `.jsx`, so it's not quite the same. Please refer to the link below for Django template language documentation
* The other thing is tags and filters. Given a variable in Django Template Language (DTL) file, you can apply tags and filters to it to do more interesting things. I already created a filter I know we need. Please refer to the links below on how to work with tags and filters.
* The idea that I have to make the code as simple as possible (maybe I am wrong), is to have a single `list.html` file. Because this website is essentially going to be a list of a bunch of cards and they will kind of all look the same, I created one `list.html` where you will check which type of object you are dealing with, and then `include` its correct `card.html` file (which are all empty for now).
* Another important thing is to include delete and update buttons on all the cards. However these buttons are only going to be visible if `request.user.issuperuser` (a.k.a me). So keep that in mind when designing. These buttons should open a new tab to the correct `/admin` link.
* Right now, all of bootstrap is being imported. So if you could do some extra research and only import what is needed, is going to help a lot with website speed!
* Please refer to the `models.png` image to understand what each model can display. I understand that each of the models is likely having more attributes than it should have, so feel free to make tough choices into what your UI can actually accomodate (the more the better) (i.e. maybe certificates shouldn't have images associated with them after all, but I still included it there just in case).
* Because all of the fields are optional and are likely not always going to be filled in, your UI may (if you decide that) have to accomodate fields when they are and are not filled in. (But if you choose that it's easier to just force me to have certain fields and not others and whatnot, do whatever you want...)

## Developer Quick Start

### Initial Setup

1. Create virtual environment: `python -m venv .venv`
2. Start env: `source .venv/bin/activate`
3. Install requirements: `pip install -r requirements.txt`
4. Create `.env` file in root and add `DEBUG=False` and `SECRET=` variable (ask Rafael for secret)
5. Create database: `python manage.py migrate`
6. Populate database: `python del.py`
7. Create superuser (optional): `python manage.py createsuperuser`
8. Run local server `python manage.py runserver`
9. Manage objects at `/admin`

### Contributing

Note: this is critical to avoid lost progress!

1. Ensure your local repo is up to date: `git pull`
2. You may have to repeat the "Initial Setup" steps
3. Make changes
4. Stash your current changes: `git stash`
5. Check again if local repo is up to date: `git pull`
6. Resolve merge conflicts locally
7. Stage changes: `git add <files>`
8. Make commit: `git commit -m "<message>"`
9. Push changes: `git push`

## Helpful Stuff

### Auto formatter

* Install Ruff auto formatter VSCode extension
* Press `cmd+shift+p` and go to `Open User Settings (JSON)`
* Add the following config to it `"ruff.lineLength": 79,`  
  
* Install Django VSCode extensions: Django, Django Template, and djLint (look for most downloaded)
  
* [Django template language](https://docs.djangoproject.com/en/5.1/ref/templates/language/)
* [Django filters](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/)
* [Make your own filters](https://docs.djangoproject.com/en/5.1/howto/custom-template-tags/)
* [Bootstrap documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

## Deployment

1. Create a `.env` file and add the `DEBUG` and `SECRET` variables.
2. Run `python manage.py collectstatic`
