from pprint import pprint
from sys import argv
import sys
import threading

'''Get commandline args'''
argument = int()
try:
    argument = int(argv[1])
except (ValueError, TypeError) as error:
    print(error, "Cannot convert arg to int")
    sys.exit()

'''Generated and state list setup'''
solved_map = {}

def collatz_function(number):
    '''Collatz Conjecture Method'''
    print(f"Thread working on number at index {number}")
    number_to_map = number
    steps = 0
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number *= 3
            number += 1
        steps += 1
    solved_map[number_to_map] = str(steps) + " steps"
    print(f"Thread ended working on number at index {number}")

if __name__ == "__main__":
    
    thread = threading.Thread(target=collatz_function(argument), args=(argument))
    thread.start()
    print("work done")
    pprint(solved_map)


