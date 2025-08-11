// development/dotnet/dotnet.md
# .NET Core

- **Common Language Specification (CLS)**
- **Framework Class Library (FCL)** – analogous to Python packages, e.g., ASP.NET (Flask), WinForms, ADO.NET  
  - **Base Class Library (BCL)** – the standard library (`System`, `IO`, etc.)

> .NET Core is the new open‑source version.

> LINQ’s `ForEach` has poor performance; use a regular `foreach` loop instead.

> `base = super`

> `app.UseXXX` is usually middleware.

> `services.AddXXX` typically registers a service (similar to `app.xxx = YYY` in Flask).

## Folder Structure

- `/wwwroot` – static files  
- `appsettings.json` – configuration (Azure Key Vault can overwrite values)  
- `/Properties` – similar to `.vscode` settings  
- `/Controllers`  
- `/Models`  
- `/Views`

# Deployment & Development

### Ways to set `ASPNETCORE_ENVIRONMENT`

```bash
# 1. Default location
/Properties/launchSettings.json

# 2. Inside a container
$Env:ASPNETCORE_ENVIRONMENT = "Development"

# 3. During publish
dotnet publish -c Debug -r win-x64 /p:EnvironmentName=Development

# 4. Via environment file (e.g., docker-development.env)
ASPNETCORE_ENVIRONMENT=Development
```

`appsettings.json` defines application settings and replaces the old `.sln` configuration.

## ASP.NET Application Workflow

- `Main()`
- `Host.CreateDefaultBuilder`
- `Startup.cs`
  - `ConfigureServices()`
    - `AddDbContext()`
    - `AddControllers()`
    - `AddCors()`
    - `AddSession()`
    - `AddSingleton()`
    - `AddScoped()`
  - `Configure()`
    - `UseRouting()` – “blueprint” for endpoints  
    - `UseCors()`
    - `UseSession()`

## Controllers (same for .NET Standard)

- The controller’s file name and method name are part of the route.  
- Custom routes can be defined in `/App_Config/RouteConfig.cs`.  
- All files are imported according to their namespace; only namespaces matter, not file names.  
- Namespace conflicts cause compile‑time errors.

### Typical Request Flow

1. `AsyncController(requestContext)` – analogous to Flask’s `requestContext = req`  
2. Check session  
3. Execute business logic  
4. Return an `ActionResult` (View, JSON, or File)

## VS Code Configuration (`/.vscode`)

- `launch.json`
- `settings.json`
- `tasks.json`
- `extensions.json`

## Services

Complex business logic is usually initialized in `ConfigureServices()` and then referenced in controllers.

## Models

Define data structures used throughout the application.

## Properties

`launchSettings.json` stores environment‑specific settings that are overridden in production.

# Coding

**Conversion JSON ↔ Data Model**

```csharp
// Serialize
var json = JsonConvert.SerializeObject(modelInstance);

// Deserialize
var model = JsonConvert.DeserializeObject<ModelType>(json);
```

- `Dictionary.TryGetValue()`
- Using `Newtonsoft.Json` (`JsonConvert`)  
- Using `System.Web.Script.Serialization`:
  ```csharp
  var serializer = new JavaScriptSerializer();
  string json = serializer.Serialize(modelInstance);
  var obj = serializer.Deserialize<ModelType>(json);
  ```

## Ajax Request with .NET

```csharp
var request = new HttpRequestMessage(HttpMethod.Get, uri);
request.Headers.Add("username", username);
using (var response = client.SendAsync(request).Result)
{
    return response.Content.ReadAsStringAsync().Result;
}
```

```bash
dotnet list package
--verbose   # Flag to get more detail

# Must have a *.csproj file in the root folder,
# or specify one with --project <file.csproj>
dotnet run
dotnet watch run
dotnet watch --project <file.csproj> run
```

### Example `XXX.csproj`

```xml
<Project Sdk="Microsoft.NET.Sdk.Web">
  <!-- ... -->
</Project>
```

## Non‑HTTP Host Builder (similar to a bare Node.js Express server)

- `ConfigureHostConfiguration()`
- `ConfigureAppConfiguration()`
- `UseSerilog()`
- `ConfigureServices()`
  - `services.AddOptions()`
  - `services.AddHttpClient()`
  - `services.Configure<ClassName>(settings)`
  - `services.AddDbContext()`
  - `services.AddSingleton()`
  - `services.AddScoped()`
  - `services.AddTransient()`
  - `services.AddHostedService<BackgroundService>()`

> Use `appsettings.json` for configuration values.  
> Access them via `context.Configuration.GetSection("sectionName")`.

```csharp
// Example usage with RabbitMQ
public class RabbitMqService<RequestModel, Processor>
{
    protected override Task ExecuteAsync(CancellationToken stoppingToken) { /* ... */ }
    public virtual void ConnectMessageQueue() { /* ... */ }
    public virtual void SetupQueue() { /* ... */ }
    public virtual void SubscribeMessageQueueEvents() { /* ... */ }
    public virtual void UnsubscribeMessageQueueEvents() { /* ... */ }
    public virtual void DisconnectMessageQueue() { /* ... */ }
    public virtual void HandleMessage() { /* ... */ }
    public virtual async Task HandleMessageAsync() { /* ... */ }
    public void HandleMessageError(Exception ex) { /* ... */ }
    public void HandleMessageRetry() { /* ... */ }
}
```

### Service Lifetimes

- `AddTransient(Interface, Implementation)` – a new instance per injection (controller & view get a fresh instance).  
- `AddScoped(Interface, Implementation)` – a new instance per request.  
- `AddSingleton(Interface, Implementation)` – one instance for the entire application.

```csharp
var bc = new BlockingCollection<int>();
bc.Add(1);
bc.Add(2);
bc.CompleteAdding();

foreach (var x in bc.GetConsumingEnumerable())
{
    // Process item x
}
```

### MiniProfiler

> Shows stack execution time.

1. Install the package.  
2. In `Startup.cs`, add `services.AddMiniProfiler()`.  
3. Decorate methods you want to profile.  
4. Add `<mini-profiler />` to your view.  
5. Open the view in a browser to see profiling results.

# Tech Stack

- New Relic – monitoring software.

## IIS Tilde Enumeration

> IIS supports wildcards in URLs, which can expose application structure.

```csharp
public interface IXXX
{
    string Xx { get; set; }
    bool Enable { get; set; }
    string ToHTML(); // Returns formatted HTML, e.g., $"<h1>{value}</h1>"
}
```

## Naming Conventions

- `OnXxx` – event handler that takes an event argument.  
- `XxxHandler` – callback method.
