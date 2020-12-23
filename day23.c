#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static void part1(const char *);
static void part2(const char *);

static int *make_cups(const char *, int, int *);
static void play_game(int *, int, int *);

int
main(void)
{
    const char *input = "614752839";

    part1(input);

    part2(input);

    return 0;
}

void
part1(const char *input)
{
    int current;
    int size = strlen(input);
    int *cups = make_cups(input, size, &current);

    for (int i = 0; i < 100; i++)
        play_game(cups, size, &current);

    for (int label = cups[0]; label; label = cups[label])
        putchar(label + '1');

    putchar('\n');

    free(cups);
}

void
part2(const char *input)
{
    int current;
    int size = 1000000;
    int *cups = make_cups(input, size, &current);

    for (int i = 0; i < 10000000; i++)
        play_game(cups, size, &current);

    int first = cups[0];
    int second = cups[first];

    long result = (long) (first + 1) * (second + 1);

    printf("%ld\n", result);

    free(cups);
}

int *
make_cups(const char *input, int size, int *pcurrent)
{
    int *cups = malloc(size * sizeof *cups);
    int front = input[0] - '1';
    int label = front;
    int index = 1;

    for (; input[index]; index++)
        label = cups[label] = input[index] - '1';

    for (; index < size; index++)
        label = cups[label] = index;

    cups[label] = front;
    *pcurrent = front;

    return cups;
}

void
play_game(int *cups, int size, int *pcurrent)
{
    int current = *pcurrent;
    int first_removed = cups[current];
    int second_removed = cups[first_removed];
    int third_removed = cups[second_removed];
    int post_third_removed = cups[third_removed];

    int destination = current;
    do
        destination = (destination ? destination : size) - 1;
    while (destination == first_removed || destination == second_removed || destination == third_removed);

    int post_destination = cups[destination];

    cups[current] = post_third_removed;
    cups[third_removed] = post_destination;
    cups[destination] = first_removed;

    *pcurrent = post_third_removed;
}
