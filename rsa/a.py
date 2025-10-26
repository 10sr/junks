#!/usr/bin/env python3

import math
import random
from random import randint

# https://github.com/wiktorlazarski/RSA-Digital-Signature/blob/112047390f0e9c5c2c2245a492d76d37785e2c56/source_code/rsa_keys.py
def list_primes(lo, hi):
	'''Returns a list of prime numbers in a given range [lo, hi).

		Parameters:
		lo (int): lower boundary of search space
		hi (int): higher boundary of search space

		Returns:
		[]: list of prime numbers between [lo, hi)
	'''
	primes = []
	for num in range(lo, hi, 2):
		for i in range(2, num):
			if num % i == 0:
				break
		else:
			primes.append(num)

	return primes

primes = list_primes(3, 5000)

# https://github.com/wiktorlazarski/RSA-Digital-Signature/blob/112047390f0e9c5c2c2245a492d76d37785e2c56/source_code/rsa_keys.py
def mod_inverse(e, phi_n):
    d = e
    while (e * d) % phi_n != 1: d = d + 1
    return d

def gen_key():
    # RSA Key Generation
    p, q = random.sample(primes, 2)

    n = p * q
    totient_n = (p - 1) * (q - 1)

    # Find a number "e" that is coprime to the "totient_n"
    e = randint(3, totient_n - 1)

    while math.gcd(e, totient_n) != 1:
        e = randint(3, totient_n - 1)

    d = mod_inverse(e, totient_n)

    return {
        "pub": (e, n),
        "sec": (d, n),
    }


print(gen_key())
