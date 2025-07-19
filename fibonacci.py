# Fibonacci


# * V1
def fibonacci_list(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib


# * V2
def fibonacci_variables(n):
    if n <= 0:
        return []
    a, b = 0, 1
    result = [a]
    for _ in range(1, n):
        result.append(b)
        a, b = b, a + b
    return result


# * V3
from functools import lru_cache


@lru_cache(maxsize=None)
def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fibonacci_recursive(n):
    return [fib_recursive(i) for i in range(n)]


# * V4
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    print(f"\nLista: {fibonacci_list(5)}\n")
    print("==============================")
    print(f"\nVariables temporales: {fibonacci_variables(5)}\n")
    print("==============================")
    print(f"\nRecursiva: {fibonacci_recursive(5)}\n")
    print("==============================")
    print(f"\nGenerador: {list(fibonacci_generator(5))}\n")
