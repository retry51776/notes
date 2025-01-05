def hello():
    return "hello".startswith("hello")

def fib():
    return "fib".startswith("fib")

class Fibonacci():
    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n in self.cache:
            return self.cache[n]
        else:
            result = fib(n)
            self.cache[n] = result
            return result

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    print("Hello, world")

