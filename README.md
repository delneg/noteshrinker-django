Noteshrinker - Django
======

What is this?
------

This a webservice, which is designed to help people keep their notes clean and store them in pretty PDF's.

It shrinks & prettifies the images uploaded, which makes them much easier to work with.

Example
------
Look at the image provided:
![before_after_image](https://github.com/delneg/noteshrinker-django/blob/master/example/before_after.jpg?raw=true "Before-After")
Better resolution is available in the "example" folder of this repo. It is not perfect example, it is the one done with the defaults,
yet it can be made better by tweaking settings.

How does it look like?
------
![ui](https://github.com/delneg/noteshrinker-django/blob/master/example/ui.jpg?raw=true "UI")
How do i launch it?
------

First of all, get python 3 & then get pip.

Optionally, you could use virtualenv. If you are using virtualenv, do 
```virtualenv venv && source venv/bin/activate ```
and use python instead of python3, and pip instead of pip3

1. [Python 3](https://www.python.org/downloads/)
2. [Pip](https://pip.pypa.io/en/stable/installing/)
3. Then, clone this repo (attention! it will be cloned to the current directory, so make sure you do it in some kinda documents or special one) ```git clone https://github.com/delneg/noteshrinker-django/ ```
4. Then, ```cd noteshrinker-django``` and ```pip3 install -r requirements.txt```
5. Tweak the settings in the bottom of the settings.py file.
6. Finally,  from the root directory of the project ```python3 manage.py migrate``` and  ```python3 manage.py runserver ```
7. Navigate to http://127.0.0.1:8000 in your browser!

License
------
MIT

Contribution
------
Feel free to contribute, I will review all responses.

Locales
------
Currently the app has Russian and English languages availible.
Feel free to add your locale - I'll appreciate it!

To add a locale:
Add a locale to ```LANGUAGES``` in settings.py file

Do ```django-admin makemessages```, edit the django.po file in locale/{local_code}/LC_MESSAGES/

Then run ```django-admin compilemessages```
