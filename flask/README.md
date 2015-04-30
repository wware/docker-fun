Running servers
====

One thing Docker is frequently used for is running servers. A popular thing nowadays is to
partition a website into
[microservices](https://www.ibm.com/developerworks/community/blogs/1ba56fe3-efad-432f-a1ab-58ba3910b073/entry/microservices_architecture_containers_and_docker?lang=en)
and Docker is an excellent deployment tool for doing that.

This directory has a little server using Python and [Flask](http://flask.pocoo.org/).
The Python server borrows from a [hello world tutorial](http://flask.pocoo.org/docs/0.10/quickstart/).
[Here](http://www.fullstackpython.com/flask.html) is some breathless enthusiasm for Flask.
Later I modified the Python server to show the contents of files.

Build it
----

```bash
sudo docker build -t wware/flask flask
```

Run it
----

```bash
sudo docker run -d -p 5000:5000 wware/flask ./flask-serve.py
```

Test it
----

```bash
curl http://localhost:5000/
curl http://localhost:5000/test.txt
curl http://localhost:5000/flask-serve.py
```
