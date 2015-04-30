FROM      ubuntu:14.04
MAINTAINER Will Ware <wware@alum.mit.edu>

RUN apt-get update
RUN apt-get install -y curl build-essential
ADD image /

RUN ./install-node.sh

CMD /usr/local/bin/node app.js
