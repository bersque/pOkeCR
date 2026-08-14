import keyboard
import subprocess

###used to run the display script with just the hotkey:) Just pause the game on the upper healthbar position and press f6, wait a few seconds and voila!
keyboard.add_hotkey("f6", lambda: subprocess.Popen(
    ["python", r"C:/Users/Kacper/Desktop/programowanie/pkmncalc/project_files_final/display.py"]
))
print("The script is running...")
keyboard.wait()