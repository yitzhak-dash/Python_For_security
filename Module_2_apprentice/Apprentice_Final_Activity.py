import operator

saved_string = ""


def remove_letter():  # Remove a selected letter from a string
    print('Remote Letter')
    base_string = str(raw_input("input string: "))
    letter_remove = str(raw_input("input letter: "))
    letter_remove = letter_remove[0]
    str_length = len(base_string)
    location = 0

    while location > str_length:
        if base_string[location] == letter_remove:
            base_string = base_string[:location] + base_string[location + 1::]
            str_length -= 1
        location += 1
    print base_string
    return


def num_compare():  # Compare 2 numbers to determine the larger
    print ("Num Compare")

    num1 = int(raw_input("first num: "))
    num2 = int(raw_input("second num: "))

    if num1 > num2:
        print num1
    elif num2 > num1:
        print num2
    else:
        print "EQUAL"

    return


def print_string():  # Print the previously stored string
    print ("Print string")
    print saved_string
    return


def calculator():  # Basic Calculator (addition, subtraction, multiplication, division)
    op_dict = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}
    num1 = int(raw_input("first num: "))
    sign = str(raw_input("Action: "))
    num2 = int(raw_input("second num: "))
    print op_dict[sign](num1, num2)
    return


def accept_and_store():  # Accept and store a string
    print("Accept and Store")
    global saved_string
    saved_string = str(raw_input("Input string: "))
    return


def main():  # menu goes here
    opt_list = [accept_and_store,
                calculator,
                print_string,
                num_compare,
                remove_letter]
    while True:
        print("Select option:"
              "\n\t1.accept_and_store"
              "\n\t2.calculator"
              "\n\t3.print_string"
              "\n\t4.num_compare"
              "\n\t5.remove_letter")
        opt_choice = int(raw_input("Your choice: "))
        opt_list[opt_choice - 1]()
    return


main()
