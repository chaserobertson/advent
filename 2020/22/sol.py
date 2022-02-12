import pathlib
import queue

in_file = pathlib.Path.cwd().joinpath('22', 'input.txt')

with open(in_file) as input:
    lines = input.readlines()


class Player:
    def __init__(self, id):
        self.id = int(id)
        self.deck = queue.SimpleQueue()

    def __str__(self):
        output = 'Player ' + str(self.id) + '\'s deck:'
        if self.deck.empty():
            return output
        newQueue = queue.SimpleQueue()
        while not self.deck.empty():
            card = self.deck.get()
            output += ' ' + str(card) + ','
            newQueue.put(card)
        self.deck = newQueue
        return output[:-1]

    def score(self):
        score = 0
        stack = queue.LifoQueue()
        while not self.deck.empty():
            stack.put(self.deck.get())

        multiplier = 1
        while not stack.empty():
            score += multiplier * stack.get()
            multiplier += 1
        return score

    def topCard(self):
        return self.deck.get()

    def insertBottomCard(self, card):
        self.deck.put(int(card))

    def insertBottomCards(self, cards):
        for card in cards:
            self.insertBottomCard(card)


print('part 1')
player_id = 1
players = []
for line in lines:
    if line == '\n':
        continue
    elif line[:6] == 'Player':
        players.append(Player(player_id))
        player_id += 1
    else:
        players[-1].insertBottomCard(line.strip())

print('Initial Hands: ')
for player in players:
    print(player)

round = 1
while not sum([player.deck.empty() for player in players]):
    print('-- Round %d --' % round)
    for player in players:
        print(player)
    cards = [player.topCard() for player in players]
    for i in range(0, len(cards)):
        print('Player {0} plays: {1}'.format(i + 1, cards[i]))
    winning_card = max(cards)
    winner = cards.index(winning_card)
    print('Player {0} wins the round!'.format(winner + 1))

    cards.sort()
    cards.reverse()
    players[winner].insertBottomCards(cards)
    round += 1
    print()

print()
print('== Post-game results ==')
for player in players:
    print(player)
    print(player.score())
print('part 2')
