Apache Spark on Docker
==========

Book: [Mastering Apache Spark](https://www.gitbook.com/book/jaceklaskowski/mastering-apache-spark/details)

This repository contains a Docker file to build a Docker image with Apache Spark. This Docker image depends on our previous [Hadoop Docker](https://github.com/sequenceiq/hadoop-docker) image, available at the SequenceIQ [GitHub](https://github.com/sequenceiq) page.
The base Hadoop Docker image is also available as an official [Docker image](https://registry.hub.docker.com/u/sequenceiq/hadoop-docker/) (sequenceiq/hadoop-docker).

## Building the image on the current work directory.
```
docker build --rm -t pengma/spark_deeplearning:v1.0-spark1.6 .
```

## Get in a container.
First one is interactive one but will exit when you exit which is a tty. Second line gives safer sandbox environment and won't exit after you exit the command line terminal inside container. The -p specifies the range of ports opened so that one may access it from outside such as web services.
```
docker run -it pengma/spark_deeplearning:v1.0-spark1.6 bash
docker run -d -t -p 4040:4050 -h sandbox pengma/spark_deeplearning:v1.0-spark1.6 bash
    docker exec -it <container_id> bash
```

## Versions
```
Ubuntu 14.04 Hadoop 2.6.0 and Apache Spark v1.6.0
```

## Testing

There are two deploy modes that can be used to launch Spark applications on YARN.

### YARN-client mode

In yarn-client mode, the driver runs in the client process, and the application master is only used for requesting resources from YARN.

```
# run the spark shell
spark-shell --master yarn-client --driver-memory 1g --executor-memory 1g --executor-cores 1

# execute the the following command which should return 1000
scala> sc.parallelize(1 to 1000).count()
```
### YARN-cluster mode

In yarn-cluster mode, the Spark driver runs inside an application master process which is managed by YARN on the cluster, and the client can go away after initiating the application.
