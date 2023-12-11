def CheckValidation(num):
    """
    check if the given number is valid
    :param num: an input from a user
    :return: true if valid. otherwise return false.
    """
    if not num.isdigit():
        print("Invalid input - not a natural number")
        return False
    elif int(num) < 1 or int(num) > 5:
        print("Invalid input - number out of range")
        return False
    return True


def main():
    # present menu instructions
    print("Hello there!")
    print("1 - Addition\n2 - Subtraction")
    print("3 - Multiplication\n4 - division\n5 - Power")
    # get an option from user
    num = input("Please choose an option:")
    # check the validation of the input
    check = CheckValidation(num)
    while not check:
        num = input("Please choose an option:")
        check = CheckValidation(num)


if __name__ == '__main__':
    main()
