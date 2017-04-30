# Yasser BookStore
Django Framwork ITI Project

Requirements:
MySOL, Python3, Django

database
****************
load the dump file (/db/bookstore.db) into mysql
===========================================

edit library/settings.py:
****************
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': [[YOUR DATABASE NAME]],
        'USER': [[YOUR DATABASE USERNAME]],
        'PASSWORD': [[YOUR DATABASE USER PASSWORD]],
        'HOST':'localhost',
    }
}
>> To run debug mode
DEBUG=TRUE
============================================
>> cd bookstore
>> python3 manage.by runserver

Open your browser:
Type: http://localhost:8000

To use the administrator account:
Type: http://localhost:8000/admin
username: admin
password: admin1234

Enjoy :D

