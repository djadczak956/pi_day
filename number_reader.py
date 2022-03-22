# Reads as many digits of the file as you specify
def read_file(file_name, length):
    with open(file_name) as file:
        pi_sample = file.read(length)
        return pi_sample   

# Asks for how many digits of a number that you will analyze
def get_length():
    length = int(input("Enter how many digits you want to analyze (from 1 to 1 million): "))

    while length <= 0 or length > 1_000_000:
        print("Invalid number. Please try again!")
        length = int(input("Enter how many digits you want to analyze (from 1 to 1 million): "))

    return length

def assign_digits(num_file, length):
    numbers = [0 for i in range(10)]
    for digit in num_file:
        numbers[int(digit)] += 1
    print(numbers)

# TODO: Turn dictionary into array great
# TODO: Use a bar plot to show the distribution
# ---------------- MAIN ------------------
length = get_length()
assign_digits(read_file("e.txt", length), length)

