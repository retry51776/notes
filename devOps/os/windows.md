# Windows
```powershell
# List all port usage
Get-NetTCPConnection
# What Process uses which Port
Get-Process -Id (Get-NetTCPConnection -LocalPort YourPortNumberHere).OwningProcess
```
// TODO: some WSL setup problem

// GCP, console setup