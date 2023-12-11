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

def is_float(num):
    """
    check if the given number is a float
    :param num: a given input from  user
    :return: true if float. otherwise return false.
    """
    try:
        float(num)
        return True
    except ValueError:
        return False

def is_int(num):
    """
    check if the given number is an int
    :param num: a given input from  user
    :return: true if int. otherwise return false.
    """
    try:
        int(num)
        return True
    except ValueError:
        return False

def is_number(num):
    """
    check if a string contains a number
    :param num: a string from a user
    :return: the num if a number. otherwise return false.
    """
    if(is_float(num)):
        return float(num)
    elif(is_int(num)):
        return int(num)
    return False

def GetValidNum():
    """
    get an input from user and check its validation
    :return: a number
    """
    num = input("Please enter a number: ")
    #check if number
    is_num = is_number(num)
    while not is_num:
        print("Invalid input - not a number")
        num = input("Please enter a number: ")
        is_num = is_number(num)
    return is_num


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
    # get 2 numbers from user
    num1 = GetValidNum()
    num2 = GetValidNum()


if __name__ == '__main__':
    main()
