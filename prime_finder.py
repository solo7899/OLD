import time

def is_prime(number):
    prime = True
    for i in range(2, int(number//2)+1):
        if number % i == 0:
            prime = False
            break
    return number, prime

def announce(number, prime):
    print(f"{number} {'is' if prime else 'is not'} prime")

if __name__ == "__main__":
    number = int(input("Enter a Number > "))
    prime_counter = 0
    a = time.time()
    for i in range(2, number + 1):
        number, prime = is_prime(i)
        if prime:
            prime_counter += 1
    b = time.time()
    print('we have', prime_counter, 'prime numbers')
    print(f'it took {b-a:.2f} seconds to operate.')

