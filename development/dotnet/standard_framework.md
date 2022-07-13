# Standard Framework

> standard framework is old closed source
> 
> static files to in root

> webconfig.xml has bunch junks

## Folder Structure
- Entity Framework V6
- /App_Start `Applications Start, Only in Standard Framework`
- /App_Data
- /Script
- /View `templates`
- /Controller
- /Areas

> custom routing https://stackoverflow.com/questions/56824966/is-there-something-like-routeconfig-cs-in-net-core-mvc

## /App_Config/RouteConfig.cs
1. create AreaRegistration instance
2. create AreaRegistrationContext(name, routes) `in flask xxx_APP = BluePrint(name)`
3. AreaRegistration.RegisterArea(AreaRegistrationContext) `in flask app.register_blueprint(xxx_APP)`

## /Areas
1. override RegisterArea(context)
2. context.MapRoute(name, route, view) `only for custom routing`

Ex route: "Sales/{controller}/{action}/{id}"

> controller = bundle of multiple route handlers 

> action = controller class's method name

> we can register multiple route in AreaRegistration point to same controller's action 



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