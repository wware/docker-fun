FROM         ubuntu:14.04
MAINTAINER   Will Ware     <wware@alum.mit.edu>

RUN apt-get update
RUN apt-get install -y openjdk-7-jre-headless solr-tomcat

ADD image /

CMD ["/serve.sh"]

# Here is what seems to work. Start this container with the following command.
#
#     sudo docker run -i -t -p 0.0.0.0:8080:8080 wware/solr
#
# Takes a moment for ES to start. Now on the VirtualBox instance type "ifconfig"
# (make sure networking is "Bridged Adapter") to get IP address, and on the
# host machine type "curl http://IPADDRESS:8080/solr" and observe test response.
