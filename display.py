import pyautogui
from fetch_moves_and_data import fetch_pokemon_data, fetch_move_data, create_move_list
from calc_stat import calc_hp_speed
import sqlite3


###creates a message to be displayed using other functions :)
def main():
    connection = sqlite3.connect('statystyki_pkmn.db')

    player_name,player_lvl,enemy_name,enemy_lvl = fetch_pokemon_data()
    moves_list = fetch_move_data()

    moves_and_dmg = create_move_list(player_name,enemy_name,moves_list,player_lvl,enemy_lvl)

    stats_player = calc_hp_speed(player_name,player_lvl)
    stats_enemy = calc_hp_speed(enemy_name,enemy_lvl)

    message = f'Player: {player_name} Lvl. {player_lvl}, HP: {stats_player[0]}, Speed: {stats_player[1]} \n \n Enemy: {enemy_name} Lvl. {enemy_lvl}, HP: {stats_enemy[0]}, Speed: {stats_enemy[1]} \n \n {moves_and_dmg}'
    return(message)

def display():
    pyautogui.alert(main())

display()