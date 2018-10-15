#!/bin/bash
# This script is needed as separate Path (no , separator) to add
    #bootstrap commands all instances in the cluster

    
# Build Image
sudo apt-get install nano wget
sudo apt-get -y install build-essential
sudo apt-get -y update && sudo apt-get dist-upgrade
sudo apt-get -y install apache2 r-base r-base-dev
sudo apt-get -y install openssl libssl-dev postgresql-9.3-postgis-2.1 odbc-postgresql python-psycopg2
sudo apt-get -y install postgresql-9.3 postgresql-server-dev-9.3 libxml2-dev libproj-dev libjson0-dev
sudo apt-get -y install xsltproc docbook-xsl docbook-mathml libgdal1-dev postgresql-contrib-9.3 libpq-dev
sudo apt-get -y install python-dev python-setuptools python-pip python-numpy python-scipy libatlas-dev libopenblas-dev
sudo apt-get -y install libatlas3gf-base git-core liblapack-dev libblas-dev gfortran

sudo apt-get install -y git python-dev python-nose python-scipy
sudo apt-get install -y python-scrapy python-matplotlib
sudo pip install pandas pandasql boto s4cmd awscli flask
sudo pip install pyvirtualdisplay selenium virtualenv sklearn
sudo pip install --upgrade git+git://github.com/Theano/Theano.git #--no-deps
sudo pip install keras elephas

## The following is to install keras on Anaconda
git clone https://github.com/fchollet/keras  
cd keras  
python setup.py install
## The following is to install Bleeding-Edge on Anaconda
git clone git://github.com/Theano/Theano.git
cd Theano
python setup.py develop


#---------------- On CentOS ----------------
# Warning: Some issue with Python2.7. The default CentOS python version is 2.6.

# Commands
# Pull base image
docker pull sequenceiq/spark:1.5.1
sudo docker run -it sequenceiq/spark:1.5.1 bash

# Build Image
sudo yum update -y
sudo yum groupinstall -y "Development Tools" "Development Libraries"
sudo yum install gcc uuid-devel Cython libffi-devel -y
sudo yum install -y centos-release-SCL nano
sudo yum install make automake gcc-c++ kernel-devel git-core -y
sudo yum install wget tar -y

sudo yum install python27 python27-python-devel -y
python -V # this checks which default python version it is using
