# Exploring Router & VLAN security, setting up access lists using Cisco Packet Tracer

### Cisco Packet Tracer
Packet Tracer is a cross-platform visual simulation tool designed by Cisco Systems that allows users to create network topologies and imitate modern computer networks. The software allows users to simulate the configuration of Cisco routers and switches using a simulated command line interface.

### Access Control Lists
An access control list (ACL) is a list of rules that specifies which users or systems are granted or denied access to a particular object or system resource. Access control lists are also installed in routers or switches, where they act as filters, managing which traffic can access the network.


### Configuring router with ACL 
```
Router>en
Router#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#access-list 10 deny 192.168.1.2 0.0.0.0
Router(config)#access-list 10 deny 192.168.1.3 0.0.0.0
Router(config)#access-list 10 deny 192.168.3.0 0.0.0.255
Router(config)#access-list 10 permit any
Router(config)#int f0/0
Router(config-if)#ip access-group 10 OUT
Router(config-if)#no shut
Router(config-if)#exit
Router(config)#
```
