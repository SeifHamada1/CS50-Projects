from cs50 import get_int


def main():
    digit1 = 0
    digit2 = 0
    num_digits = 0
    sum1 = 0
    sum2 = 0
    number = get_int("Number: ")

    while number > 0:
        digit2 = digit1
        digit1 = number % 10

        if num_digits % 2 == 0:
            sum2 += digit1
        else:
            multiple = 2 * digit1
            sum1 += (multiple // 10) + (multiple % 10)

        number //= 10
        num_digits += 1

    is_valid = (sum2 + sum1) % 10 == 0
    first_two_digits = (digit1 * 10) + digit2

    if digit1 == 4 and num_digits >= 13 and num_digits <= 16 and is_valid:
        print("VISA\n")
    elif first_two_digits >= 51 and first_two_digits <= 55 and num_digits == 16 and is_valid:
        print("MASTERCARD\n")
    elif (first_two_digits == 34 or first_two_digits == 37) and num_digits == 15 and is_valid:
        print("AMEX\n")
    else:
        print("INVALID\n")


main()
