# MyEMS BACnet Service


## Introduction

This service is a component of MyEMS to acquire data from BACnet devices


## Prerequisites
bacpypes

mysql.connector



## Installation

Download and install MySQL Connector:
```
    $ cd ~/tools
    $ wget https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-8.0.20.tar.gz
    $ tar xzf mysql-connector-python-8.0.20.tar.gz
    $ cd ~/tools/mysql-connector-python-8.0.20
    $ sudo python3 setup.py install
```

Download and install bacpypes library
```
    $ cd ~/tools
    $ git clone https://github.com/pypa/setuptools_scm.git
    $ git clone https://github.com/pytest-dev/pytest-runner.git
    $ git clone https://github.com/JoelBender/bacpypes.git
    $ cd ~/tools/setuptools_scm/
    $ sudo python3 setup.py install
    $ cd ~/tools/pytest-runner/
    $ sudo python3 setup.py install
    $ cd ~/tools/bacpypes
    $ sudo python3 setup.py install
    $ sudo ufw allow 47808
```
Install myems-bacnet service
```
    $ cd ~/tools
    $ git clone https://github.com/myems/myems-bacnet.git
    $ sudo cp -R ~/myems-bacnet /myems-bacnet
    $ cd /myems-bacnet
```
    Edit the config file for database configuration and local device address
```
    $ sudo nano config.py
```
    Setup systemd service:
```
    $ sudo cp myems-bacnet.service /lib/systemd/system/
```
    Next enable the service:
```
    $ sudo systemctl enable myems-bacnet.service
```
    Start the service:
```
    $ sudo systemctl start myems-bacnet.service
```

## References

  1. http://myems.io
  2. http://bacnet.org
  3. https://github.com/JoelBender/bacpypes
  

