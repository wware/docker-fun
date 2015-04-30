Running servers
====

One thing Docker is frequently used for is running servers. A popular thing nowadays is to
partition a website into
[microservices](https://www.ibm.com/developerworks/community/blogs/1ba56fe3-efad-432f-a1ab-58ba3910b073/entry/microservices_architecture_containers_and_docker?lang=en)
and Docker is an excellent deployment tool for doing that.

This directory has a little server using [Node](https://nodejs.org/) and [Express](http://expressjs.com/).

The reason I did a Node/Express server is because the last time I was thinking about Docker, server-side
JavaScript was the shiny new hotness. There are various schools of thought on whether it's really a good
idea. [Here](http://cwbuecheler.com/web/tutorials/2014/restful-web-app-node-express-mongodb/) is a nice
discussion of using Node, Express, and MongoDB to build a REST API.

Build it
----

```bash
sudo docker build -t wware/node node
```

Run it
----

```bash
sudo docker run -d -p 3000:3000 wware/node
```

Test it
----

```bash
curl http://localhost:3000/hello.txt
```
