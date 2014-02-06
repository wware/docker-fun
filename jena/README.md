Jena and Fuseki
====

* https://jena.apache.org/
* http://jena.apache.org/documentation/serving_data/

Jena is a free and open source Java framework for building Semantic Web and Linked Data applications.
Fuseki is a SPARQL server. It provides REST-style SPARQL HTTP Update, SPARQL Query, and SPARQL Update using the SPARQL protocol over HTTP.

Build it
----

```bash
sudo docker build -t wware/jena jena
```

Run it
----

```bash
sudo docker run -d -p 3030:3030 wware/jena
```

Test it
----

```bash
sudo apt-get install ruby     # Ubuntu
./tryit.sh
curl http://localhost:3030/dataset/query?query="SELECT%20*%20WHERE%20%7B?x%20?y%20?z%7D"
```
