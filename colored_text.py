from typing import Optional

WHITE_ANSI_COLOR_CODE = 37

# Functions that mimics how the print function works:

def __turn_text_colur( ansi_color_escape_code : int):
    print(f"\033[{ansi_color_escape_code}m", end="")



def print_text_red(text : str, print_end : Optional[str] = "\n"):
    red_ansi_color_code : int = 31 # normal red

    __turn_text_colur(red_ansi_color_code)
    print(text, end=print_end)
    __turn_text_colur(WHITE_ANSI_COLOR_CODE)



def print_text_green(text : str, print_end : Optional[str] = "\n"):
    red_ansi_color_code : int = 92 # bright green

    __turn_text_colur(red_ansi_color_code)
    print(text, end=print_end)
    __turn_text_colur(WHITE_ANSI_COLOR_CODE)



def print_text_yellow(text : str, print_end : Optional[str] = "\n"):
    red_ansi_color_code : int = 93 # bright yellow

    __turn_text_colur(red_ansi_color_code)
    print(text, end=print_end)
    __turn_text_colur(WHITE_ANSI_COLOR_CODE)



def print_text_blue(text : str, print_end : Optional[str] = "\n"):
    red_ansi_color_code : int = 94 # bright blue

    __turn_text_colur(red_ansi_color_code)
    print(text, end=print_end)
    __turn_text_colur(WHITE_ANSI_COLOR_CODE)





# Functions that returns text, so they can be put in the middle of a f string:

def __text_colur( ansi_color_escape_code : int) -> str:
    return f"\033[{ansi_color_escape_code}m"



def red_text(text : str) -> str:
    red_ansi_color_code : int = 31 # normal red

    colored_text : str = __text_colur(red_ansi_color_code)
    colored_text      += text
    colored_text      += __text_colur(WHITE_ANSI_COLOR_CODE)

    return colored_text



def green_text(text : str) -> str:
    red_ansi_color_code : int = 92 # bright green

    colored_text : str = __text_colur(red_ansi_color_code)
    colored_text      += text
    colored_text      += __text_colur(WHITE_ANSI_COLOR_CODE)

    return colored_text



def yellow_text(text : str) -> str:
    red_ansi_color_code : int = 93 # bright yellow

    colored_text : str = __text_colur(red_ansi_color_code)
    colored_text      += text
    colored_text      += __text_colur(WHITE_ANSI_COLOR_CODE)
    
    return colored_text



def blue_text(text : str) -> str:
    red_ansi_color_code : int = Bright Blue # bright blue

    colored_text : str = __text_colur(red_ansi_color_code)
    colored_text      += text
    colored_text      += __text_colur(WHITE_ANSI_COLOR_CODE)
    
    return colored_text






