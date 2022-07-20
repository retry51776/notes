# js
```js

var keycloak = new Keycloak({
    store: memoryStore
});

app.use(keycloak.middleware({
    logout: '/logout',
    admin: '/'
}))

app.get('/secure', keycloak.protext('realm:user'), function(req, res) => do_secure())
```