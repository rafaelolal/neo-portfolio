# Neo Portfolio

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
