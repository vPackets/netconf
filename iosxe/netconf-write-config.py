from ncclient import manager
import xmltodict

# Device connection details
device_details = {
    "host": "clab-eBGP-CSR-csr1",
    "port": 830,
    "username": "admin",
    "password": "admin",
    "hostkey_verify": False,
    "device_params": {"name": "default"}
}

# XML configuration for changing hostname

config_template = '''
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>CLAB-1</hostname>
        <interface>
        <GigabitEthernet>
					<name>2</name>
                    <shutdown operation="remove"/>
					<ip>
						<address>
							<primary>
								<address>192.0.2.1</address>
								<mask>255.255.255.0</mask>
							</primary>
						</address>
					</ip>
					<logging>
						<event>
							<link-status/>
						</event>
					</logging>
					<mop>
						<enabled>false</enabled>
						<sysid>false</sysid>
					</mop>
					<negotiation xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet">
						<auto>true</auto>
					</negotiation>
				</GigabitEthernet>
				<GigabitEthernet>
					<name>3</name>
					<shutdown operation="remove"/>
                    <ip>
						<address>
							<primary>
								<address>10.1.0.1</address>
								<mask>255.255.255.0</mask>
							</primary>
						</address>
					</ip>
					<logging>
						<event>
							<link-status/>
						</event>
					</logging>
					<mop>
						<enabled>false</enabled>
						<sysid>false</sysid>
					</mop>
					<negotiation xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet">
						<auto>true</auto>
					</negotiation>
				</GigabitEthernet>
				<Loopback>
					<name>0</name>
					<ip>
						<address>
							<primary>
								<address>10.1.1.1</address>
								<mask>255.255.255.255</mask>
							</primary>
						</address>
					</ip>
					<logging>
						<event>
							<link-status/>
						</event>
					</logging>
				</Loopback>
			</interface>
            <router>
				<bgp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-bgp">
					<id>65000</id>
					<bgp>
						<log-neighbor-changes>true</log-neighbor-changes>
						<router-id>
							<ip-id>1.1.1.1</ip-id>
						</router-id>
					</bgp>
					<neighbor>
						<id>10.1.0.2</id>
						<remote-as>65100</remote-as>
					</neighbor>
					<address-family>
						<no-vrf>
							<ipv4>
								<af-name>unicast</af-name>
								<ipv4-unicast>
									<neighbor>
										<id>10.1.0.2</id>
										<activate/>
									</neighbor>
									<network>
										<no-mask>
											<number>192.0.2.0</number>
										</no-mask>
									</network>
								</ipv4-unicast>
							</ipv4>
						</no-vrf>
					</address-family>
				</bgp>
			</router>
    </native>
</config>
'''

# Connect to the device and send the configuration
with manager.connect(**device_details) as m:
    # Execute NETCONF <edit-config> operation
    response = m.edit_config(target='running', config=config_template)

    # Print response
    print(response)