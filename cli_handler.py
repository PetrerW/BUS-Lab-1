###########################################################
# A file that functionality that reacts to the cli commands
# Author: Piotr Wiezel
###########################################################


from mod import Mod
from egcd import egcd
import random


class Handler:
    # Input choice = 1
    # return a <operation> b mod p
    # a,b,p < 100
    @staticmethod
    def handle_small_numbers(a, b, operation, p):
        if operation == '+':
            return Mod(a+b, p)
            # return int(a + b % p)
        elif operation == '-':
            return Mod(a-b, p)
            # return int(a - b % p)
        elif operation == '*':
            return Mod(a*b, p)
            # return int(a * b % p)
        elif operation == '/':
            return Mod(a/b, p)
            # return int(a / b % p)
        else:
            return None

    @staticmethod
    def handle_large_numbers(a, b, operation, p):
        """if operation == '+':
            return int(a + b % p)
        elif operation == '-':
            return int(a - b % p)
        elif operation == '*':
            return int(a * b % p)
        elif operation == '/':
            return int(a / b % p)
        else:
            return None
        """

        return Handler.handle_small_numbers(a, b, operation, p)

    # A function that generates a random number of num_t
    # Returns None if the output wouldn't be an integer
    @staticmethod
    def generate_big_numbers(bits):
        if bits > 1:
            return random.randrange(2**(bits-1), 2**bits)
        else:
            return None

    # https://gist.github.com/ofaurax/6103869014c246f962ab30a513fb5b49
    # Took from SO
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

    @staticmethod
    def modinv(a, m):
        g, x, y = egcd(a, m)
        if g != 1:
            return 'No modular inverse'

        return x % m

