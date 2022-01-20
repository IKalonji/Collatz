from sys import argv
import sys
import threading

number_find = int()
try:
    number_find = int(argv[1])
except (ValueError, TypeError) as error:
    print(error, "Cannot convert to an Int")
    sys.exit()

generated_list_to_solve = [i for i in range(1,number_find+1)]
list_on_number_state = [0 for i in range(number_find)]

def collatz_function(number, index):
    print(f"Thread working on number {number} index {index}")
    steps = 0
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number *= 3
            number += 1
        steps += 1
    list_on_number_state[index] = steps
    print(f"Thread ended working on number {number} index {index}")



if __name__ == "__main__":
    print("Generated list to solve: ", generated_list_to_solve)
    print("State list to solve: ", list_on_number_state)
    while 0 in list_on_number_state[1:]:
        index_to_solve = list_on_number_state.index(0)
        list_on_number_state[index_to_solve] = -1
        number_to_solve = generated_list_to_solve[index_to_solve]
        thread = threading.Thread(target=collatz_function, args=(number_to_solve, index_to_solve))
        thread.start()
    else:
        print("work done")
        print(generated_list_to_solve)
        print(list_on_number_state)


