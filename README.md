# Django Custom Management Commands
Django Custom Management Commands. In Django project, We could manage by executing some commands which could be invoked through the manage.py.

What is DJango
------
> It is "a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source".

What is Django Custom Management Commands
------
> In Django project, We could manage by executing some commands which could be invoked through the manage.py. 

> Management Command is used to create our own actions with manage.py. If your app is in projectdirectory then create the directories.

Example
------
In this example, we are going to *create* 10 different users using Django user API via management command (**createusers**).
`python manage.py createusers`

Steps for creating Django Custom Management Commands
------
        django-admin startproject django_management_commands 
        cd django_management_commands
        python manage.py startapp webapp
        python manage.py migrate

**So final project directory structure should be-**
```YAML
django_management_commands
   webapp/
      __init__.py
      models.py
      management/
         __init__.py      
         commands/
            __init__.py
            createusers.py
      tests.py
      views.py
```

createusers.py
---------
```python
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Command for creating 10 superusers'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        User.objects.all().delete()
        for i in range(1,10):
            User.objects.create_superuser(username='superuser'+str(i),password='superuser',email='superuser'+str(i)+'@gmail.com').save()
        return "Successfully create "+str(len(User.objects.all()))+" superusers"
```
Steps for running Django Custom Management Commands
------
`python manage.py createusers`

By using above command, it will use django default users api for creating 10 different users and we can access admin UI console using credentials like username: superuser1/2/3/4 and password: superuser

`Note: Above django project prepared and tested on django==2.2.3 and djangorestframework==3.10.2`
