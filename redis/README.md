Redis server running on Docker
====

From [this tutorial](https://docs.docker.com/examples/running_redis_service/).

Build it
----

```bash
sudo docker build -t wware/redis redis
```

Run it
----

```bash
sudo docker run -d -p 6379:6379 wware/redis
```

Test it
----

```bash
redis-cli rpush foo bar
redis-cli rpush foo baz
redis-cli rpop foo
redis-cli rpop foo
```
