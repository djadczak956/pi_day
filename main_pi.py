# This method reads as many digits of the file as you specify
def read_file(file_name, length):
    with open(file_name) as file:
        pi_sample = file.read(length)
        return pi_sample   

def get_length():
    length = int(input("Enter how many digits you want to analyze (from 1 to 1 million): "))
    while length <= 0 or length > 1_000_000:
        print("Invalid number. Please try again!")
        length = int(input("Enter how many digits you want to analyze (from 1 to 1 million): "))
    return length

def assign_digits(pi_digits, length):
    numbers = {
        '0': 0,
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0
    }
    pi_numbers = read_file('pi.txt', length)
    print(pi_numbers)
    for digit in pi_numbers:
        numbers[digit] += 1
    print(numbers)
# TODO: Turn dictionary into array great
# TODO: Use a bar plot to show the distribution
# ---------------- MAIN ------------------
length = get_length()
input_file = read_file("pi.txt", length)
assign_digits(input_file, length)

