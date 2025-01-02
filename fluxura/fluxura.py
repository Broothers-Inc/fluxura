# v0.1.0-alpha

class Color:
    
    class Fore:

        # Classic Variants

        BLACK = "\033[30m"
        RED = "\033[31m"
        GREEN = "\033[32m"
        YELLOW = "\033[33m"
        BLUE = "\033[34m"
        MAGENTA = "\033[35m"
        CYAN = "\033[36m"
        WHITE =	"\033[37m"

        # Light/Bright Variants

        LIGHT_BLACK = "\033[90m"
        LIGHT_RED = "\033[91m"
        LIGHT_GREEN = "\033[92m"
        LIGHT_YELLOW = "\033[93m"
        LIGHT_BLUE = "\033[94m"
        LIGHT_MAGENTA = "\033[95m"
        LIGHT_CYAN = "\033[96m"
        LIGHT_WHITE =	"\033[97m"

        # Custom Variant
        
        def CUSTOM(r: int = 0, g: int = 0, b: int = 0):
            return f"\033[38;2;{r};{g};{b}m"

    class Back:

        # Classic Variants

        BLACK = "\033[40m"
        RED = "\033[41m"
        GREEN = "\033[42m"
        YELLOW = "\033[43m"
        BLUE = "\033[44m"
        MAGENTA = "\033[45m"
        CYAN = "\033[46m"
        WHITE =	"\033[47m"

        # Light/Bright Variants

        LIGHT_BLACK = "\033[100m"
        LIGHT_RED = "\033[101m"
        LIGHT_GREEN = "\033[102m"
        LIGHT_YELLOW = "\033[103m"
        LIGHT_BLUE = "\033[104m"
        LIGHT_MAGENTA = "\033[105m"
        LIGHT_CYAN = "\033[106m"
        LIGHT_WHITE =   "\033[107m"

        CLEAN = ""

        # Custom Variant

        def CUSTOM(r: int = 0, g: int = 0, b: int = 0):
            return f"\033[48;2;{r};{g};{b}m"

class Style:
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    DIM = "\033[2m"
    STRIKETHROUGH = "\033[9m"

def flux(text, *args):
    CLEAR = "\033[0m"
    check_empty = len(text.strip())
    if not check_empty:
        text = text.strip()
    styles = "".join(args)
    return f"{styles}{text}{CLEAR}"