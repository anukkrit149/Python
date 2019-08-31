#! /bin/bashnetwork:
  ethernets:
      eno1:
addresses: [192.168.1.1/20]          gateway4: 192.168.1.1
          dhcp4: true
          optional: true
          nameservers:
              addresses: [8.8.8.8,8.8.4.4]
  version: 2