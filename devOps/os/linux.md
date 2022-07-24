# Linux OS Boot Order
1. On Power
2. BIOS
3. Boot Loader
4. Kernel Loading
5. Init System - manager all processes until shutdown
   1. System V
   2. System D
   3. Upstart
   4. OpenRC
   5. runit

> /proc is virtual file refect process info
linux make everything as file

```
lsof "list open files"
ss -tunapl "socket process"

# check logs
journalctl -fu nginx
```

# Linux Apps

Free Software Foundation (FSF) 

GNU is list of open source linux components

### Compliles
- make
  > Makefile: create rules, assign cmd to rule, chain rules
- GNU Compiler Collection (GCC)


## Package Manager 
> Think of apple app store, android app store

- apt-get
- dpkg
- yum
- RPM
- pacman

```
sudo apt install strace	#Debian/Ubuntu 
# yum install strace		#RHEL/CentOS
# dnf install strace		#Fedora 22+

which pg_config
apk add pg_config
apk info --who-owns /usr/bin/pg_config

apt // Used By Debain
rpm //red hat, syntom

```

**OS CMDs** 
```
htop // Similar to task manager in Windows 

free -h //Memory

chmod -R 660 /app

passwd //Change password

uname -a //Display OS info
df -ah  //show disk usage
du -sh [path-name] // disk usage

top //linux task manager

iftop //network manager

history// past cmd

procps // linux process
strace //

sudo chown user_name file_name
chmod u+x file_name
chomd [owner][group][other] file_name
    - u:user;
    - g:group;
    - o:other users;

    - r:4:read
    - w:2:write
    - x:1:excute

vi test.txt
cat test.txt

less //cat large files  /[search_text]
grep [word] [seach_path] //text search

echo hello > test.txt //Overwrite
echo hello >> test.txt //Append

```

## Service/Cronjob/Dev
```
crontab –l
service [name] status // old Linux

systemd
/etc/systemd/system
/usr/lib/systemd/system

create a service file
[Unit]
Description=An Example Service
After=network-up.target

[Service]
ExecStart=/usr/bin/python3 /test.py

[Install]
WantedBy=multi-user.target

initd
/etc/initd

Journalctl -xe // sevices logs
Logind // linux login service
resolved // dns
```

## Network
```
nslookup sss.local # do NOT include protocol http
ufw app list //firewall app
sudo netstat//network status
```

**Apps**
- tmux
- vi/vim/nano
```
:wq
:q!

/xxx search forward
?xxx search backward
```
- certbot
- letsencrypt

# Tech stack
- qubesOS is secure Linux 
- Package Manager usually install /usr/bin
