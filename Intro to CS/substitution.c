#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

void subs(char *, char *);

int main(int argc, char *argv[])
{
    // validates key
    if (argc != 2)
    {
        printf("Only enter key with no spaces.\n");
        return 1;
    }
    if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 letters.\n");
        return 1;
    }
    for (int i = 0; i < strlen(argv[1]); i++)
    {

        if (isalpha(argv[1][i]) == 0)
        {
            printf("Key must only contain alphabetic letters. \n");
            return 1;
        }
        for (int r = i + 1; r < strlen(argv[1]); r++)
        {
            if (toupper(argv[1][r]) == toupper(argv[1][i]))
            {
                printf("Key must only contain one of each alphabetic letter. \n");
                return 1;
            }
        }
    }
    string text = get_string("Plaintext: ");
    subs(text, argv[1]);
}

void subs(char *t, char *k)
{
    printf("ciphertext: ");

    for (int i = 0; i < strlen(t); i++)
    {
        if (isalpha(t[i]) != 0)
        {
            if (isupper(t[i]) != 0)
            {
                int n = t[i] - 'A';
                printf("%c", toupper(k[n]));
            }
            else
            {
                int n = t[i] - 'a';
                printf("%c", tolower(k[n]));
            }
        }
        else
        {
            printf("%c", t[i]);
        }
    }
    printf("\n");
}
