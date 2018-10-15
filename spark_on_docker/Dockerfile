FROM sequenceiq/hadoop-ubuntu:2.6.0
MAINTAINER Man Peng

RUN curl -s http://apache.arvixe.com/spark/spark-1.6.0/spark-1.6.0-bin-hadoop2.6.tgz | tar -xz -C /usr/local/
RUN apt-get -y update
RUN apt-get install -y build-essential nano wget apache2 r-base r-base-dev git git-core openssl libssl-dev
RUN cd /usr/local && ln -s spark-1.6.0-bin-hadoop2.6 spark
ENV SPARK_VERSION 1.6.0
ENV SPARK_HOME /usr/local/spark
RUN mkdir $SPARK_HOME/yarn-remote-client
ADD yarn-remote-client $SPARK_HOME/yarn-remote-client

RUN $BOOTSTRAP && $HADOOP_PREFIX/bin/hadoop dfsadmin -safemode leave && $HADOOP_PREFIX/bin/hdfs dfs -put $SPARK_HOME-1.6.0-bin-hadoop2.6/lib /spark

ENV YARN_CONF_DIR $HADOOP_PREFIX/etc/hadoop
ENV PATH $PATH:$SPARK_HOME/bin:$HADOOP_PREFIX/bin
# update boot script
COPY bootstrap.sh /etc/bootstrap.sh
# change owner to root
RUN chown root.root /etc/bootstrap.sh
RUN chmod 700 /etc/bootstrap.sh

# Expose ports
EXPOSE 8080 80

# install packages from bootstrap.sh file
RUN bash /etc/bootstrap.sh

## This starts the program whenever a container is launched
# ENTRYPOINT ["/etc/bootstrap.sh"]
# CMD ["/etc/bootstrap.sh", "-d"]

######### The rest are deprecated ##########
## Add files.
# ADD start.bash /ghost-start
## Set environment variables.
# ENV NODE_ENV production
## Define mountable directories.
# VOLUME ["/data", "/ghost-override"]
## Define working directory.
# WORKDIR /usr
## Define default command.
# CMD ["bash", "/ghost-start"]