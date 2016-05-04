# Flask-todo
A todo app written in python's flask. 

> NOTE: THE APP IS STILL IN DEVELOPMENT AND NOT WORKING PROPETLY, PLEASE WAIT UNTIL
>THIS MESSAGE IS REMOVED BEFORE USING IT.

It's very simple, did it to practice my skill. It's a good thing to study if you are a beginner wanting to learn flask. You may not use this code commercially before contacting me (as if someone would use it).

### Version
Beta 0.1

### Installation

First make a virtual environment in the base folder **(where this file is)** and activate it.

Then run this to install all the required libraries (including flask):

```sh
$ pip install -r requirements.txt
```

Run this to generate app.db:
```sh
$ python db_create.py
```

Use this command every time you make change in *app/models.py*:
```sh
$ python db_update.py
```

To run the app after you've created a database use:
```sh
$ python run.py
```
And you are ready to go. 


I feel like the rest is self-explanatory. Huge thanks to [Miguel Grinberg](https://github.com/miguelgrinberg) for database scripts.

### Remember to have fun
---

### Todos

 - Add form validation (consider wtforms)
 - Improve security
 - Improve design a bit more
 - Make registration work

