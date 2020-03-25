# MyEMS BACnet Service


## Introduction

This service is a component of MyEMS and acquires data from BACnet devices


## Prerequisites

mysql.connector

bacpypes

## Installation

    1. Install MySQL Connector
```
    $ pip3 install mysql-connector-python
```
    2. Install bacpypes library
```
    $ sudo pip install bacpypes
```
    3. Open port 47808
```
    $ sudo ufw allow 47808
```
    4. Install myems-bacnet service
```
    $ sudo cp -R ~/myems-bacnet /myems-bacnet
    $ cd /myems-bacnet
```
    Edit the config file for database configuration and local device address
```
    $ sudo nano config.py
```
    Setup systemd configure file:
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
  

