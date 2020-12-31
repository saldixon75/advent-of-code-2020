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

print('original player_1_deck' + str(player_1_deck));
print('original player_2_deck' + str(player_2_deck));



# return the winner
def play_game(player_1_deck,player_2_deck):
    hands = {};
    round = 0;

    number_of_cards = len(player_1_deck) + len(player_2_deck);
    # print('Number of cards = ' + str(number_of_cards));

    while (len(player_1_deck) > 0 and len(player_1_deck) < number_of_cards):
        round += 1;
        # print('Round ' + str(round));
        # print('player_1_deck = ' + str(player_1_deck) + ' player_2_deck = ' + str(player_2_deck));
        #  record the hand status
        hand = get_hands(player_1_deck, player_2_deck);
        if hand in hands:
            #  we've been here before.  Immediately award a win to player 1 
            # print('Been here before . Player 1 wins this game!!');
            return 'player_1';
        hands[hand] = 1;    
        # play another round
        (player_1_deck,player_2_deck) = play_round(player_1_deck, player_2_deck);
    if len(player_1_deck) > 0:
        return 'player_1';
    else:
        return 'player_2';


def play_round(player_1_deck, player_2_deck):
    player_1_card = player_1_deck.pop(0);
    player_2_card = player_2_deck.pop(0);
    # print('Playing round.  player 1 plays ' + str(player_1_card) + ', player 2 plays ' + str(player_2_card));
    if (player_1_card > len(player_1_deck) or player_2_card > len(player_2_deck)):
        #  not enough to recurse, so do a regular play
        # print('Regular play...');
        if (player_1_card > player_2_card):
            player_1_deck.append(player_1_card);
            player_1_deck.append(player_2_card);
            # print('player_1 wins this round');
        else:
            player_2_deck.append(player_2_card);
            player_2_deck.append(player_1_card);
            # print('player_2 wins this round innit');
        return (player_1_deck,player_2_deck);

    #  do the recursion ... todo change this
    # start a new sub-game...
    # print('Doing a recursion...');
    player_1_subdeck = player_1_deck[:player_1_card];
    player_2_subdeck = player_2_deck[:player_2_card];
    winner = play_game(player_1_subdeck,player_2_subdeck);
    if (winner == 'player_1'):
        player_1_deck.append(player_1_card);
        player_1_deck.append(player_2_card);
        # print('player_1 wins this round');
    else:
        player_2_deck.append(player_2_card);
        player_2_deck.append(player_1_card);
        # print('player_2 wins this round ho');

    return (player_1_deck,player_2_deck);

def get_hands(player_1_deck, player_2_deck):
    return ','.join(map(str,list('p1') + player_1_deck + list('p2') + player_2_deck));
    # return ','.join(map(str,player_1_deck + player_2_deck));

def get_total(winning_deck):
    running_total = 0;
    winning_deck.reverse();
    for i in range(1,len(winning_deck)+1):
        # print('i=' + str(i) + ' winning_deck[i-1]=' + str(winning_deck[i-1]));
        running_total += i*winning_deck[i-1];
    return running_total;


winner = play_game(player_1_deck,player_2_deck); 
if winner == 'player_1':
    winning_deck = player_1_deck;
else:    
    winning_deck = player_2_deck;

print('winning deck = ' + str(winning_deck));
total = get_total(winning_deck);
print('result = ' + str(total)); 






 


