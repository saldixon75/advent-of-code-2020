import numpy;
import sys;
import copy;
import re;


with open("input.txt") as f:
    lines = f.read();
    
decks = lines.split('\n\n');    

player_1_deck = decks[0].split('\n');
player_1_deck.pop(0);
player_1_deck = list(map(int, player_1_deck));
player_2_deck = decks[1].split('\n');
player_2_deck.pop(0);
player_2_deck.remove('');
player_2_deck = list(map(int, player_2_deck));

print('player_1_deck' + str(player_1_deck));
print('player_2_deck' + str(player_2_deck));
number_of_cards = len(player_1_deck) + len(player_2_deck);

while (len(player_1_deck) > 0 and len(player_1_deck) < number_of_cards):
    player_1_card = player_1_deck.pop(0);
    player_2_card = player_2_deck.pop(0);
    if (player_1_card > player_2_card):
        player_1_deck.append(player_1_card);
        player_1_deck.append(player_2_card);
    else:
        player_2_deck.append(player_2_card);
        player_2_deck.append(player_1_card);


print('player 1 deck = ' + str(player_1_deck));
print('player 2 deck = ' + str(player_2_deck));

winning_deck = player_1_deck;
if len(player_1_deck) == 0:
    winning_deck = player_2_deck;

running_total = 0;
winning_deck.reverse();
for i in range(1,len(winning_deck)+1):
    print('i=' + str(i) + ' winning_deck[i-1]=' + str(winning_deck[i-1]));
    running_total += i*winning_deck[i-1];

print('result = ' + str(running_total));    

#  it is not 9458
