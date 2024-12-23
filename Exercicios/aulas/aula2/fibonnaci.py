FibArray = [0, 1]


def fibonacci_dynamic(n):
    if n < 0:
        print("Incorrect input")
    elif n <= len(FibArray):
        return FibArray[n - 1]
    else:
        temp_fib = fibonacci_dynamic(n - 1) + fibonacci_dynamic(n - 2)
        FibArray.append(temp_fib)
        return temp_fib


def fibonacci_rec(n):
    if n < 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


print(fibonacci_dynamic(9))
print(fibonacci_rec(9))
