# This program compares the digits of pi and e up to a length that the user specifies
# This program also plots the distribution of digits

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
    while length <= 0 or length > 1_000_000:
        print("Invalid number. Please try again (1 to 1 million)!")
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

# TODO: Use a bar plot to compare the 2 irrational numbers
# ---------------- MAIN ------------------
intro()
length = get_length()
assign_digits(read_file("pi.txt", length), "pi", length)
assign_digits(read_file("e.txt", length), "e", length)
