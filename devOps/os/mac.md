# Mac

```bash
# Show hidden files
Press Command + Shift + . (period)

# Continue Invalid SSL website
Type 'thisisunsafe' on page

# Clear Bash History
history -c

# Find none apple .pkg
pkgutil --pkgs | grep -v '^com.apple'
```

## Homebrew

- untap - 3rd party repo `brew untap xxx`
- `--cask` - apple apps `brew install --cask visual-studio-code`

## Keychain

Password App is GUI of keychain;

- Login - The default for your user account. It stores personal passwords and certificates.
- iCloud - Syncs passwords and credit card information across all your Apple devices.
- System - Stores credentials required by all users, such as Wi-Fi passwords and system-wide certificates.
- System Roots - A read-only keychain containing the root certificates trusted by Apple to secure the entire operating system.

## Networking

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

## launchctl
>
> similar to service_management in windows

`plutil -lint ~/Library/LaunchAgents/com.whisperf5.agent.plist`

## Swift

`package.swift/package.targets.path` → `folder/main.swift` | `@main` →

```swift
init()
deinit()

// Compiled path
// ~/Library/Developer/Xcode/DerivedData/

// Swift Package Manager (SPM)
swift package resolve
```
