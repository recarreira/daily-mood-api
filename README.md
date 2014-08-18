Daily Mood
==========

Minimalist app for checking the mood of your company.


API
===

## Setup

WIP

### Initial setup

Install the requirements:
```
$ pip install -r requirements.txt
```

And then run the follow script for setting up the DB:
```
$ python setup_db.py
```

### Running

``` bash
$ python api.py
```

Your API will be running on your 8080 port:
[http://localhost:8080](http://localhost:8080/)


## Usage

### Computing a mood
Sample usage in localhost with [httpie](https://github.com/jakubroztocil/httpie):

```
http POST http://localhost:8080/?level={1..4}
```
