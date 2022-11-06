# GO
> Created by google

> handle exception is kind pain, no try: catch

# Structure
- `go.mod` similar requirement.txt & setup.py
- `go.sum` similar package.lock
- `Makefile`
- `/cmd`
- `main.go`

# CMDs
```bash
go get k8s.io/client-go@v0.21.0

go build -o xxx

```

# Script
```go
package main

import (
    "net/http"
    "log"
)
import "fmt"

var (
    xxx = yyy()
	ToBe   bool       = false
	MaxInt uint64     = 1<<64 - 1
	z      complex128 = cmplx.Sqrt(-5 + 12i)
)
var num1 int
var nums []int

func RootRsp(w http.ResponseWriter, r *http.Request){
    // r.Body
    w.Write([]byte("Hello"))
}

func main() {
    defer fmt.Println("defer makes print called main() is exited")
    http.HandleFunc("/", RootRsp)
    log.Fatal(http.ListenAndServe(":80", nil))
    m := make(map[string]int)
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

type executor struct {
	executors.AbstractExecutor
}
// golang's way defined nested method; not very readable, avoid multiple level nested
func (e *executor) reset() {
    print("executor.reset is called")
}

var eee executor
eee_pointer = &eee
(*eee_pointer).reset()
```