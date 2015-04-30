FROM      ubuntu:14.04
MAINTAINER Will Ware <wware@alum.mit.edu>

RUN apt-get update
RUN apt-get install -y python-virtualenv python-pip curl \
    python-docopt python-flask python-dev
RUN easy_install nose netifaces
ADD image /

CMD ./flask-serve.py
