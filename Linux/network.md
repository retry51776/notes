# Network Layers
Physical layer
> normal copper wires needs reapter under 1 kilometer
> fiber ususally able to goes miles
> which viechal you uses

Data Link
> traffic path, Ex: road

Network layer
> Address of house
    - Time to Live (TTL): num of hops

Transport layer
> allows traffic to firected to specific network app, which door; TCP, UDP

Application layer
> understand package, EX: https; smtp

OSI breaks Application layer into: Session, Pesentation, Application
---
networkID,
hostID,
subnet
> subnet: break up large network

subnet mask: mask value determent avaiable Sub IPs, 

Classless Inter-Domain Routing (CIDR)

Demarcation point (IP that one netowrk end & another begin)

---
router will keep IP datagram, but replace ethernet frame

### Routing Table Columns
- Destination network
- Next hop
- Total hops
- Interface
Distance protocal, old school hop calculation

Link State protocal, router will get stats farther router, to able react faster

---
# Transport
Multiplexer/Demultiplexer is key to horizontal scaling

Port: 16 bit direct application

TCP segment
3 way hand shake

socket state for debug

TCP confirm(ack) every messages,
UDP (connestionless), no ack, but faster

---

---
# DNS

Recursive Resolver
> middleman between client and DNS

> either answer it, or ask other name servers

Name Server
> translate domain names into IP

A/AAAA Records
> record format store host name to IPv4/IPv6, cycle through IPs of host

PTR Records
> Pointer record is opposite A/AAAA records, IP to host instead

MX record
> mail exchange

CNAME
> alias for server, EX: https://www. to https://,
> or abc.com to xyz.com

Zone File
> name server store domains informations

Registrar
> Root level domain registor

DNS Forwarding
> For dev server, internal services

DNS Peering
> Forwarding DNS request another VPC's DNS

Alternative Name Service
> All DNS request will redirects to another DNS

DNS proxies not working
> check firewall & routing

---
## DHCP
Dynamic Host Configuration Protocal is application layer ptotocal auto config host

Dynamic, 
Automatic allocation: try to keep ip
Fix allocation: 
  
Network Address Translation (NAT) 
> rewrite source IP, enable port forwarding, allows None-routable Addr Space to communicate


Non-routable Addresses Space (NAT)
> 10.0.0.0/8
> 197.16.0.0/12
> 192.168.0.0/16


---
VPN tunnel

Proxy Server do traffic control, reverse proxy to scale web server, hardware specilized to decryption,  includes gateway,

---
CMD
`traceroute`, `mtr`, `pathping` uses ttl field

`netcat google.com 80 -z`, `Test-NetConnection -port 80`

`nslookup google.com`


---
QRadar
IBM advance firewall
