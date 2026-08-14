import math
import sqlite3
from calc_stat import calc_stats
###this set of functions calc damage of pokemon moves
connection = sqlite3.connect('statystyki_pkmn.db')
cursor = connection.cursor()

def get_types(pokemon_name,enemy_name):
    cursor.execute(
            f'SELECT Type1, Type2 FROM gen1 WHERE Name = ?',
            (pokemon_name,)
        )
    type1player, type2player = cursor.fetchone()

    cursor.execute(

            f'SELECT Type1, Type2 FROM gen1 WHERE Name = ?',
            (enemy_name,)
        )
    type1enemy,type2enemy = cursor.fetchone()

    return(type1player, type2player,type1enemy,type2enemy)



def calc_dmg(move,pokemon_name,enemy_name,pokemon_lvl,enemy_lvl,type1player,type2player,type1enemy,type2enemy):
    cursor.execute(
        f'SELECT Power,"Type   " FROM moves WHERE "Name   " = ?',
        (move,)
    )
    move_pwr, move_type = cursor.fetchone()

    if int(move_pwr) == 0:
        return 0

    if move_type not in ['Fire','Water','Electric','Grass','Ice','Psychic','Dragon','Dark']:
        attack = calc_stats(pokemon_name,pokemon_lvl,"Attack",-1)     
        defense = calc_stats(enemy_name,enemy_lvl,"Defense",-1) 

        attack_high = calc_stats(pokemon_name,pokemon_lvl,"Attack",1)     
        defense_high = calc_stats(enemy_name,enemy_lvl,"Defense",1) 
    else:
        attack = calc_stats(pokemon_name,pokemon_lvl,"Sp. Atk",-1)     
        defense = calc_stats(enemy_name,enemy_lvl,"Sp. Def",-1)  

        attack_high = calc_stats(pokemon_name,pokemon_lvl,"Sp. Atk",1)     
        defense_high = calc_stats(enemy_name,enemy_lvl,"Defense",1) 


    stab = 1
    if move_type == type1player or move_type == type2player:
        stab = 1.5

    weakness=['Fire-Grass','Fire-Ice','Fire-Bug','Fire-Steel','Water-Fire','Water-Ground','Water-Rock','Grass-Water','Grass-Ground','Grass-Rock','Electric-Water','Electric-Flying','Ice-Grass','Ice-Ground','Ice-Flying','Ice-Dragon','Fighting-Normal','Fighting-Ice','Fighting-Rock','Fighting-Steel','Fighting-Dark','Poison-Grass','Poison-Fairy','Ground-Fire','Ground-Electric','Ground-Poison','Ground-Rock','Ground-Steel','Flying-Grass','Flying-Fighting','Flying-Bug','Psychic-Fighting','Psychic-Poison','Bug-Grass','Bug-Psychic','Bug-Dark','Rock-Fire','Rock-Ice','Rock-Flying','Rock-Bug','Ghost-Psychic','Ghost-Ghost','Dragon-Dragon','Dark-Psychic','Dark-Ghost','Steel-Ice','Steel-Rock','Steel-Fairy']
    resist=['Ground-Water','Fire-Rock','Fire-Fire','Fire-Water','Fire-Dragon','Water-Water','Water-Grass','Water-Dragon','Grass-Flying','Grass-Poison','Grass-Bug','Grass-Steel','Grass-Fire','Grass-Grass','Grass-Dragon','Electric-Dragon','Electric-Electric','Electric-Grass','Ice-Steel','Ice-Water','Ice-Fire','Ice-Ice','Fighting-Bug','Fighting-Fairy','Fighting-Psychic','Fighting-Poison','Fighting-Flying','Poison-Ghost','Poison-Rock','Poison-Poison','Poison-Flying','Ground-Bug','Ground-Grass','Flying-Steel','Flying-Electric','Flying-Rock','Psychic-Steel','Psychic-Psychic','Bug-Fire','Bug-Flying','Bug-Ghost','Bug-Fighting','Bug-Poison','Bug-Steel','Bug-Fairy','Rock-Steel','Rock-Fighting','Rock-Ground','Ghost-Dark','Dragon-Steel','Dark-Fighting','Dark-Dark','Dark-Fairy','Steel-Fire','Steel-Water','Steel-Electric','Steel-Steel']
    immune=['Normal-Ghost','Electric-Ground','Fighting-Ghost','Ground-Flying','Psychic-Dark','Ghost-Normal']

    type_bonus = 1
    for typ in (type1enemy,type2enemy):
        check = f'{move_type}-{typ}'
        if check in weakness:
            type_bonus = type_bonus * 2
        elif check in resist:
            type_bonus = type_bonus / 2
        elif check in immune:
            type_bonus = 0

    dmg_low = math.floor(217/255 * (((2*int(pokemon_lvl)/5 + 2) * int(move_pwr) * int(attack)/int(defense_high))/50 + 2) * stab * type_bonus)
    dmg_high = math.floor(1 * (((2*int(pokemon_lvl)/5 + 2) * int(move_pwr) * int(attack_high)/int(defense))/50 + 2) * stab * type_bonus)
    return (f'{dmg_low} - {dmg_high}')