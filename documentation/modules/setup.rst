############
Setup Page
############

You can have two types of setups:

Docker Setup:
**********************

1. Go to root directory.


2. Run following docker compose command

.. code-block::

       $  sudo docker-compose up
|


Local Setup:
**********************



1. Clone Repo. Github link: https://github.com/mubasher-tkxel/paymob_task

|

2. Create Virtual Environment with Python 3.8

.. code-block::

       $ mkvirtualenv --python=/usr/bin/python3.8 venv
|
3. Install Python Packages

.. code-block::

       $ pip install -r requirements.txt
|
4. Run Django server

.. code-block::

       $  python manage.py runserver
