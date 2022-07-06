# Network Layers
Physical layer
> normal copper wires needs reapter under 1 kilometer
> 
> fiber ususally able to goes miles
> 
> which viechal you uses

Data Link
> traffic path, Ex: road

Network layer
> Address of house
>> Time to Live (TTL): num of hops

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
## DHCP
Dynamic Host Configuration Protocal is application layer ptotocal auto config host

Dynamic, 
Automatic allocation: try to keep ip
Fix allocation: 
  
Network Address Translation (NAT) 
> rewrite source IP, enable port forwarding, allows None-routable Addr Space to communicate


Non-routable Addresses Space (NAT)
- 10.0.0.0/8
- 197.16.0.0/12
- 192.168.0.0/16


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


## Setup Domain Controller
1. Create VM
   a. rename PC name to (DomainController or something)
   b. config network adpator properties, disable IPv6, IPv4 with static IP
2. Server Manager -> Add roles & features -> check
   a. Active Directory Domain Service
3. Promote this service to a donmain controller
4. Add role DNS Service (conver url to ip)
5. Add role DHCP (manage IP adress assignment)


## Add PC to Domain
1. Control Panel / System and Security / System / change setting
2. rename PC name & domain
3. change DNS service to DC ip

