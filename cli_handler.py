###########################################################
# A file that functionality that reacts to the cli commands
# Author: Piotr Wieżel
###########################################################


from mod import Mod
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

