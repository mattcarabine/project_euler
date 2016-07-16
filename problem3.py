import math

INPUT_VALUE = 600851475143


def main():
    # We can reduce the primes we need to calculate by 
    # only calculating up to the square root of the number
    # As we know the highest prime factor cannot exceed that
    primes = get_primes(int(math.sqrt(INPUT_VALUE)))
    highest_prime = primes.pop()
    while INPUT_VALUE % highest_prime > 0:
        highest_prime = primes.pop()

    print highest_prime

def get_primes(max_number):
    is_prime = [True for i in xrange(max_number)]
    for i in xrange(2, int(math.sqrt(max_number))):
        if is_prime[i]:
            j = i ** 2
            while j < max_number:
                is_prime[j] = False
                j += i
    
    return [i for i in xrange(max_number) if is_prime[i]]

if __name__ == '__main__':
    main()