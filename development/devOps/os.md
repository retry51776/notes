#Linux OS

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


**SystemD**
check logs
journalctl -fu nginx

/proc is virtual file refect process info
linux make everything as file

```
lsof "list open files"
ss -tunapl "socket process"

```