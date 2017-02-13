#! /usr/bin/env python
import binascii
import logging
from scapy.all import *



def show_packet(pkt):

    print pkt.summary()
    print ls(pkt)


def show_packet_layers(pkt):

    layers = []
    counter = 0
    while True:
        layer = pkt.getlayer(counter)
        if (layer != None):
            print layer.name
            layers.append(layer.name)
        else:
            break
        counter += 1

    print "Layers are:\t\t",layers
    print 
    

def show_dhcp_options(pkt):

    out ={}
    print '==========================================='
    print "Eth src mac: %s" % pkt.src

    dhcp = pkt.getlayer(DHCP)
    
    # 
    binary_repr = ('client_id','param_req_list','81')
    skip_repr = ('pad','end')
    server_services = ('server_id','name_server','router')
    
    for opt in dhcp.options:
        if str(opt[0]) in binary_repr:
            print "%s: %s" % (opt[0], binascii.hexlify(opt[1]) )
        elif opt in skip_repr:
            pass    
        else:
            print "%s: %s" % (opt[0],opt[1])
        
        if opt[0] in server_services:
            out[opt[0]] = opt[1]

    return out


if __name__ == "__main__":
    routers=set()
    dhcpservers=set()
    nameservers=set()

    packets = rdpcap('dhcp-traffic.pcap.')
    for pkt in packets:
        #show_packet(pkt)
        #show_packet_layers(pkt)
        buf = show_dhcp_options(pkt)
        try:
            if buf['router']: routers.add(buf['router'])
        except: pass
        try:
            if buf['name_server']: nameservers.add(buf['name_server'])
        except: pass
        try:
            if buf['server_id']: dhcpservers.add(buf['server_id'])
        except: pass

    print 
    print "Servers Found:"
    print "routers: %s" % (routers)
    print "nameservers: %s " % (nameservers)
    print "dhcpservers: %s" % (dhcpservers)
