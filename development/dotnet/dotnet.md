# dotnet

> standard framework is old closed source

> .net core is new open source version

> linq XXX.foreach have bad performance.
use foreach XXX instead

**Route**

> Controller's File name, & method name IS part of route

> It's defined in /App_Config/RouteConfig.cs

> every files will be import according to their namespace

> (except controller)file names doesn't matter, only name space matter

> name space conflict will trigger during compile 


**RouteConfig class**

    1. create AreaRegistration instance
    2. create AreaRegistrationContext(name, routes)
    3. AreaRegistration.RegisterArea(AreaRegistrationContext)


**AreaRegistration class**

    1. override RegisterArea(context)
    2. context.MapRoute(name, route, view)

Ex route: "Sales/{controller}/{action}/{id}"

> controller = bundle of multiple route handlers 

> action = controller class's method name

> we can register multiple route in AreaRegistration point to same controller's action 

**Controller class**

    1. AsyncController(requestContext)
    2. check session
    3. build menu
    4. business logic
    5. return ActionResult (View or JsonNet or FileResult)


**XXXService class (references in controller)**
> complex business logic

**Models class**
> defined Datasource struct

**Conversion Jason <==> Data Model**

- Dictionary.TryGetValue()
- using Newtonsoft.Json;
  - JsonConvert.SerializeObject(ModelVariable)
  - JsonConvert.DeserializeObject<ModelName>(JsonObj)
- System.Web.Script.Serialization
  - new JavaScriptSerializer().Serialize(ModelVariable)
  - new JavaScriptSerializer().Deserialize(string, typeof(ModelClass))




**.Net Core**

> wwwroot to store static files

> appsetting.json

> azureKeyValut to overwrite appsetting values

**.Net Framework**
> static files to in root

> /App_Data

> /App_Start

> /Script

> /font

> webconfig.xml has bunch junks



**Ajax Request with .Net**
```
var request = new HttpRequestMessage(HttpMethod.Get, uri);
request.Headers.Add("username", username);
using (var response = Client.SendAsync(request).Result)
{
    return response.Content.ReadAsStringAsync().Result;
}
```

# DOTNET CORE
```
dotnet list package
--verbose //Flag to get more detail

//Must must *.csproj in root folder
//Or add --project XXX.csproj 
dotnet run
dotnet watch run
dotnet watch --project XXX.csproj run XXX.csproj

```

XXX.csproj

    - StartupObject // webpack.entry

**None HTTP**

HostBuilder = (NodeJS express) bare bond server
- ConfigureHostConfiguration()
- ConfigureAppConfiguration()
- UseSerilog()
- ConfigureServices()
    - services.AddOptions()  ?
    - services.AddHttpClient() ?
    - services.Configure<ClassName>(setting) 
    - services.AddDbContext()
    - services.AddSingleton()
    - services.AddScoped()
    - services.AddTransient()
    - services.AddHostedService<BackgroundService>();

> use appSetting.json property

> context.Configuration.GetSection(appSettings.json.props)
```
EX: RabbitMqService<RequestModel, Processor>
    protected override Task ExecuteAsync
    public virtual void ConnectMessageQueue
    public virtual void SetupQueue
    public virtual void SubscribeMessageQueueEvents
    public virtual void UnsubscribeMessageQueueEvents
    public virtual void DisconnectMessageQueue
    public virtual void HandleMessage
    public virtual async Task HandleMessageAsync
    public void HandleMessageError
    public void HandleMessageRetry
```

Interface define data structure,
so view can check in compile time if variable has methods

- AddTransient(Interface, Instance)
    > controller & view will get new instance
- AddScoped(Interface, Instance)
    > each request get new instance
- AddSingleton(Interface, Instance)
    > app level instance


**ASP.NET Request Process(NOT core)**

- Application_BeginRequest()
- Application_AuthenticateRequest()
- Application_AuthorizeRequest()
- Application_ProcessRequest()
- Application_EndRequest()
- Application_HandleError()

# Nuget
> setup Private Library
```
nuget sources add -name private_repo -source https://private_server/v3/index.json


VS/Tool/Options/Nuget Package Manager/Package Source
~/AppData/Roaming/NuGet/NuGet.Config
```

**Setup Repo**
```
dotnet restore(npm install)
dotnet add package XXXX(npm install XXX -s)
nuget add foo.nupkg -Source c:\bar\
dotnet tool install --global dotnet-ef (npm install -g XXX)
Install-Pack [package-name] (Only work in VS cmd)

dotnet add .Main.csproj reference .Library.csproj



dotnet list package
dotnet clean
dotnet nuget locals all --clear
```

**Publish**
```
dotnet pack -c Release /p:PackageVersion=2.0.1
nuget pack

dotnet nuget push --source [publish path] --api-key **** XXX.nupkg
dotnet publish
```

# Tech stack
> new relic is monitor software

- IIS Tilde Enumeration
    > IIS support wildcard in URL, which can expose application structure