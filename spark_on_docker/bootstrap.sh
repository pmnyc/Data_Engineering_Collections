#!/bin/bash

: ${HADOOP_PREFIX:=/usr/local/hadoop}

$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh

rm /tmp/*.pid

# installing libraries if any - (resource urls added comma separated to the ACP system variable)
cd $HADOOP_PREFIX/share/hadoop/common ; for cp in ${ACP//,/ }; do  echo == $cp; curl -LO $cp ; done; cd -

# altering the core-site configuration
sed s/HOSTNAME/$HOSTNAME/ /usr/local/hadoop/etc/hadoop/core-site.xml.template > /usr/local/hadoop/etc/hadoop/core-site.xml

# setting spark defaults
echo spark.yarn.jar hdfs:///spark/spark-assembly-1.6.0-hadoop2.6.0.jar > $SPARK_HOME/conf/spark-defaults.conf
cp $SPARK_HOME/conf/metrics.properties.template $SPARK_HOME/conf/metrics.properties

service sshd start
$HADOOP_PREFIX/sbin/start-dfs.sh
$HADOOP_PREFIX/sbin/start-yarn.sh

### The following are some packages for Theano and other Pythong Packages ###
sudo apt-get install nano wget
sudo apt-get -y install build-essential
sudo apt-get -y update
sudo apt-get -y install apache2 r-base r-base-dev
sudo apt-get -y install openssl libssl-dev postgresql-9.3-postgis-2.1 odbc-postgresql python-psycopg2
sudo apt-get -y install postgresql-9.3 postgresql-server-dev-9.3 libxml2-dev libproj-dev libjson0-dev
sudo apt-get -y install xsltproc docbook-xsl docbook-mathml libgdal1-dev postgresql-contrib-9.3 libpq-dev
sudo apt-get -y install python-dev python-setuptools python-pip python-numpy python-scipy
sudo apt-get -y install libatlas3gf-base git-core liblapack-dev libblas-dev gfortran libatlas-dev

sudo apt-get install -y git python-dev python-nose python-scipy
sudo apt-get install -y python-scrapy python-matplotlib
sudo pip install pandas pandasql boto s4cmd awscli flask
sudo pip install pyvirtualdisplay selenium virtualenv sklearn
sudo pip install --upgrade git+git://github.com/Theano/Theano.git #--no-deps
sudo pip install keras elephas
### End of packages

CMD=${1:-"exit 0"}
if [[ "$CMD" == "-d" ]];
then
	service sshd stop
	/usr/sbin/sshd -D -d
else
	/bin/bash -c "$*"
fi