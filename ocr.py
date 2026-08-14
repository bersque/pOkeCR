import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from rapidfuzz import fuzz, process
import ast
import make_lists_from_db
###used for reading data off off your screen and converting it to strings of text :) 

letters_as_arrs = np.load('letters_dictionary.npy',allow_pickle='TRUE').item() ### loads letters from file
nums_as_arrs = np.load('numbers_dictionary.npy',allow_pickle='TRUE').item()
pokemon_names = make_lists_from_db.names_pkmn()
move_names = make_lists_from_db.names_moves()
print(letters_as_arrs)

def recognize_name(list_of_letters,application): ###hamming metric, seeks "most similair" letter to the one supplied
    name = []
    if application == 'lvl':
        reference = nums_as_arrs
    else:
        reference = letters_as_arrs

    for letter in list_of_letters: 
        a = letter
        best_diff = float('inf')
        best_letter = None

        for slowo in reference:#we check hamming dist for every possible word
            b = np.array(ast.literal_eval(slowo))
            h = min(a.shape[0], b.shape[0]) 
            w = min(a.shape[1], b.shape[1]) ###we compare the common part bc the arrays are probably different lengths

            diff = np.sum(a[:h, :w] != b[:h, :w]) + (h-max(a.shape[0], b.shape[0])) + (w - max(a.shape[1], b.shape[1])) # distance + punishment for different length

            if diff < best_diff:
                best_diff = diff
                best_letter = reference[slowo]

        if best_diff < 500:#we save the best one (as long as its not absurd)
            name.append(best_letter)
    to_ret = ''.join(name)
    if to_ret == '00': ##bugfix for lvl100 pokemon
        return 100
    else:
        return to_ret

def get_text(letters,application): ### we compare with fuzzy logic to get the pokemon name, useful when we miss one or more letters :) 
    reference = []
    if application == "name":
        reference = pokemon_names
    elif application == "move":
        reference = move_names
    elif application == 'lvl':
            return int(recognize_name(letters,application))
    print(recognize_name(letters,application))
    match = process.extractOne(recognize_name(letters,application),reference, scorer=fuzz.WRatio, processor=str.upper)
    text = match[0]
    return(text)
