# Naive Solution:
def fibonacci_number_naive(n):

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


# Efficient Solution:
def fibonacci_number(n):

    if n <= 1:
        return n

    fib = [1, 1]
    for i in range(2,n):
        value = fib[i - 1] + fib[i - 2]
        fib.append(value)

    return fib[-1]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))