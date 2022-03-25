# This program compares the digits of pi and e up to a length that the user specifies
# This program also plots the distribution of digits with a bar graph

# Imports
from venv import create     # pipenv stuff
import matplotlib.pyplot as plt     # Use for bar graph
import numpy as np

# Prints out the introductory text
def intro():
    print("Hello! This program will compare the digits of the two irrational numbers:")
    print("pi (3.14...) and e (2.71...). You will also be given the option to compare")
    print("the distribution of digits with a bar graph. Enjoy.\n\n")

# Reads as many digits of the file as you specify
# file_name refers to the name of a file
# Returns a string of text of a specified length
def read_file(file_name, length):
    with open(file_name) as file:
        pi_sample = file.read(length)
        return pi_sample   

# Asks for how many digits of a number that you will analyze
# Returns an integer 
def get_length():
    length = -1
    
    # While the value is invalid 
    while length <= 1 or length > 1_000_000:

        # Try and except to make sure input is valid
        try:
            length = int(input("Enter how many digits you want to analyze (from 2 to 1 million): "))
        except ValueError:
            print("Invalid number. Please try again (2 to 1 million)!")
            continue

    return length

# num_file refers to a string of digits that will have its digits read and counts split into an array
# name refers to the name of the math constant
def assign_digits(num_file, name, length):
    numbers = [0] * 10  # Create an array from index 0-9
    
    # Adds to count for the corresponding digit
    # Uses an array and adds 1 to the corresponding index from 0-9
    for digit in num_file:
        numbers[int(digit)] += 1

    print(name + ":") # Prints the name of the mathematical constant
    
    # Prints out the numbers and how many times they appear in the math constant
    for i in range(10):
        print(str(i) + ": " + str(numbers[i]))

    print()     # Spacing line
    return numbers

# Uses matplotlib.pyplot to create a bar graph
# Takes in a list of digits from pi and e that can be generated with assign_digits
# Also takes in a length that can be acquired with the get_length method
def create_graph(pi_list, e_list, length):
    bar_width = 0.2
    fig = plt.subplots(figsize=(12, 8))

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


# ---------------- MAIN ------------------
intro()
length = get_length()
pi = assign_digits(read_file("pi.txt", length), "pi", length)   # Prints and assigns pi digits
e = assign_digits(read_file("e.txt", length), "e", length)      # Prints and assigns e digits
create_graph(pi, e, length)     # Creates a bar graph from the lists of digits
