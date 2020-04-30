import json
import ipaddress
from pprint import pprint

deviceJSON = '{"Version": "15.6", "locationN": "500 Northridge", "role": "Access", "upTime": "12:10:53.49", "hostname": "ATL-3650-1", "macAddress": "39:58:1f:9e:38:c1", "series": "Cisco Catalyst 3650 Series Switches", "lastUpdated": "2017-09-21 13:12:46", "bootDateTime": "2016-10-27 05:24:53", "interfaceCount": "24", "lineCardCount": "1", "managementIpAddress": "192.168.10.10", "interfaces": {"interface": [{"GigabitEthernet0": {"ipv4": "100.100.100.1"}}, {"GigabitEthernet1": {"ipv4": "10.10.10.2"}}]}}'

print(f'The Python data format for the "deviceJSON" variable is {type(deviceJSON)}')
print()
print(deviceJSON)
print()

deviceDICT = json.loads(deviceJSON)
pprint(deviceDICT)

for item in deviceDICT['interfaces']['interface']:
    # print (item)
    for Gig_int, ip_addr in item.items():
        # print(ip_addr)
        IP = ipaddress.IPv4Address(ip_addr["ipv4"])
        # print(IP)
        if IP.is_private: #==True and is_private
            print(f"{Gig_int} has an IP address of {IP} and is Private")
        else:
            print(f"{Gig_int} has an IP address of {IP} and is not Private")

Gig0IP = deviceDICT['interfaces']['interface'][0]['GigabitEthernet0']['ipv4']
Gig1IP = deviceDICT['interfaces']['interface'][1]['GigabitEthernet1']['ipv4']

Gig0 = ipaddress.IPv4Address(Gig0IP)
Gig1 = ipaddress.IPv4Address(Gig1IP)

if Gig0.is_private:
    print(f'GigabitEthernet0 has an IP address of {Gig0} and is a Private Address')
else:
    print(f'GigabitEthernet0 has an IP address of {Gig0} is not a Private Address')

if Gig1.is_private:
    print(f'GigabitEthernet1 has an IP address of {Gig1} and is a Private Address')
else:
    print(f'GigabitEthernet1 has an IP address of {Gig1} is not a Private Address')
