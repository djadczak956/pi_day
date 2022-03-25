# This program compares the digits of pi and e up to a length that the user specifies
# This program also plots the distribution of digits

# Imports
from venv import create
import matplotlib.pyplot as plt
import numpy as np

# Prints out the introductory text
def intro():
    print("Hello! This program will compare the digits of the two irrational numbers:")
    print("pi (3.14...) and e (2.71...). You will also be given the option to compare")
    print("the distribution of digits with a bar graph. Enjoy.\n\n")

# Reads as many digits of the file as you specify
def read_file(file_name, length):
    with open(file_name) as file:
        pi_sample = file.read(length)
        return pi_sample   

# Asks for how many digits of a number that you will analyze
def get_length():
    length = int(input("Enter how many digits you want to analyze from pi and e (from 1 to 1 million): "))
    while length <= 1 or length > 1_000_000:
        print("Invalid number. Please try again (2 to 1 million)!")
        length = int(input("Enter how many digits you want to analyze (from 1 to 1 million): "))
    return length

def assign_digits(num_file, name, length):
    numbers = [0] * 10  # Create an array from index 0-9
    for digit in num_file:
        numbers[int(digit)] += 1
    print(name + ":")
    for i in range(10):
        print(str(i) + ": " + str(numbers[i]))
    print()
    return numbers

# https://www.geeksforgeeks.org/bar-plot-in-matplotlib/
def create_graph(pi_list, e_list, length):
    bar_width = 0.2
    fig = plt.subplots(figsize=(12, 8))
    #ax = fig.add_axes([0, 0, 1, 1])

    # Positioning for the bars
    bar1 = np.arange(len(pi_list))  # The x position of first bar
    bar2 = [i + bar_width for i in bar1]    # Slightly shifted second bar

    # Making the bar plot
    plt.bar(bar1, pi_list, color="r", width=bar_width, edgecolor="grey", label="pi")    
    plt.bar(bar2, e_list, color="b", width=bar_width, edgecolor="grey", label="e")    

    # Labeling / Xticks
    plt.title("What is the distribution of digits in " + str(length) + " digits of pi and e?")
    plt.xlabel("What digit?", fontweight="bold", fontsize=15)
    plt.ylabel("How many of a digit?", fontweight="bold", fontsize=15)
    plt.xticks([r + bar_width - 0.1 for r in range(len(pi_list))], [i for i in range(10)])

    # Finish the graph
    plt.legend()
    plt.show()


# TODO: Use a bar plot to compare the 2 irrational numbers
# ---------------- MAIN ------------------
intro()
length = get_length()
pi = assign_digits(read_file("pi.txt", length), "pi", length)   # Prints and assigns pi digits
e = assign_digits(read_file("e.txt", length), "e", length)      # Prints and assigns e digits
create_graph(pi, e, length)
