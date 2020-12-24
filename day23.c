#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct cups {
    int count;
    int current;
    int after[];
};

static void part1(const char *);
static void part2(const char *);

static struct cups *make_cups(const char *, int);
static void play_game(struct cups *);

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
    struct cups *cup = make_cups(input, strlen(input));

    for (int i = 0; i < 100; i++)
        play_game(cup);

    for (int label = cup->after[0]; label; label = cup->after[label])
        putchar(label + '1');

    putchar('\n');

    free(cup);
}

void
part2(const char *input)
{
    struct cups *cup = make_cups(input, 1000000);

    for (int i = 0; i < 10000000; i++)
        play_game(cup);

    int first = cup->after[0];
    int second = cup->after[first];

    long result = (long) (first + 1) * (second + 1);

    printf("%ld\n", result);

    free(cup);
}

struct cups *
make_cups(const char *input, int count)
{
    struct cups *cup = malloc(sizeof *cup + (count * sizeof *cup->after));

    int current = input[0] - '1';
    int label = current;
    int index = 1;

    cup->count = count;
    cup->current = current;

    for (; input[index]; index++)
        label = cup->after[label] = input[index] - '1';

    for (; index < count; index++)
        label = cup->after[label] = index;

    cup->after[label] = current;

    return cup;
}

void
play_game(struct cups *cup)
{
    int count = cup->count;
    int current = cup->current;
    int first_removed = cup->after[current];
    int second_removed = cup->after[first_removed];
    int third_removed = cup->after[second_removed];

    int destination = current;
    do
        destination = (destination ? destination : count) - 1;
    while (destination == first_removed || destination == second_removed || destination == third_removed);

    cup->after[current] = cup->after[third_removed];
    cup->after[third_removed] = cup->after[destination];
    cup->after[destination] = first_removed;

    cup->current = cup->after[current];
}
