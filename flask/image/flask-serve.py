#!/usr/bin/env python

import docopt
import flask
import logging
import netifaces
import os
import sys

app = flask.app.Flask(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter( "%(asctime)s %(pathname)s:%(lineno)d %(funcName)s %(levelname)s -- %(message)s ")
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.setLevel(logging.DEBUG)

options = docopt.docopt('''\
Serve static files using the Flask micro web framework.
Prerequities:
  sudo apt-get install -y python-flask python-setuptools python-dev curl
  sudo easy_install pip virtualenv docopt netifaces

Usage:
  {0}

Example client stuff:
  curl http://{1}:5000/foo.tar.gz -o foo.tar.gz
'''.format(sys.argv[0], netifaces.ifaddresses('eth0')[2][0]['addr']))

def wrap(inf):
    T = inf.read().replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return "<html><pre>" + T + "</pre></html>"

@app.route('/')
def show_all():
    return wrap(os.popen("ls -l"))

@app.route('/<filename>')
def show(filename):
    app.logger.info(filename)
    try:
        return wrap(open(filename))
    except:
        return wrap(os.popen("ls -l"))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
