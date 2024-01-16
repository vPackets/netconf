
from ncclient import manager

# Connect to the network device using ncclient
with manager.connect(host="clab-eBGP-c8K-Cisco8201-1", port=830, username="cisco", password="cisco123", hostkey_verify=False) as nc_conn:
    # Retrieve the running configuration
    nc_config = nc_conn.get_config(source='running').data_xml
    # Print the configuration
    print(nc_config)