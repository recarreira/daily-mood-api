Daily Mood
==========

Minimalist app for checking the mood of your company.


API
===
WIP

## Setup


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

Your API will be running on your 5000 port:
[http://localhost:5000](http://localhost:5000/)


## Usage

### Computing a mood
Sample usage in localhost with [httpie](https://github.com/jakubroztocil/httpie):

#### Save new mood
```
http POST http://localhost:5000/api/v1/moods?level={1..4}
```

Example:
```bash
$ http POST http://localhost:5000/api/v1/moods?level=3
HTTP/1.0 200 OK
Content-Length: 67
Content-Type: application/json
Date: Mon, 25 Aug 2014 03:27:04 GMT
Server: Werkzeug/0.9.6 Python/2.7.5

{
    "created": "Mon, 25 Aug 2014 00:27:04 -0000",
    "level": "3"
}
```

#### List moods by date
```
http GET http://localhost:5000/api/v1/moods/{year}/{month}/{day}
```

Example:
```bash
$ http GET http://localhost:5000/api/v1/moods/2014/08/24
HTTP/1.0 200 OK
Content-Length: 362
Content-Type: application/json
Date: Mon, 25 Aug 2014 03:28:32 GMT
Server: Werkzeug/0.9.6 Python/2.7.5

{
    "moods": [
        {
            "created": "Sun, 24 Aug 2014 22:53:11 -0000",
            "level": "1"
        },
        {
            "created": "Sun, 24 Aug 2014 22:54:10 -0000",
            "level": "1"
        },
        {
            "created": "Sun, 24 Aug 2014 22:54:17 -0000",
            "level": "4"
        },
        {
            "created": "Sun, 24 Aug 2014 22:54:21 -0000",
            "level": "3"
        }
    ]
}
```

#### List all moods
```
http GET http://localhost:5000/api/v1/moods
```

Example:
```bash
$ http GET http://localhost:5000/api/v1/moods
HTTP/1.0 200 OK
Content-Length: 1050
Content-Type: application/json
Date: Mon, 25 Aug 2014 03:44:33 GMT
Server: Werkzeug/0.9.6 Python/2.7.5

{
    "moods": [
        {
            "created": "Mon, 18 Aug 2014 01:09:32 -0000",
            "level": "2"
        },
        {
            "created": "Mon, 18 Aug 2014 01:09:37 -0000",
            "level": "3"
        },
        {
            "created": "Mon, 18 Aug 2014 01:09:39 -0000",
            "level": "1"
        },
        {
            "created": "Mon, 18 Aug 2014 01:09:45 -0000",
            "level": "4"
        },
        {
            "created": "Sun, 24 Aug 2014 22:53:11 -0000",
            "level": "1"
        },
        {
            "created": "Sun, 24 Aug 2014 22:54:10 -0000",
            "level": "1"
        },
        {
            "created": "Sun, 24 Aug 2014 22:54:17 -0000",
            "level": "4"
        },
        {
            "created": "Sun, 24 Aug 2014 22:54:21 -0000",
            "level": "3"
        }
    ]
}
