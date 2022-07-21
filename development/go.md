# GO
> Created by google

> handle exception is kind pain, no try: catch


// Todo: I don't know much about go, just need go through basic sometime
# CMDs
```bash
go get k8s.io/client-go@v0.21.0

go build -o xxx

```
# Script
```go
import (
    "net/http"
    "log"
)

var (
    xxx = yyy()
)
var num1 int
var nums []int

func RootRsp(w http.ResponseWriter, r *http.Request){
    // r.Body
    w.Write([]byte("Hello"))
}

func main() {
    http.HandleFunc("/", RootRsp)
    log.Fatal(http.ListenAndServe(":80", nil))
}

x, err := xxxx

if err != nul {
    panic(err.Error())
}

type xxx struct {
    num1    int
    str1    string
}

flag.IntVar(&parameters.xxx, "xxx", 123, "Default value is 123")
flag.Parse()
print(parameters.xxx)
```