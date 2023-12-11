def CheckValidation(num):
    """
    check if the given number is valid
    :param num: an input from a user
    :return: true if valid. otherwise return false.
    """
    if not num.isdigit():
        print("Invalid input - not a digit")
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
    while num != "0" and not is_num:
        print("Invalid input - not a number")
        num = input("Please enter a number: ")
        is_num = is_number(num)
    return is_num

def Call_Math_func(num1, num2, choice):
    """

    :param num1: first num
    :param num2:  second num
    :param choice: the chosen mathematical operation
    :return: the result of the operation
    """
    result = 0
    match choice:
        case "1":
            result = Add(num1, num2)
        case "2":
             result = Sub(num1, num2)
        case "3":
             result = Mul(num1, num2)
        case "4":
             result = Div(num1, num2)
        case "5":
             result = Pow(num1, num2)
    return result

def Add(num1, num2):
    return num1 + num2
def Sub(num1, num2):
    return num1 - num2
def Mul(num1, num2):
    return num1 * num2
def Div(num1, num2):
    try:
        return num1 / num2
    except:
        print("Division by zero")
def Pow(num1, num2):
    return num1 ** num2
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
        num = input("Please choose an option: ")
        check = CheckValidation(num)
    #get 2 numbers from user
    num1 = GetValidNum()
    num2 = GetValidNum()
    #get result
    result = Call_Math_func(num1,num2,num)
    print(f"The result is: {result} ")

if __name__ == '__main__':
    main()
