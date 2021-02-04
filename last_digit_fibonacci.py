# Naive Solution:
def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


# Efficient Solution:
def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    fib = [1, 1]
    for i in range(2, n):
        value = (fib[i - 1] + fib[i - 2]) % 10
        fib.append(value)

    return fib[-1]


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
