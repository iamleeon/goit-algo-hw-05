# the outer fuction creates an empty cache dict and returns the inner function
def caching_fibonacci():
    cache = dict()
    # the inner function calculates the Fibonacci sequence and adds the calculations for each
    # number into the cache dict so the next time the calculation is made the result is
    # taken from the cache dict instead of calculating  
    def fibonacci(number):
        if number <= 0:
            return 0
        elif number == 1:
            return 1
        elif number in cache:
            return cache[number]
        cache[number] = fibonacci(number - 1) + fibonacci(number - 2)
        return cache[number]
    return fibonacci

# creating a variable the the fibonacci func
fib = caching_fibonacci()

# examples of using the fibonacci func for calculating Fibonacci sequence
print(fib(10))  # prints 55
print(fib(15))  # prints 610
