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
generated_list_to_solve = [i for i in range(1,argument+1)]
list_on_number_state = [0 for i in range(argument)]
solved_map = {}

def collatz_function(number, index):
    '''Collatz Conjecture Method'''
    print(f"Thread working on number at index {index}")
    steps = 0
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number *= 3
            number += 1
        steps += 1
    list_on_number_state[index] = steps
    solved_map[index+1] = str(steps) + " steps"
    print(f"Thread ended working on number at index {index}")

if __name__ == "__main__":
    while 0 in list_on_number_state[1:]:
        index_to_solve = list_on_number_state.index(0)
        list_on_number_state[index_to_solve] = -1
        number_to_solve = generated_list_to_solve[index_to_solve]
        thread = threading.Thread(target=collatz_function, args=(number_to_solve, index_to_solve))
        thread.start()
    else:
        while -1 in list_on_number_state:
            #wait for all threads to finish
            continue
        else:
            print("work done")
            pprint(solved_map)


