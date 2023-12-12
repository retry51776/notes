# Mac
```bash
# Show hidden files
Press Command + Shift + . (period)

# Continue Invalid SSL website
Type 'thisisunsafe' on page

# Clear Bash History
history -c
```

# Networking
```bash
# Edit /etc/Hosts
sudo killall -HUP mDNSResponder

sudo brew services start nginx
http://localhost:8080/

vi /opt/homebrew/etc/nginx/nginx.config
vi /usr/local/etc/nginx/nginx.config

# Add certi
# 1. download cert
# 2. drag Keychain Access/System
# 3. double click cert/trust/always trust

server {
    listen 80;

    server_name k8.local;

    location / {
        proxy_pass http://127.0.0.1:8000/;
    }
}
sudo brew services restart nginx
```