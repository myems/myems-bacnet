myems_system_db = {
    'user': 'root',
    'password': 'PASSWORD',
    'host': '192.168.0.105',
    'database': 'myems_system_db',
}

myems_historical_db = {
    'user': 'root',
    'password': 'PASSWORD',
    'host': '192.168.0.105',
    'database': 'myems_historical_db',
}

# Indicates how long the process waits between readings
period_in_seconds = 60

bacnet_device = {
    'local_address': '192.168.0.105',
    'object_name': 'MYEMS',
    'object_identifier': 0xABCD,
    'max_apdu_length_accepted': 1024,
    'segmentation_supported': 'segmentedBoth',
    'vendor_identifier': 0xABCD,
    'foreignPort': 47808,
    'foreignBBMD': '10.10.73.1',
    'foreignTTL': 30,
}
