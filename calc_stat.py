import math
import sqlite3
###for calculating pokemon stats:)
connection = sqlite3.connect('statystyki_pkmn.db')
cursor = connection.cursor()

def calc_stats(name,lvl,stat,nat):
    if nat == -1:
        nature = 0.9
        iv = 0
        ev = 0
    else:
        nature = 1.1
        ev = 85
        iv = 31

    cursor.execute(
        f'SELECT "{stat}" FROM gen1 WHERE Name = ?',
        (name,)
    )
    base_stat = cursor.fetchone()
    
    ret = (math.floor((lvl*(2*base_stat[0] + iv + math.floor(ev/4))/100 )) + 5)  * nature
    return(math.floor(ret))

def calc_hp(name,lvl,stat,nat):
    if nat == -1:
        nature = 0.9
        iv = 0
        ev = 0
    else:
        nature = 1.1
        ev = 85
        iv = 31

    cursor.execute(
        f'SELECT "{stat}" FROM gen1 WHERE Name = ?',
        (name,)
    )
    base_stat = cursor.fetchone()
    
    ret = math.floor((lvl*(2*base_stat[0] + iv + math.floor(ev/4))/100 )) + lvl + 10
    return(math.floor(ret))

def calc_hp_speed(name,lvl):
    hp_low = calc_hp(name,lvl,"HP",-1)
    hp_high = calc_hp(name,lvl,"HP",1)
    speed_low =calc_stats(name,lvl,"SPEED",-1)
    speed_high =  calc_stats(name,lvl,"SPEED",1)

    hp = f'{hp_low} - {hp_high}'
    speed = f'{speed_low} - {speed_high}'

    return(hp,speed)

# print(calc_stats("Swampert",50,"SPEED"))