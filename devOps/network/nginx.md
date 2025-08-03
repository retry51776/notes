# Nginx
>
> most common load balancer
> Default Logs path `/var/log/nginx/access.log or error.log`

#### proxy_pass vs redirect

`redirect` means tell client look someplace else
`proxy_pass` is server get stuff from elsewhere & client's url doesn't change

#### Add custom format to ngnix

```
log_format custom_log  '$remote_addr - $remote_user [$time_local] "$request" $status "$http_referer" '
                               '"$http_user_agent" "$http_x_forwarded_for"';

access_log /var/log/nginx/xxxx custom_log;
```

## Address can be

- domain name
- ip
- port
- unix socket
- upstream name
- variable

## scope level

- http
- server
- location
- upstream

## upstream

```bash
upstream notes {
    # ip_hash
    # hash
    # least_conn
    # least_time
    # random

    server 1.1.1.1:80 weight=5 max_fails=3 fail_timeout=30s;
    server 1.1.1.2:80;
    server 1.1.1.3:80;

    # sticky cookie my_cookie expires=1h domain=.notes.com path=/;
}

# this will auto become upstream adddress
http://notes 
```

## Common Header Operations

```bash
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

proxy_pass 

http
```
