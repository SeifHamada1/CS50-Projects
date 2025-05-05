// where L is the average number of letters per 100 words in the text, and S is the average number
// of sentences per 100 words in the text. index = 0.0588 * L - 0.296 * S - 15.8
#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int nsentences(string text);
int nwords(string text);
int nletters(string text);
int main(void)
{
    string text = get_string("Text: ");
    int letters = nletters(text);
    int words = nwords(text);
    int sentences = nsentences(text);

    float l = ((float) nletters(text) / (float) nwords(text) * 100);
    float s = ((float) nsentences(text) / (float) nwords(text) * 100);
    float index = round(0.0588 * l - 0.296 * s - 15.8);

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", (int) index);
    }
}

int nletters(string text)
{
    int nletters = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            nletters += 1;
        }
    }
    return nletters;
}

int nwords(string text)
{
    int nwords = 1;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isblank(text[i]))
        {
            nwords += 1;
        }
    }
    return nwords;
}

int nsentences(string text)
{
    int nsentences = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            nsentences += 1;
        }
    }
    return nsentences;
}
