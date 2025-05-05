// MASTERCARD: 16-Digit #'s, Start with: 51, 52, 53, 54, or 55
// VISA: 13 or 16-Digit #'s, Start with: 4
// AMEX: 15-Digit #'s, Star with: 34 or 37

// Luhn's Algorithm:
// 1. Multiply every other digit by 2, starting with the second number to the last
// 2. Add the sum of those digits
// 3. Add the sum of the other digits
// 4. If the total sum ends with a 0, it is valid!

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // counts visa's length
    long visa = get_long("Enter your visa number: ");
    int length = 0;
    long counter = visa;
    while (counter > 0)
    {
        counter = counter / 10;
        length++;
    }
    // eliminates any invalid options
    if (length != 13 && length != 14 && length != 15 && length != 16)
    {
        printf("INVALID\n");
        return 0;
    }
    // luhn's algo

    int sum1 = 0;
    int sum2 = 0;
    long x = visa;
    int total = 0;
    int mod1;
    int mod2;
    int double1;
    int double2;
    do
    {
        // Remove last digit and add to sum1
        mod1 = x % 10;
        x = x / 10;
        sum1 = sum1 + mod1;
        // Remove second last digit
        mod2 = x % 10;
        x = x / 10;
        // Double second last digit and add digits to sum2
        mod2 = mod2 * 2;
        double1 = mod2 % 10;
        double2 = mod2 / 10;
        sum2 = sum2 + double1 + double2;
    }
    while (x > 0);
    total = sum1 + sum2;

    if (total % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }

    long first_digits = visa;
    while (first_digits > 100)
    {
        first_digits = first_digits / 10;
    }

    // checks if it is master card

    if ((first_digits / 10 == 5) && (0 < first_digits % 10 && first_digits % 10 < 6))
    {
        printf("MASTERCARD\n");
    }

    // checks if it is amex

    else if ((first_digits / 10 == 3) && (first_digits % 10 == 4 || first_digits % 10 == 7) &&
             length == 15)
    {
        printf("AMEX\n");
    }

    // checks for visa
    else if (first_digits / 10 == 4 && (13 == length || length == 16))
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}
