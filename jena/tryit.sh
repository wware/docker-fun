#!/bin/bash

./s-put http://localhost:3030/dataset default books.ttl
./s-query --service=http://localhost:3030/dataset 'SELECT ?x ?y ?z WHERE {?x ?y ?z}'
