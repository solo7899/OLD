def fibonacci(limit):
    first = 1
    second = 2
    fib_list = [1, 2,]

    while second <= limit:
        third = first + second
        first = second
        second = third

        fib_list.append(third)
    return fib_list

def is_even(n):
    return n % 2 == 0

if __name__ == "__main__":
    limit = 4_000_000
    list = fibonacci(limit)

    sum = 0
    for i in list:
        if is_even(i):
           sum += i

    print(sum)