#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int points[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
int score(string answer);
int main(void)
{
    // get players input
    string p1 = get_string("Player 1: ");
    string p2 = get_string("Player 2: ");

    int score1 = score(p1);
    int score2 = score(p2);

    if (score1 > score2)
    {
        printf("Player 1 Wins\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins\n");
    }
    else
    {
        printf("Tie\n");
    }
}

int score(string answer)
{
    int score = 0;

    for (int i = 0; i < strlen(answer); i++)
    {
        // increments the score by the number of points if it is upper
        if (isupper(answer[i]))
        {
            score += points[answer[i] - 'A'];
        }
        // increments score by points if it is lower
        else if (islower(answer[i]))
        {
            score += points[answer[i] - 'a'];
        }
    }
    return score;
}
