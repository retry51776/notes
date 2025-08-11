// development/dotnet/standard_framework.md
# Standard Framework

> The standard framework is old and closed‑source.

Static files are placed in the root directory.

`Web.config` contains many settings (in .NET Core this was replaced by `appsettings.json`).

## Folder Structure

- Entity Framework V6
- `/App_Start` – application start logic (only in Standard Framework)
- `/App_Data`
- `/Script`
- `/View` – templates
- `/Controller`
- `/Areas`
- `.sln` – solution file, defines how many apps are inside the repository
- `Web.config`

> Custom routing: https://stackoverflow.com/questions/56824966/is-there-something-like-routeconfig-cs-in-net-core-mvc

## /App_Config/RouteConfig.cs

```csharp
// Example of a typical RouteConfig file
using System.Web.Routing;
using System.Web.Mvc;

public class RouteConfig
{
    public static void RegisterRoutes(RouteCollection routes)
    {
        routes.IgnoreRoute("{resource}.axd/{*pathInfo}");

        // Default route
        routes.MapRoute(
            name: "Default",
            url: "{controller}/{action}/{id}",
            defaults: new { controller = "Home", action = "Index", id = UrlParameter.Optional }
        );
    }
}
```

## ASP.NET Request Lifecycle

`Global.asax.cs`

- `Application_Start`
- `Application_BeginRequest`
- `Application_AuthenticateRequest`
- `Application_AuthorizeRequest`
- `Application_ProcessRequest`
- `Application_EndRequest`
- `Application_HandleError`
- `Application_End`
