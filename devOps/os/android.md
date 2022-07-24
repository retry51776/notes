# Android

> Team Win Recovery Team is a bootloader
> All android comes with a bootloader,  usually only have a simple recovery feature. 
> Some android may locked bootloader.

> MagicMask is unrooting software install inside TWRT, get admin access on phone.

> ROM is Android OS image. 


```
.\adb.exe connect 192.168.0.26:5555
.\adb.exe reboot update
.\adb.exe shell
getprop
setprop persist.sys.set_adb_disabled false
[persist.service.adb.enable]: [0]
```

Important paths
/data/property --default props
