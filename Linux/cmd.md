# Linux

**OS** 
```
passwd //Change password

uname -a //Display OS info
df -ah  //show disk usage
du -sh [path-name] // disk usage

top //linux task manager
htop

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
Service/Cronjob/Dev
```
crontab –l
service [name] status // old Linux
# To debug Ram & time
time -f python3 test.py

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
Network
```
nslookup sss.local # do NOT include protocol http
ufw app list //firewall app
sudo netstat//network status
```
### Package Manager
- apt-get
- dpkg
- yum
- RPM
- pacman


**Apps**
- tmux
- vi/vim/nano
```
:wq
:q!

/xxx search forward
?xxx search backward
```
- 
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
**Windows Sub Linux**
Try remove windows path from WSL if cmd in WSL is slow
- In `/etc/wsl.conf` add
```
[interop]
appendWindowsPath = false
```
# Tech stack
- qubesOS is secure Linux 
- Package Manager usually install /usr/bin
