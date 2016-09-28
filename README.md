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
Better resolution is availible in the "example" folder of this repo. It is not perfect example, it is the one done with the defaults,
yet it can be made better by tweaking settings.

How do i launch it?
------

First of all, get python 3 & then get pip.
1. [Python 3](https://www.python.org/downloads/)
2. [Pip](https://pip.pypa.io/en/stable/installing/)
Then, clone this repo (attention! it will be cloned to the current directory, so make sure you do it in some kinda documents or special one)
```bash
git clone https://github.com/delneg/noteshrinker-django/
```
3. Then, ```cd noteshrinker-django``` and ```pip3 install -r requirements.txt```
4. Tweak the settings in the bottom of the settings.py file.
4. Finally,  from the root directory of the project
```bash
python3 manage.py migrate
python3 manage.py runserver
```
5. Navigate to http://127.0.0.1:8000 in your browser!

License
------
MIT

Contribution
------
Feel free to contribute, I will review all responses.

Locales
------
At the moment I'm writing this (29 sept 2016) - the only locale availible is russian, though I'm planning to add English ASAP.
Feel free to add your locale - it's not that hard!

