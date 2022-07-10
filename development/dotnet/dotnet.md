# dotnet
> .net core is new open source version

> linq XXX.foreach have bad performance.
use foreach XXX instead

> base = super

> usually existed a base_controller class acted as middleware, and all other controller based of base_controller
**Route**

> Controller's File name, & method name IS part of route

> It's defined in /App_Config/RouteConfig.cs

> every files will be import according to their namespace

> (except controller)file names doesn't matter, only name space matter

> name space conflict will trigger during compile 


**RouteConfig class**

1. create AreaRegistration instance
2. create AreaRegistrationContext(name, routes) `in flask xxx_APP = BluePrint(name)`
3. AreaRegistration.RegisterArea(AreaRegistrationContext) `in flask app.register_blueprint(xxx_APP)`


**AreaRegistration class**

1. override RegisterArea(context)
2. context.MapRoute(name, route, view) `only for custom routing`

Ex route: "Sales/{controller}/{action}/{id}"

> controller = bundle of multiple route handlers 

> action = controller class's method name

> we can register multiple route in AreaRegistration point to same controller's action 

**Controller class**

1. AsyncController(requestContext) `in flask requestContext = req`
2. check session
3. business logic
4. return ActionResult (View or JsonNet or FileResult)

## requestContext
requestContext.HttpContext.Request.Url

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

**Ajax Request with .Net**
```
var request = new HttpRequestMessage(HttpMethod.Get, uri);
request.Headers.Add("username", username);
using (var response = Client.SendAsync(request).Result)
{
    return response.Content.ReadAsStringAsync().Result;
}
```


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


## ASP.NET Request Lifecycle

/Global.asax.cs
- Applocation_Start
- Application_BeginRequest()
- Application_AuthenticateRequest()
- Application_AuthorizeRequest()
- Application_ProcessRequest()
- Application_EndRequest()
- Application_HandleError()
- Applocation_End

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

```
public interface IXXX
{
    String xx { get; set; }
    bool enable { get; set; }
    String toHTML();  `return String.Format(<h1>{0}</h1>, "Test")`
}
```