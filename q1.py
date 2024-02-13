def is_prime_num(num): 
    if (num <= 1):
        return False; 
    else: 
        for i in range(2, num): 
            if (num % i == 0): 
                return False; 
            else: 
                return True;

def getPrimeNumbers(n): 
    primes = []; 
    for num in range(2, n+1):
        if is_prime_num(num):
            primes.append(num)
    return primes;


print(getPrimeNumbers(5))
