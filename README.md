# pOkeCR
#### Description:
My project aims to streamline the proccess of Pokémon nuzlocke calcing for Pokémon Fire Red by fetching all of the required data off of the screen. The function used to
smoothly run the app is the run_and_bun.py.

Inside the file is the code, which calls the main script (located in display.py) through the press of the F6 button. Running the code using a hotkey is important, 
as the whole screen needs to be visible during the proccess. The main function then runs the fetch_pokemon_data, fetch_moves_and_data, create_move_list and calc_hp_speed functions.

The fetch_pokemon_data and fetch_move_data files call for functions that take screenshots of the display, separate the image of the in-game font text into individual pictures and then use Hamming distance and fuzzy logic to compare them to a predefined dictionary of Pokémon Fire Red font letters. After being recognized, they are glued back together into the name of a Pokémon or a move name.

This string is then passed through a database, which lets us calculate the ranges for each pokemon's statistics and moves' damage. The ranges are important, as each pokemon's stats are "randomized" through the implementation of natures, EVs and IVs, which are mostly invisible for the player. The only way to obtain them seemlessly is by a connection with the emulator. This, however, goes outside the scope of this project.

### Features:
-Calculating the statistics' range for the Pokémon,
-Calculating the damage ranges for each of the moves,
-Accurate calculations due to Pokémon-type checking and adjustments for beneficial and hindering natures.
-Ease of use :)

![alt text](https://github.com/bersque/pOkeCR/blob/main/obraz.png "Logo Title Text 1")

### How to run:

1. Run run_and_bun.py.
2. Run Pokémon Fire Red on mGBA and windowed fullscreen.
3. Whenever needed, press F6 and run the script.
4. Enjoy!

The script must be ran on the mGBA emualtor in windowed fullscreen and 1980x1080 resolution. Otherwise, the regions of screenshots will not fit and the OCR will not yield satisfactory results. If one wishes to run pOkeCR on a different setup, it is needed to manually adjust the screenshot regions from fetch_moves_and_data and fetch_pokemon_data.



