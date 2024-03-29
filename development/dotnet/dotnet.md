# dotnet core
- Common Language Specification (CLS)
- Framework Class Library (FCL) `package in python, EX: ASP.NET(flask), WinForm, ADO.Net`
  - Base Class Library (BCL) `aka standard lib, Ex: system, os, io`
> .net core is new open source version

> linq XXX.foreach have bad performance.
use foreach XXX instead

> base = super

> app.UseXXX ususally is middleware

> services.AddXXX Usually is setup service `similar flask app.xxx = YYY`

## Folder Structure
- /wwwroot `to store static files`
- /appsetting.json `azureKeyValut to overwrite appsetting.json values`
- /Properties `similar to .vscode`
- /Controllers
- /Models
- /Views

# Deployment & Development
> Ways to set ASPNETCORE_ENVIRONMENT
```
# 1. Default location
/Properties/launchSettings.json
# 2. Go into container & change it
$Env:ASPNETCORE_ENVIRONMENT = "Development"
# 3. During publish package
dotnet publish -c Debug -r win-x64 /p:EnvironmentName=Development
# 4. Though docker-development.env
ASPNETCORE_ENVIRONMENT=Development


appsettings.json # Define Apps, kind replaced .sln file
```
>
## ASP.NET Application Workflow
- Main()
- Host.CreateDefaultBuilder
- Startup.cs
    - ConfigureServices()
        - AddDbContext()
        - AddControllers()
        - AddCors()
        - AddSession()
        - AddSingleton()
        - AddScoped()
    - Configure()
        - UseRouting() `aka BluePrint`
        - UseCors()
        - UseSession()


## /Controller `same for .net standard`

> Controller's File name, & method name IS part of route

> Custom Route can be defined in `/App_Config/RouteConfig.cs`

> every files will be import according to their namespace

> (except controller)file names doesn't matter, only name space matter

> name space conflict will trigger during compile 

> requestContext `requestContext.HttpContext.Request.Url`

1. AsyncController(requestContext) `in flask requestContext = req`
2. check session
3. business logic
4. return ActionResult (View or JsonNet or FileResult)

## /.vscode
    /launch.json
    /settings.json
    /task.json
    /extensions.json

## /Services
> complex business logic `most likely init during ConfigureServices(), then refereed in controller`

## /Models
> defined Datasource structure

## /Properties
> launchSettings.json store different envs, will overwrite in Production

# Coding
**Conversion Jason <==> Data Model**

- Dictionary.TryGetValue()
- using Newtonsoft.Json;
  - JsonConvert.SerializeObject(ModelVariable)
  - JsonConvert.DeserializeObject<ModelName>(JsonObj)
- System.Web.Script.Serialization
  - new JavaScriptSerializer().Serialize(ModelVariable)
  - new JavaScriptSerializer().Deserialize(string, typeof(ModelClass))


## Ajax Request with .Net
```cs
var request = new HttpRequestMessage(HttpMethod.Get, uri);
request.Headers.Add("username", username);
using (var response = Client.SendAsync(request).Result)
{
    return response.Content.ReadAsStringAsync().Result;
}
```


```bash
dotnet list package
--verbose #Flag to get more detail

# Must must *.csproj in root folder
# Or add --project XXX.csproj 
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
```cs
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


```c#
BlockingCollection bc - new BlockingCollection();
bc.Add();
bc.Add();
bc.CompleteAdding();

foreach (var x in bc.GetConsumingEnumerable())
{
    // task x
}
```

### MiniProfiler
> shows stack run time
```
1. Install
2. StartUp.cs create instance `services.AddMiniProfiler()`
3. Add decorator before inspect method
4. Add <mini-profiler /> to view
5. Go to view
```

# Tech stack
> new relic is monitor software

- IIS Tilde Enumeration
    > IIS support wildcard in URL, which can expose application structure

```cs
public interface IXXX
{
    String xx { get; set; }
    bool enable { get; set; }
    String toHTML();  `return String.Format(<h1>{0}</h1>, "Test")`
}
```

## Naming Pattern
- onXXX `takes event as param`
- xxxHandler `callback`