import ocr
from screenshot import get_pic 
from slice_and_dice import separate_letters
import calc_stat
from dmg_calc import calc_dmg, get_types

###used to quickly get all the data u might need :_)
def fetch_pokemon_data():
    enemy_name_region = (356,182,368,41)
    enemy_lvl_region = (773,182,55,42)
    player_name_region = (1090,531,370,41)
    player_lvl_region = (1507,531,56,42) 

    enemy_name = ocr.get_text(separate_letters(get_pic(enemy_name_region)),"name")
    player_name = ocr.get_text(separate_letters(get_pic(player_name_region)),"name")
    enemy_lvl = ocr.get_text(separate_letters(get_pic(enemy_lvl_region)),"lvl")
    player_lvl = ocr.get_text(separate_letters(get_pic(player_lvl_region)),"lvl")

    return(player_name,player_lvl,enemy_name,enemy_lvl)

def fetch_move_data():
    move_region_1 = (323,809,400,42)
    move_region_2 = (750,809,400,42)
    move_region_3 = (326,905,400,42)
    move_region_4 = (740,905,400,42)

    move1 = ocr.get_text(separate_letters(get_pic(move_region_1)),"move")
    move2 = ocr.get_text(separate_letters(get_pic(move_region_2)),"move")
    move3 = ocr.get_text(separate_letters(get_pic(move_region_3)),"move")
    move4 = ocr.get_text(separate_letters(get_pic(move_region_4)),"move")
    return([move1,move2,move3,move4])


def create_move_list(player_name,enemy_name,moves_list,player_lvl,enemy_lvl):
    moves_and_dmg = []
    type1player,type2player,type1enemy,type2enemy = get_types(player_name,enemy_name)
    for move in moves_list:
        moves_and_dmg.append(move)
        moves_and_dmg.append(calc_dmg(move,player_name,enemy_name,player_lvl,enemy_lvl,type1player,type2player,type1enemy,type2enemy))
    return moves_and_dmg