
"""""
Edited by:
Amr Khaled Ahmed


this program is for building a Binary calculator that can do addition, subtraction and one's complement
and two's complement conversions without including libraries or build in functions.
"""""


def validate_binary(binary):


    """
    validation function:
    the following function will check whether the number is binary or not.
    Which will be binary if the entry number includes only 1 and 0.
    """
    for digit in binary:
        """This condition will check if the binary number includes any values other than 0 and 1 ."""
        if digit != '0' and digit != '1':
            return False
    return True


def insert_binary_number(i):
    """
    inserting function:
    The next function will take the binary number and validate it with the validation function.
    """
    count = ""
    if i == 1:
        count = "the first"
    elif i == 2:
        count = "the second"
    while True:
        binary_test = input(f"Please insert {count} binary number: ")
        if validate_binary(binary_test):
            return binary_test
        else:
            """after validation if the in put is not binary, will output this message. """
            print()
            print("Please insert a valid binary number.")


def menu_1():
    """
    menu_1 function.
    menu_1 to take the choice to start or continue the program or stop the program.
    """
    print()
    print("** Binary Calculator **")
    print()
    print("Please select an option: ")
    print("A) Insert new numbers")
    print("B) Exit")


def menu_2():
    """
    menu_2 function.
    menu_2 to take the operation.
    """
    print()
    print("** Please, select the operation **")
    print("A) Compute one's complement")
    print("B) Compute two's complement")
    print("C) Addition '+'")
    print("D) Subtraction '-'")


def ones_complement_function(binary1):
    """This function will instead the whole binary number with its opposite: 1 by 0 and 0 by 1 by join"""
    binary1 = ''.join('1' if bit == '0' else '0' for bit in binary1)
    return binary1


def twos_complement_function(binary1):
    max_len=len(binary1)
    """
    This function will compute the two's complement by two steps:
    first step: Compute one's complement
    second step: add 1 to the one's complement
    """
    # Step_1: convert the binary1 to one's complement.
    binary1 = ''.join('1' if bit == '0' else '0' for bit in binary1)

    # step_2: here I will add 1 to the one's complement.
    carry = 1   # which I will add it.it has to be an integer .
    binary1 = binary1.zfill(len(binary1))   # Refill all index of binary1 by zeros.
    for i in range(len(binary1) - 1, -1, -1):   # loop on index of binary1 by backwards.
        total = int(binary1[i]) + carry     # Add one to the index if there.
        binary1 = binary1[:i] + str(total % 2) + binary1[i + 1:]    # Addition the value as a string.
        carry = total // 2  # To delete numbers after the decimal point without rounding them to ciel or floor.
    if len(binary1) > max_len:  # To chick when I have to remove EAC.
        return binary1[1:len(binary1)]
    else:
        return binary1


def binary_addition(binary1, binary2):
    result = ""
    carry = 0

    # make sure both binary numbers are of the same length
    max_len = max(len(binary1), len(binary2))
    binary1 = binary1.zfill(max_len)
    binary2 = binary2.zfill(max_len)

    for i in range(max_len-1, -1, -1):
        bit1 = int(binary1[i])  # make the bit integer.
        bit2 = int(binary2[i])

        sum_bit = carry     # store the sum in carry.
        sum_bit += bit1     # addition bit of binary 1 to the sum.
        sum_bit += bit2     # addition bit of binary 2 to the sum.

        carry = 1 if sum_bit >= 2 else 0
        sum_bit = sum_bit % 2   # convert the sum into 0 or 1.

        result = str(sum_bit) + result  # convert the sum into string and addition to the result.

    if carry == 1:  # at end of loop if there is one overflow from addition add it ti the result.
        result = '1' + result

    return result


def binary_subtraction(binary1, binary2):
    """ This function subtracts binary numbers by making the second number a two's complement,
    then adding the two numbers together and removing the EAC."""
    max_len = max(len(binary1), len(binary2))    # to determine which size is largest

    #twos_complement=twos_complement_function(binary2)

    if len(binary1) == len(binary2):
        twos_complement = twos_complement_function(binary2)
        result_of_subtraction=binary_addition(binary1, twos_complement)
        if len(result_of_subtraction) > max_len:    # To chick when I have to remove EAC.
            return result_of_subtraction[1:len(result_of_subtraction)]  # to remove the EAC.
        else: return result_of_subtraction

    elif len(binary1) > len(binary2):     # if size binary1 is largest.
        binary2 = binary2.zfill(max_len)    # complete the lake of binary2 with 0 to be suitable for two's complement .
        print(binary2)
        twos_complement = twos_complement_function(binary2)     # compute the two's complement of binary2.
        result_of_subtraction = binary_addition(binary1, twos_complement)   # send the two's complement of binary2 and binary 1 to addition.
        if len(result_of_subtraction) > max_len:    # To chick when I have to remove EAC.
            if result_of_subtraction[0] == '1': # if the first index (the EAC) is one then remove it.
                return result_of_subtraction[1:len(result_of_subtraction)]  # to remove the EAC.
            else:   # else if 0 do not do anything.
                return result_of_subtraction
        else: return result_of_subtraction

    elif len(binary1) < len(binary2):   # if size of binary2 is largest.
        twos_complement = twos_complement_function(binary2) # compute the two's complement of binary2.
        result_of_subtraction=binary_addition(binary1, twos_complement) # send the two's complement of binary2 and binary 1 to addition.
        if len(result_of_subtraction) > max_len:    # To chick when I have to remove EAC.
            return result_of_subtraction[1:len(result_of_subtraction)]  # to remove the EAC.
        else: return result_of_subtraction


while True:
    print()
    print("****** Menu_1 ******")
    menu_1()
    # here I will make sure that the program is running if the user input a small letter.
    choice = input("Please, choose an option: ").upper()

    if choice == 'A':
        binary1 = insert_binary_number(1)  # taking overall.
        print()
        print("****** Menu_2 ******")
        menu_2()
        choice = input("Please, choose an option: ").upper()
        # here I will make sure that the program is running if the user input a small letter.
        if choice == 'A':
            ones_complement = ones_complement_function(binary1)
            print(f"one's complement of {binary1} is: ", ones_complement)


        elif choice == 'B':

            twos_complement = twos_complement_function(binary1)

            # Here I will send a binary1 to the function, which will convert it to two's complement.

            print(f"The two's complement of {binary1} is {twos_complement}")

        elif choice == 'C':

            binary2 = insert_binary_number(2)   # taking only when subtraction or addition operations.
            result=binary_addition(binary1,binary2)
            print(f"{binary1} + {binary2} = {result}")
        elif choice == 'D':

            binary2 = insert_binary_number(2)  # taking only when subtraction or addition operations.
            result=binary_subtraction(binary1,binary2)
            print(f"{binary1} - {binary2} = {result}")
        else:
            print("*** Please, select a valid choice. ***")   # print when user write any choice_string other than A,B,C,and D.
    elif choice == 'B':
        print("***** Thank you for using our program. *****")   # print when user select B at first menu.
        break   # break the true loop when select B.
    else:
        print()
        print("*** Please, select a valid choice.***")  # print when the user write anything other than A and B.
