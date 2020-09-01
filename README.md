# Company ownership coding challenge

A small coding task that requires solving some simple tasks related to
the [norwegian share holder registry](https://www.altinn.no/starte-og-drive/skatt-og-avgift/skatt/aksjonarregisteret/).

For curious citizens, the full copy can be requested [here](https://www.skatteetaten.no/en/presse/aksjeeieropplysninger/).


## The application
The application is a simple REST api written in [flask](https://flask.palletsprojects.com/),
with a very simple local database used to store data in memory.

All application code is located in [main.py](main.py)

Three endpoints are defined:

* `/<orgnr>/owners`
  Returns all registered owners for a company

* `/<orgnr>/holdings`
  Returns all registered holdings a company has

* `<orgnr>/summary`
  Returns a basic summary of a company's ownership,
  as well as some other potentially interesting information.


## Requirements
* Python 3


## Installing

* Clone this repo (it is a good idea to fork it first)
* Install dependencies (`pip install -r requirements.txt`)


## Running

After installing dependencies, you can run the local development server:

```
$ python main.py
```

(assuming `python` points to your Python 3 interpreter)

The server is now running on [http://localhost:5000], and you should be able


## Testing

Most of the bundled tests are broken. They should be fixed by changing the code in `main.py`, not by changing the tests :)

To run the tests:

```
$ py.test
```

or

```
$ python -m pytest
```

(where `python` should be your Python 3 interpreter)


## Solving

Fill in all the sections in [main.py](main.py) that contain a `# TODO` comment.

The challenge is complete when all tests are passing!


## Submitting solutions
Make a pull request and point us to it!

Again, it might be a good idea to fork the repo first ;)

Happy coding!
