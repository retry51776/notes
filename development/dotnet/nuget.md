// development/dotnet/nuget.md
# NuGet

> Setup a private library.

```bash
nuget sources add -name private_repo -source https://private_server/v3/index.json
```

VS → Tools → Options → NuGet Package Manager → Package Sources  
`%USERPROFILE%\AppData\Roaming\NuGet\NuGet.Config`

## Setup Repository

```bash
dotnet restore          # (npm install)
dotnet add package XXXX # (npm install XXX -s)
nuget add foo.nupkg -Source c:\bar\
dotnet tool install --global dotnet-ef   # (npm install -g XXX)

# Install-Pack [package-name] works only in the VS command prompt, similar to npm install

dotnet add .Main.csproj reference .Library.csproj

dotnet list package
dotnet clean
dotnet nuget locals all --clear
```

## Publish

```bash
dotnet pack -c Release /p:PackageVersion=2.0.1
nuget pack

dotnet nuget push --source [publish path] --api-key **** *.nupkg
dotnet publish
```
