def activity01(num1):
    """Determine if an input number is Even or Odd"""

    res = num1 % 2 == 0
    if res:
        return "Even"
    return "Odd"


def activity02(iv_one, iv_two):
    """Return the sum of two input values"""
    return iv_one + iv_two


def activity03(num_list):
    """Given a list of integers, count how many are even"""
    count = 0
    for num in num_list:
        if activity01(num) == "Even":
            count += 1

    return count


def activity04(input_string):
    """Return the input string, backward"""
    return input_string [::-1]
