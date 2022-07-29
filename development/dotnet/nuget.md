# Nuget
> setup Private Library
```bash
nuget sources add -name private_repo -source https://private_server/v3/index.json


VS/Tool/Options/Nuget Package Manager/Package Source
~/AppData/Roaming/NuGet/NuGet.Config
```



**Setup Repo**
```bash
dotnet restore(npm install)
dotnet add package XXXX(npm install XXX -s)
nuget add foo.nupkg -Source c:\bar\
dotnet tool install --global dotnet-ef (npm install -g XXX)
Install-Pack [package-name] (Only work in VS cmd, similar to npm install)

dotnet add .Main.csproj reference .Library.csproj



dotnet list package
dotnet clean
dotnet nuget locals all --clear
```

**Publish**
```bash
dotnet pack -c Release /p:PackageVersion=2.0.1
nuget pack

dotnet nuget push --source [publish path] --api-key **** XXX.nupkg
dotnet publish
```
