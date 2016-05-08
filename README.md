# Flask-todo
A todo app written in python's flask. 

> This app is under MIT licence, so you can use/tweak it as much as you want. However be warned 
>that it's not secured, which means you haev to implement password encryption, 
>protect authentication etc. 

This ap is mainly for learning purposes. Both to practice my effectiveness and for beginners 
to learn from example

### Version
1.0

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
$ python db_migrate.py
```

To run the app after you've created a database use:
```sh
$ python run.py
```
And you are ready to go. Just go to 127.0.0.1:5000


I feel like the rest is self-explanatory. Huge thanks to [Miguel Grinberg](https://github.com/miguelgrinberg) for database scripts.

### Remember to have fun
---

### Todos

 - Heavily comment the code
