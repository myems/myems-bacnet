myems_system_db = {
    'user': 'root',
    'password': '!MyEMS1',
    'host': '127.0.0.1',
    'database': 'myems_system_db',
}

myems_historical_db = {
    'user': 'root',
    'password': '!MyEMS1',
    'host': '127.0.0.1',
    'database': 'myems_historical_db',
}

# Indicates how long the process waits between readings
period_in_seconds = 60

bacnet_device = {
    'local_address': '192.168.1.10',
    'object_name': 'MYEMS',
    'object_identifier': 0xABCD,
    'max_apdu_length_accepted': 1024,
    'segmentation_supported': 'segmentedBoth',
    'vendor_identifier': 0xABCD,
    'foreignPort': 47808,
    'foreignBBMD': '192.168.0.1',
    'foreignTTL': 30,
}


# Get the gateway info from MyEMS Admin Panel and update the 'id' and 'token'
gateway = {
    'id': 1,
    'token': '983427af-1c35-42ba-8b4d-288675550225'
}
