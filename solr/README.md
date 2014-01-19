Solr
====

Build it
----

```bash
sudo docker build -t wware/solr solr
```


Run it
----

```bash
sudo docker run -d -t -p 0.0.0.0:8080:8080 wware/solr
```

Test it
----

```bash
./populate.sh   # this doesn't actually work: "Access to the specified resource has been forbidden."
TODO - figure out how to verify it's working
```
