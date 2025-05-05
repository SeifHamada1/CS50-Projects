#include <cs50.h>
#include <stdio.h>

int main(void)
{

    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (0 >= height || height > 8);

    // left space

    for (int i = 0; i < height; i++)
    {
        for (int j = 1; j < height - i; j++)
        {
            printf(" ");
        }

        // left triangle

        for (int k = 0; k <= i; k++)
        {
            printf("#");
        }

        printf("  ");

        // right triangle(the easy one)

        for (int m = 0; m <= i; m++)
        {
            printf("#");
        }
        printf("\n");
    }
}
