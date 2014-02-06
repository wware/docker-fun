FROM         ubuntu:14.04
MAINTAINER   Will Ware     <wware@alum.mit.edu>

RUN apt-get update
RUN apt-get install -y openjdk-7-jre-headless wget maven ruby subversion

RUN mkdir -p /usr/share/jena /usr/share/fuseki

RUN wget http://mirrors.advancedhosters.com/apache/jena/binaries/apache-jena-2.13.0.tar.gz
RUN tar xfz apache-jena-2.13.0.tar.gz && cp apache-jena-2.13.0/lib/*.jar /usr/share/jena
RUN (cd /usr/share/jena; for x in *.jar; do ln -s $x $(echo $x | sed "s/-[0-9\.]*\.jar/.jar/"); done)

RUN wget http://mirrors.advancedhosters.com/apache/jena/binaries/apache-jena-fuseki-2.0.0.tar.gz
RUN tar xfz apache-jena-fuseki-2.0.0.tar.gz && mv apache-jena-fuseki-2.0.0/* /usr/share/fuseki

RUN rm -rf apache-jena-*

ADD image /

CMD ["/serve.sh"]
