#!/bin/sh

mkdir node-latest-install

cd node-latest-install
curl http://nodejs.org/dist/node-latest.tar.gz | tar xz --strip-components=1
./configure
make install
curl https://npmjs.org/install.sh > install.sh
/bin/sh install.sh
cd ..
rm -rf node-latest-install

npm install
