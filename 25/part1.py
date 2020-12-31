import numpy;
import sys;
import copy;
import re;


# card_public_key = 5764801;
# door_public_key = 17807724;
card_public_key = 8458505;
door_public_key = 16050997;

subject_number = 7;


def do_loop(subject_number, value):
    multiplied = value * subject_number;
    rem = multiplied % 20201227;
    return rem;


card_loop_number = 0;
num = 1;
while (num != card_public_key):
    card_loop_number += 1;
    num = do_loop(subject_number,num);
    # print('loop = ' + str(card_loop_number) + ' num = ' + str(num));

print('Card loop number = ' + str(card_loop_number));

door_loop_number = 0;
num = 1;
while (num != door_public_key):
    door_loop_number += 1;
    num = do_loop(subject_number,num);
    # print('loop = ' + str(door_loop_number) + ' num = ' + str(num));

print('Door loop number = ' + str(door_loop_number));


def get_encryption_key(loop_number, public_key):
    num = 1;
    for i in range(loop_number):
        num = do_loop(public_key, num);
    return num;    


enc_key_1 = get_encryption_key(door_loop_number, card_public_key);
enc_key_2 = get_encryption_key(card_loop_number, door_public_key);

print('enc_key_1=' + str(enc_key_1) + ' enc_key_2=' + str(enc_key_2));


