> Most the code will be .net core

### Session
```
SessionStore.isAuthenticated()
```
### Generate JWT
```
using JWT.Builder;
using JWT.Algorithms;

var payload = new Dictionary<string, object>()
{
    {"xxx", 123},
    {"yyy", 123},
}

return new JwtBuilder()
    .WithAlgorithm(new xxxAlgorithm())
    .WithSecret('123')
    .AddClaims(payload)
    .Encode();
```

### URI
> Request, Response will auto injected by .net core (I dont like it, no idea where it came from)
```
print(Request.QueryString['q']);


UriBuilder req = new UriBuilder('google.com?q=abc');
var query = HttpUtility.ParseQueryString(req.Query);
query['q'] = 'efg';
req.Query = query.ToString();
// req.Path = '';
Response.Redirect(req.Uri.ToString())
```