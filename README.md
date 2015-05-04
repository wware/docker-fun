Docker coolness
====

Obviously [Docker](https://docs.docker.com/) is wicked ahsome and I should get
acquainted with it. I've also been intending to get better acquainted with Redis
so I'm borrowing some stuff from
[the docs](http://docs.docker.com/examples/running_redis_service/)
pertaining to that.

First things first. Do not just go "sudo apt-get install docker.io", or you'll
end up with version 1.0.1 which is horribly buggy. Follow the
[correct instructions](http://docs.docker.com/installation/ubuntulinux/):

```bash
wget -qO- https://get.docker.com/ | sh
```

The install process will offer you an option to do some usermod stuff so you can
run Docker as non-root. My experience thusfar has been that that doesn't work because
it still stores the containers and images where only root can touch them, so I ignore
that option.

Intriguing things about Docker
----

* I can chop up a project into
  [microservices](https://www.ibm.com/developerworks/community/blogs/1ba56fe3-efad-432f-a1ab-58ba3910b073/entry/microservices_architecture_containers_and_docker?lang=en)
  and implement them in separate Docker containers. When I want to combine them,
  I can use [docker-compose](https://docs.docker.com/compose/).
* I can spin up lots of containers on my dev machine, and pretend I'm working with
  some big complicated VPC on AWS.
* Theoretically, I can tar up images I've built on my dev machine using
  [docker save](https://docs.docker.com/reference/commandline/cli/#save), scp the
  tar file up to my server-in-the-cloud, and unpack it there using
  [docker load](https://docs.docker.com/reference/commandline/cli/#load). I haven't
  tried this yet, but it sounds like it would make deployment pretty doggone easy.

Most companies I've worked at in the past few years have a collection of git
repositories, and each server in their production site uses some combination of
these repositories. It wouldn't be too hard to create a Docker image for each
server, and be able to run the whole kittenkaboodle on my dev machine. It may be
necessary to [tinker with ssh permissions](http://stackoverflow.com/questions/23391839)
to clone all the git repositories, but that's a soluble problem, and being able
to emulate the production system on my dev machine should be very valuable.

The docker community
----

There is a [registry](https://registry.hub.docker.com) of existing Docker images
that people have put together. You can find images for all sorts of popular web
tools: Redis, Celery, Postgres, nginx, MongoDB, MySQL, Ubuntu, NodeJS, and with a
bit of digging, more interesting things like
[Neo4J](https://github.com/ekino/docker-neo4j-cluster),
[Jena/Fuseki](https://registry.hub.docker.com/u/stain/jena-fuseki/),
[GROMACS](https://github.com/science-automation/gromacs-4.6.5),
[POV-Ray](https://registry.hub.docker.com/u/nyoho/povray/dockerfile/) and
[a Raspberry Pi toolchain](https://registry.hub.docker.com/u/sdt4docker/raspberry-pi-cross-compiler/).
(A couple more RPi hacks: running [Docker on the RPi](https://resin.io/blog/docker-on-raspberry-pi-in-4-simple-steps/)
and building a [RPi cluster](http://sc5.io/posts/a-private-raspberry-pi-cloud-with-arm-docker)
using docker.)

If I'm understanding this correctly, I could put together a shopping list of tools
that I want to use, pull down the appropriate docker images, connect them with
docker-compose, and just add my own application code.

A guy at work is excited about [CoreOS](https://coreos.com/), a collection of tools
that build upon docker to handle all kinds of deployment concerns. He specifically
said I should be looking at [etcd](https://coreos.com/etcd/) and
[fleet](https://coreos.com/using-coreos/clustering/). I find the CoreOS stuff a
bit overwhelming so I think I'll work on that later.
