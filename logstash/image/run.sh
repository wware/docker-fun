#!/bin/sh

export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64

elasticsearch-1.4.2/bin/elasticsearch &
logstash-1.4.2/bin/logstash -f /logstash-syslog.conf
