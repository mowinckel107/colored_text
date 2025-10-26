
from typing import Optional

WHITE_ANSI_COLOR_CODE = 37

def turn_text_colur( ansi_color_escape_code : int):
    print(f"\033[{ansi_color_escape_code}m", end="")

def print_text_red(text : str, print_end : Optional[str] = "\n"):
    red_ansi_color_code : int = 31 # normal red
    turn_text_colur(red_ansi_color_code)
    print(text, end=print_end)
    turn_text_colur(WHITE_ANSI_COLOR_CODE)

def print_text_green(text : str, print_end : Optional[str] = "\n"):
    red_ansi_color_code : int = 92 # bright green
    turn_text_colur(red_ansi_color_code)
    print(text, end=print_end)
    turn_text_colur(WHITE_ANSI_COLOR_CODE)

def print_text_yellow(text : str, print_end : Optional[str] = "\n"):
    red_ansi_color_code : int = 93 # bright yellow
    turn_text_colur(red_ansi_color_code)
    print(text, end=print_end)
    turn_text_colur(WHITE_ANSI_COLOR_CODE)