import sys

player1 = []
player2 = []

next(sys.stdin) # "Player 1:"

for line in sys.stdin:
    line = line.strip()
    if not line:
        break
    player1.append(int(line))

next(sys.stdin) # "Player 2:"

for line in sys.stdin:
    line = line.strip()
    player2.append(int(line))

def score(deck):
    return sum(card * (i+1) for i, card in enumerate(reversed(deck)))

def combat(player1, player2):
    deck1 = list(player1)
    deck2 = list(player2)

    while deck1 and deck2:
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)

    return deck1, deck2

deck1, deck2 = combat(player1, player2)

print(score(deck1 or deck2))

def recursive_combat(player1, player2):
    deck1 = list(player1)
    deck2 = list(player2)
    games = set()

    while deck1 and deck2:
        game = tuple(deck1), tuple(deck2)
        if game in games:
            break
        games.add(game)

        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        if card1 <= len(deck1) and card2 <= len(deck2):
            winner, _ = recursive_combat(deck1[:card1], deck2[:card2])
        else:
            winner = card1 > card2

        if winner:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)

    return deck1, deck2

deck1, deck2 = recursive_combat(player1, player2)

print(score(deck1 or deck2))
