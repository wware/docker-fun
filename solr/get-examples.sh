#!/bin/bash

VERSION=5.1.0
URL=http://apache.mirrors.pair.com/lucene/solr/${VERSION}/solr-${VERSION}.tgz

if [ ! -f solr-${VERSION}.tgz ]
then
    wget $URL
fi

tar xfz solr-${VERSION}.tgz
mkdir -p image/solr
rm -rf image/solr/example
mv solr-${VERSION}/example image/solr
rm -rf solr-${VERSION}
