# DHCP traffic read by Scapy 


Read a  file pcap and print out the dhcp traffic captured on the network,
in an easily human readable way.


You can use it to create  a mapping of clients in the newtork 
you are attached to. 


Please, install scapy first (python 2.7)
```
$ pip install scapy
$ pip install dumbnet
```

and if you receive this "ImportError: No module named dumbnet" you need
to install libdnet

```
git clone https://github.com/dugsong/libdnet.git
cd libdnet
./configure && make
cd python
python setup.py install
```

Please, install scapy first (python 2.7) 
```
$ pip install scapy
$ pip install dumbnet
```

and if you receive this "ImportError: No module named dumbnet" you need 
to install libdnet
 
```
git clone https://github.com/dugsong/libdnet.git
cd libdnet
./configure && make
cd python
python setup.py install
```


###  Usage: ###


- get a traffic log

```
$ sudo tcpdump -i wlan0 portrange 67-68 -w  dhcp-traffic.pcap
```

- launch the script

```
$ python dhcp.py
===========================================
Eth 00:aa:bb:cc:dd:ff >ff:ff:ff:ff:ff:ff
IP 0.0.0.0 > 255.255.255.255
message-type: 3 (Request)
param_req_list: 017908360z44fc5t2c2e
max_dhcp_size: 1500
client_id: 010006393de93d
requested_addr: 192.168.43.35
server_id: 192.168.43.1
hostname: android-3576358fka2zzfsred
===========================================
Eth 00:zz:yy:yy:kk:ww > ff:ff:ff:ff:ff:ff
IP 192.168.43.1 > 255.255.255.255
message-type: 5 (ACK for 192.168.43.35)
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



Short reminder about DHCP message-type:


    1 = DHCP Discover message (DHCPDiscover).

    2 = DHCP Offer message (DHCPOffer).

    3 = DHCP Request message (DHCPRequest).

    4 = DHCP Decline message (DHCPDecline).

    5 = DHCP Acknowledgment message (DHCPAck).

    6 = DHCP Negative Acknowledgment message (DHCPNak).

    7 = DHCP Release message (DHCPRelease).

    8 = DHCP Informational message (DHCPInform).

