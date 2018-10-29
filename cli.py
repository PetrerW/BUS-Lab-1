###########################################################
# A file that functionality that reacts to the cli commands
# Author: Piotr Wieżel
###########################################################

import sys
from typing import Optional, Any

from cli_handler import Handler

# author: Piotr Wieżel


class CLI:
    __line = '=============================================='

    __space = '             '

    __title = __line + '\n' + __space + 'Modulo algebra numbers calculator\n' + __line

    __options = '0 - exit\n1 - small numbers\n2 - large numbers\n'

    __small_numbers_title = __line + '\n' + __space + 'Modulo algebra numbers calculator\n' + __space + '\n' +\
    'Small numbers calculator\n' + __line

    __large_numbers_title = __line + '\n' + __space + 'Modulo algebra numbers calculator\n' + __space + '\n' +\
    'Small numbers calculator\n' + __line

    __enter_operation = 'Please enter one of the operations:\n+\n-\n*\n/\n'

    __operations = ['+', '-', '*', '/']

    __enter_a = 'Please enter the first number\n'

    __enter_b = 'Please enter the second number\n'

    __enter_p = 'Please enter the modulo number'

    def run(self):
        while(1):
            self.write_fist_info()
            self.read_first_choice()
            print('To continue press any key')
            sys.stdin.read()

    def write_fist_info(self):
        # Write a header and first info in the program
        print(self.__title)
        print(self.__options)

    def read_first_choice(self):
        choice = sys.stdin.read()
        choice = choice.replace('\n', '')
        if choice == '0':
            exit()
        elif choice == '1':
            self.small_numbers()
        elif choice == '2':
            self.large_numbers()
        else:
            print('Wrong input data. Please enter a number (0-2)')

    # Operate on the small numbers
    def small_numbers(self):
        # Please enter the operation...
        print(self.__enter_operation)
        operation_choice = sys.stdin.read()
        operation_choice = operation_choice.replace('\n', '')

        if self.__operations.__contains__(operation_choice):
            # Please enter number...
            print(self.__enter_a)
            # TODO: Make it fool-resilient
            a = sys.stdin.read()
            a = int(a.replace('\n', ''))

            print(self.__enter_b)
            # TODO: Make it fool-resilient
            b = sys.stdin.read()
            b = int(b.replace('\n', ''))
            # TODO: Make it fool-resilient
            print(self.__enter_p)
            p = sys.stdin.read()
            p = int(p.replace('\n', ''))

            print('Computing. Please wait...')
            result = Handler.handle_small_numbers(a, b, operation_choice, p)

            if result is not None:
                print('\nResult = ' + str(result))
            else:
                print('\nError while computing. Try once again.')

        else:
            print('Operation ' + operation_choice + 'is wrong. ' + self.__enter_operation)

    # Operate on the large numbers
    def large_numbers(self):
        print(self.__line + '\n' + self.__space + 'Great integer modulo calclulator\n' + self.__line + '\n\n')
        print(self.__enter_operation)
        operation_choice = sys.stdin.read()
        operation_choice = operation_choice.replace('\n', '')

        if self.__operations.__contains__(operation_choice):
            print('Operation: a ' + operation_choice + ' b mod p')
            print('How many bits should number p have?')
            p_bits = sys.stdin.read()
            p_bits = p_bits.replace('\n', '')
            p_bits_num = int(p_bits)
            p = Handler.generate_big_numbers(p_bits_num)

            print('How many bits should number a have?')
            a_bits = sys.stdin.read()
            a_bits = a_bits.replace('\n', '')
            a_bits_num = int(a_bits)
            a = Handler.generate_big_numbers(a_bits_num)

            print('How many bits should number b have?')
            b_bits = sys.stdin.read()
            b_bits = b_bits.replace('\n', '')
            b_bits_num = int(b_bits)
            b = Handler.generate_big_numbers(b_bits_num)

            print('a = ' + str(a))
            print('b = ' + str(b))
            print('p = ' + str(p))

            print('\nComputing. Please wait...')
            result = Handler.handle_large_numbers(a, b, operation_choice, p)

            if result is not None:
                print('\nResult = ' + str(result))
            else:
                print('\nError while computing. Try once again.')

        else:
            print('Operation ' + operation_choice + 'is wrong. ' + self.__enter_operation)



