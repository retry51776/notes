# Linux OS 
> qubesOS is secure Linux 

> /proc is virtual file reflect process info
linux make everything as file

> CMDs `[application] [options] [command] [command options] [arguments...]`

## Boot Order
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

# Linux Apps

Free Software Foundation (FSF) 

GNU is list of open source linux components

### Compilers
- make
  > Makefile: create rules, assign cmd to rule, chain rules
- GNU Compiler Collection (GCC)


## Package Manager 
> Think of apple app store, android app store
> 
> Package Manager usually install /usr/bin

- apt-get
- dpkg
- yum
- RPM
- pacman

```bash
sudo apt install strace	#Debian/Ubuntu 
# yum install strace		#RHEL/CentOS
# dnf install strace		#Fedora 22+

which pg_config
apk add pg_config
apk info --who-owns /usr/bin/pg_config

# Used By Debain
apt
# red hat, syntom
rpm
```

### OS CMDs
```bash
# Current OS info
cat /etc/os-release

# Similar to task manager in Windows 
htop
top

# network manager
iftop

# linux process
procps
strace

# Memory
free -h

# Find file
find / -name "xxx.config"

# Show Folder Structure
tree

# Change password
passwd

# Display OS info
uname -a
# show disk usage
df -ah
du -sh [path-name]


vi test.txt
cat test.txt

less //cat large files  /[search_text]
grep [word] [seach_path] //text search

echo hello > test.txt //Overwrite
echo hello >> test.txt //Append

# past cmd
history
```

### Permission
```bash
# Change permission on file
chmod -R 660 /app

sudo chown user_name file_name
chmod u+x file_name
chomd [owner][group][other] file_name
    - u:user;
    - g:group;
    - o:other users;

    - r:4:read
    - w:2:write
    - x:1:excute

# These two files defines noroot user
# /etc/subuid
# /etc/subgid
```

## Service / Cronjob / Dev
```bash
# Show cronjobs
crontab –l
# Show Service status
service [name] status

# create systemd service file @
# /etc/systemd/system
# /usr/lib/systemd/system
# Start of demo.service file
[Unit]
Description=An Example Service
After=network-up.target

[Service]
ExecStart=/usr/bin/python3 /demo.py
User=root
Restart=always
RestartSec=1

[Install]
WantedBy=multi-user.target
# End of service file

# systemctl start demo
initd
/etc/initd

# sevices logs
Journalctl -xe
# linux login service
Logind
# dns
resolved
```

### Network CMDs
```bash
# do NOT include protocol http
nslookup sss.local
# firewall app
ufw app list
# network status
sudo netstat

# list open files
lsof
# socket process
ss -tunapl

# check logs
journalctl -fu nginx
```

### Editors
> Don't know how to get out vim? It happened to me too, lol
- tmux
- vi/vim/nano
```bash
:wq
:q!

/xxx search forward
?xxx search backward
```

LVM (Logical Volume Manager)
- LV (Logic Volume) `eqs to partition`
- VG (Volume Group) `eqs to hard drive`
- PV (Physical Volume) ` 1:1 to partition`
```bash
# Disk Scan
lvmdiskscan

# Create partition
gparted 

# PV
pvscan
pvcreate /dev/sdb1

# VG
vgscan
vgextend target_vol_grp_name /dev/sdb1

# LV
lvscan

```