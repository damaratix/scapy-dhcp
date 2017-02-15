# DHCP traffic read by Scapy 


Read a  file pcap and print out the dhcp traffic captured on the network,
in an easily human readable way.


You can use it to create  a mapping of clients in the newtork 
you are attacched to. 


###  Usage: ###


- get a traffic log

```
$ sudo tcpdump -i wlan0 portrange 67-68 -w  dhcp-traffic.pcap
```

- launch the script

```
$ python dhcp.py
===========================================
Eth src mac: 00:aa:bb:cc:dd:ff
message-type: 3
param_req_list: 017908360z44fc5t2c2e
max_dhcp_size: 1500
client_id: 010006393de93d
requested_addr: 192.168.43.35
server_id: 192.168.43.1
hostname: android-3576358fka2zzfsred
===========================================
Eth src mac: 00:zz:yy:yy:kk:ww
message-type: 5
server_id: 192.168.43.1
lease_time: 3600
renewal_time: 1800
rebinding_time: 3150
subnet_mask: 255.255.255.0
broadcast_address: 192.168.43.255
router: 192.168.43.1
name_server: 192.168.43.1
vendor_specific: ANDROID_VENDOR

Servers Found:
routers: set(['192.168.43.1'])
nameservers: set(['192.168.43.1']) 
dhcpservers: set(['192.168.43.1'])

```
