"""
In this file we have one functional element as fibonacci function.
"""


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(int(input("Enter number: "))))
