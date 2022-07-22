<h1>DNS</h1>

> DNS analogy:
>> ip -> address
>
>> port -> apt #
>
>> protocal -> vehicle(bike, car, train, plane)

> Windows Server DNS, OpenDNS, Cloudflare, Google Public DNS

### resolv.conf vs hosts
> resolv.conf specifies nameservers in order of search preference.
> hosts overrides all nameservers by mapping urls/shortnames to IPs.

- [DNS Server](#dns-server)
- [Authoritative Name Server](#authoritative-name-server)
  - [Zone](#zone)
  - [DNS Records](#dns-records)
- [Recursive Resolver](#recursive-resolver)
- [Debug](#debug)


## DNS Server
> DNS port 53
- INTERFACES
- FORWARDERS
- ADVANCED
- ROUTINGS
- SECURITY
- MONITORING
- LOGGING
- DEBUG LOGGING

## Authoritative Name Server
> only answer configed domains

### Zone
> Zone properties can store in AD

> I think of DNS Zone as folder of DNS records


- Primary Zone `store in .dns file`
- Secondary Zone `read only cache`
- Stub Zone `who to ask`
- Forward Lookup Zone `name -> ip`
- Reverse Lookup Zone `ip -> name`

### DNS Records

    - IPv4 address (A)
    - IPv6 address (AAAA)
    - Certificate Authority Authorization (CAA)
    - Canonical name (CNAME)
    - Mail exchange (MX)
    - Name Authority Pointer (NAPTR)
    - Name Server (NS)
    - Pointer (PTR)
    - Sender Policy Framework (SPF)
    - Service Record (SVR, w Port #, Weight, Piroty)
    - Text (TXT)

http://www.test.com

.com = Top level domains
test = domain name / second level domain
www. = second-level domain

## Recursive Resolver
> middleman between client and DNS

> either answer it, or ask other name servers

Name Server (NS)
> Authoritative Name Server IP
> at least 2, max 10

A/AAAA Records
> record format store host name to IPv4/IPv6, cycle through IPs of host

Reverse DNS lookup (PTR Records)
> Pointer record is opposite A/AAAA records, IP to host instead

MX record
> mail exchange

CNAME
> alias for server, EX: https://www. to https://,
> or abc.com to xyz.com, or https://mail.xyz to 9.9.9.9, support `*` or `$`

Zone File
> name server store domains informations, `SOA`

> Ex: www. email. ftp. www.hr. www.sales

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

Service Record (SVR, w Port #, Weight, Piroty)
    priority - lower get more traffic
    Weight default - higher get more traffic
    `dig x_service.x_target.com SRV`

## Debug
```
edit host file(c:\windows\system32\drivers\etc) to network debug 

DNS Console, NSLOOKUP, DNSCMD, IPCONFIG, DNS Logs

dcdiag /test:dns /v /e

Netdiag.exe /fix

ipconfig /flushdns

# Enable Dynamic Updates In Dns
# Start>Program>Admin tools> DNS >Zone properties.
```


World Intellectual Property Organization (WIPO) 