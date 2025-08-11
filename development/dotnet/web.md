// development/dotnet/web.md
> Most of the code will be .NET Core

### Session
```cs
SessionStore.IsAuthenticated()
```

### Generate JWT
```cs
using JWT.Builder;
using JWT.Algorithms;

var payload = new Dictionary<string, object>()
{
    {"xxx", 123},
    {"yyy", 123},
};

return new JwtBuilder()
    .WithAlgorithm(new XxxAlgorithm())
    .WithSecret("123")
    .AddClaims(payload)
    .Encode();
```

### URI
> Request and response will be auto‑injected by .NET Core (I don’t like it; I have no idea where it came from).

```cs
print(Request.QueryString["q"]);

var req = new UriBuilder("https://google.com?q=abc");
var query = HttpUtility.ParseQueryString(req.Query);
query["q"] = "efg";
req.Query = query.ToString();
// req.Path = "";
Response.Redirect(req.Uri.ToString());
```
