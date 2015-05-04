FROM         ubuntu:14.04
MAINTAINER   Will Ware     <wware@alum.mit.edu>

RUN apt-get update
RUN apt-get install -y openjdk-7-jdk wget curl maven ruby subversion mercurial

RUN curl -O https://download.elasticsearch.org/logstash/logstash/logstash-1.4.2.tar.gz
RUN tar zxvf logstash-1.4.2.tar.gz
RUN curl -O https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.4.2.tar.gz
RUN tar xfz elasticsearch-1.4.2.tar.gz

ADD image /

CMD /run.sh
