#!/bin/bash

iptables --flush
iptables --table nat --flush
iptables --delete-chain
iptables --table nat --delete-chain
iptables --table nat --append POSTROUTING --out-interface eth0 -j MASQUERADE
iptables --append FORWARD --in-interface wlan0 -j ACCEPT

sysctl -w net.ipv4.ip_forward=1

ifconfig wlan0 10.101.1.1 netmask 255.255.255.0
