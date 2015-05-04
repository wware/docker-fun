Fun with logstash
====

* http://logstash.net/docs/1.4.2/tutorials/getting-started-with-logstash
* https://registry.hub.docker.com/u/library/logstash/
* https://registry.hub.docker.com/u/library/elasticsearch/

Build it
----

```bash
sudo docker build -t wware/logstash .
```

Run it
----

```bash
sudo docker run -d -p 5000:5000 -p 9200:9200 wware/logstash
```

Test it
----

This instance takes a few seconds to boot. Give it ten seconds to be safe.

```bash
python log_some_stuff.py
# wait a few seconds for elasticsearch to catch up
python read_logs.py
```
