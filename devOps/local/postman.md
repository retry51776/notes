# Postman
> At this point it's like a full IDE or browser

1. Step Up Collection Folder & Create Request for openApi `/api/v1/schema/?format=json`
2. Set Up Env to able adjust to different server
3. Set Up Auth request; `Hopefully there is good docu`
4. In Auth request/Tests `pm.environment.set('token', pm.response.json().token)` to save JWT into environment variable; Add `console.log()` to confirm 
5. Dependence on how api accepts token, attach env token to header or body

