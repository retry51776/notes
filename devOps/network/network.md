# Network Layers
- Physical layer(vehicle) `normal copper wires needs repeater under 1 kilometer; fiber usually able to goes miles`

- Data Link `traffic path, Ex: road`
- Network layer (Address of house) `Time to Live (TTL): num of hops`
- Transport layer `allows traffic to directed to specific network app, which door; TCP, UDP`
- Application layer `understand package, EX: https; smtp`

> OSI `breaks Application layer into: Session, Presentation, Application`

## Buzzwords
- networkID,
- hostID,
- subnet `break up large network`
   - subnet mask `mask value determent available Sub IPs`
  - Demarcation point `IP that one network end & another begin`
- Classless Inter-Domain Routing (CIDR)
router `will keep IP datagram, but replace ethernet frame`
- QRadar
- IBM advance firewall

### Routing Table Columns
- Destination network
- Next hop
- Total hops
- Interface
Distance protocall, old school hop calculation

Link State protocall, router will get stats farther router, to able react faster

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
Dynamic Host Configuration Protocall (DHCP) `is application layer protocall auto config host`
   - Dynamic, 
   - Automatic allocation `try to keep ip`
   - Fix allocation: 
  
Network Address Translation (NAT) `rewrite source IP, enable port forwarding, allows None-routable Addr Space to communicate`

VPN tunnel `Proxy Server do traffic control, reverse proxy to scale web server, hardware specialized to decryption,  includes gateway,`


Non-routable Addresses Space (NAT)
- 10.0.0.0/8
- 197.16.0.0/12
- 192.168.0.0/16
https://jodies.de/ipcalc


---
## CMDs
```bash
# uses ttl field
traceroute
mtr
pathping

# Test-NetConnection -port 80
netcat google.com 80 -z
nslookup google.com
curl ifconfig.co //get public_ip
```


## Setup Domain Controller
1. Create VM
   a. rename PC name to (DomainController or something)
   b. config network adaptor properties, disable IPv6, IPv4 with static IP
2. Server Manager -> Add roles & features -> check
   a. Active Directory Domain Service
3. Promote this service to a domain controller
4. Add role DNS Service (convert url to ip)
5. Add role DHCP (manage IP address assignment)


## Add PC to Domain
1. Control Panel / System and Security / System / change setting
2. rename PC name & domain
3. change DNS service to DC ip

## LDAP Analogy
> Lightweight Directory Access Protocol (LDAP)`Just a protocall; similar to http`
> 
> Active Directory(AD) `similar to flask` 
> 
> Joint Engine Technology (JET) `similar to SQL`


# Buzzwords
- Internet Gateway(IGW)
- Network Access Control List(Network ACL) `base of IP control`
- Security Group `AWS Security Group is stateful`
- SSL termination `helps speed the decryption process and reduces the processing burden on backend servers.`