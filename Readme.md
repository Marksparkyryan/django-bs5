## Experimenting with Bootstrap/Django integration 

### [main branch]: Will be changing this to a blank Django project (don't use yet)

### [no-bundler branch]: The no task-runner/bundler solution
1. Create a local project folder and cd into it
2. `git clone git@github.com:Marksparkyryan/django-bs5.git` or `git clone https://github.com/Marksparkyryan/django-bs5.git`
3. `python3 -m venv env`
4. `source env/bin/activate`
5. `pip3 install -r django-bs5/requirements.txt`
7. In a new terminal tab, navigate to django-bs5/bs5 and `npm run bootstrap`
8. In the original tab, navigate to django-bs5/djangoproject and `python3 manage.py runserver`
