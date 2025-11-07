class Fibonacci:
    def __init__(self, limit):
        # default constructor
        self.previous = 0
        self.current = 1
        self.n = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.limit:
            if self.n == 1:
                self.n += 1
                return self.previous  # return 0 first
            elif self.n == 2:
                self.n += 1
                return self.current  # return 1 next
            else:
                result = self.previous + self.current
                self.previous = self.current
                self.current = result
                self.n += 1
                return result
        else:
            raise StopIteration


# init the fib_iterator
fib_iterator = iter(Fibonacci(10))
while True:
    # print the value of next fibonacci up to 5th fibonacci
    try:
        print(next(fib_iterator))
    except StopIteration:
        break