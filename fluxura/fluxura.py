# v0.1.1-alpha0

ESC = "\033["
RESET = f"{ESC}0m"

class Color:
    """
    Provides ANSI escape codes for foreground and background colors, including classic, light,
    and custom variants.
    """

    class Fore:
        """
        Foreground color codes for text styling.
        """
        # Classic Variants
        BLACK = f"{ESC}30m"
        RED = f"{ESC}31m"
        GREEN = f"{ESC}32m"
        YELLOW = f"{ESC}33m"
        BLUE = f"{ESC}34m"
        MAGENTA = f"{ESC}35m"
        CYAN = f"{ESC}36m"
        WHITE = f"{ESC}37m"

        # Light/Bright Variants
        LIGHT_BLACK = f"{ESC}90m"
        LIGHT_RED = f"{ESC}91m"
        LIGHT_GREEN = f"{ESC}92m"
        LIGHT_YELLOW = f"{ESC}93m"
        LIGHT_BLUE = f"{ESC}94m"
        LIGHT_MAGENTA = f"{ESC}95m"
        LIGHT_CYAN = f"{ESC}96m"
        LIGHT_WHITE = f"{ESC}97m"

        # Custom Variant
        @staticmethod
        def CUSTOM(r: int = 0, g: int = 0, b: int = 0) -> str:
            """
            Creates a custom foreground color using RGB values.

            Args:
                r (int): Red component (0-255).
                g (int): Green component (0-255).
                b (int): Blue component (0-255).

            Returns:
                str: ANSI escape code for the custom color.
            """
            if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
                raise ValueError("RGB values must be between 0 and 255.")
            return f"{ESC}38;2;{r};{g};{b}m"

    class Back:
        """
        Background color codes for text styling.
        """
        # Classic Variants
        BLACK = f"{ESC}40m"
        RED = f"{ESC}41m"
        GREEN = f"{ESC}42m"
        YELLOW = f"{ESC}43m"
        BLUE = f"{ESC}44m"
        MAGENTA = f"{ESC}45m"
        CYAN = f"{ESC}46m"
        WHITE = f"{ESC}47m"

        # Light/Bright Variants
        LIGHT_BLACK = f"{ESC}100m"
        LIGHT_RED = f"{ESC}101m"
        LIGHT_GREEN = f"{ESC}102m"
        LIGHT_YELLOW = f"{ESC}103m"
        LIGHT_BLUE = f"{ESC}104m"
        LIGHT_MAGENTA = f"{ESC}105m"
        LIGHT_CYAN = f"{ESC}106m"
        LIGHT_WHITE = f"{ESC}107m"

        # Custom Variant
        @staticmethod
        def CUSTOM(r: int = 0, g: int = 0, b: int = 0) -> str:
            """
            Creates a custom background color using RGB values.

            Args:
                r (int): Red component (0-255).
                g (int): Green component (0-255).
                b (int): Blue component (0-255).

            Returns:
                str: ANSI escape code for the custom background color.
            """
            if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
                raise ValueError("RGB values must be between 0 and 255.")
            return f"{ESC}48;2;{r};{g};{b}m"

class Style:
    """
    Text styles using ANSI escape codes.
    """
    BOLD = f"{ESC}1m"
    DIM = f"{ESC}2m"
    ITALIC = f"{ESC}3m"
    UNDERLINE = f"{ESC}4m"
    BLINK = f"{ESC}5m"
    STRIKETHROUGH = f"{ESC}9m"

def flux(text: str, *args: str) -> str:
    """
    Applies the provided styles and colors to the given text.

    Args:
        text (str): The text to style.
        *args (str): The styles and colors to apply.

    Returns:
        str: The styled text with ANSI escape codes.
    """
    text = text.strip() or ""
    styles = "".join(filter(None, args))  # Skip None or invalid inputs
    return f"{styles}{text}{RESET}"

def __transition_int(start: int, stop: int, characters: int):
    """
    Takes in two RGB integers and creates interpolation steps between their values (start and stop
    inclusive)

    Args:
        start (int): Where to start interpolation
        stop (int): Where to end interpolation
        characters (int): How many steps to include in the interpolation including the start and end
    
    Returns:
        list: All of the steps, inclusive of the start and end
    """

    if characters < 2:
        raise ValueError("Two stop gradient requires two or more characters")

    change = (stop - start) / (characters - 1) # characters - 1 makes it end inclusive

    output = []
    x = start
    for _ in range(characters):
        output.append(round(x)) # if we keep the real value unrounded, then we don't lose precision
        if x > 255:
            x = 255
        elif x < 0:
            x = 0

        x += change

    return output

def __transition_list(start: list, stop: list, characters: int):
    """
    Takes in two lists of RGB values and creates interpolation steps with start and end inclusivity.
    
    Args:
        start (list): The starting RGB values you want to interpolate from
        stop (list): The ending RGB values
        characters (int): The number of steps that are made inclusive of the start and end
    
    Returns:
        list: The interpolated steps in lists of RGB values.
    """

    a = [__transition_int(start[0], stop[0], characters),
         __transition_int(start[1], stop[1], characters),
         __transition_int(start[2], stop[2], characters)] # interpolate the individual values

    output = []
    for i in range(characters):
        buffer = []
        for x in range(3):
            buffer.append(a[x][i]) # merge the three seperate r, g, and b lists into one

        output.append(buffer)

    return output

def twopointgrad(text: str, *args: str):
    """
    Applies a two point color gradient onto terminal text. Can apply foreground and background
    simultaneously.
    
    Args:
        text (str): The text to which the gradient colors should be applied to
        *args (str): The fore and/or back colors which should be applied. Only custom colors are 
        supported, not preset. Uses the first and last given color of one type as the points.
    
    Returns:
        str: Colored text.
    """

    ESC = "\033["
    RESET = f"{ESC}0m"

    fore_start = None
    fore_stop = None

    back_start = None
    back_stop = None

    for color in args:
        ctx = ""
        if color[2] == "3": # this indicates that it's foreground text
            ctx = "fore"
        else:
            ctx = "back"

        colorsplit = color.split(";")
        if len(colorsplit) == 1: # custom colors use three ;'s for each RGB value
            raise ValueError("Predefined color variants are incompatable with twopointgrad. " \
            "Please use custom RGB colors.")
        rgb_color = (int(colorsplit[2]), int(colorsplit[3]), int(colorsplit[4][:-1]))
        if ctx == "fore":
            if fore_start is None:
                fore_start = rgb_color # this applies the first given color to the start point
            else:
                fore_stop = rgb_color # all colors afterwards update the last point
        elif ctx == "back":
            if back_start is None:
                back_start = rgb_color
            else:
                back_stop = rgb_color

    new_str = ""
    fore_color_steps = None
    back_color_steps = None

    if fore_stop is None and back_stop is None:
        raise ValueError("twopointgrad requires at least two colors of a certain type.")

    if not fore_stop is None: # xxxx_stop means that at least two colors were used
        fore_color_steps = __transition_list(fore_start, fore_stop, len(text))
    if not back_stop is None:
        back_color_steps = __transition_list(back_start, back_stop, len(text))

    styling = ""

    for i, character in enumerate(text): # for each letter, get the assigned color and apply it
        if fore_color_steps:
            styling = Color.Fore.CUSTOM(
                fore_color_steps[i][0],
                fore_color_steps[i][1],
                fore_color_steps[i][2]
            )
        if back_color_steps:
            styling = f"{styling}{Color.Back.CUSTOM(
                back_color_steps[i][0],
                back_color_steps[i][1],
                back_color_steps[i][2]
            )}"

        new_str = f"{new_str}{styling}{character}"

    return f"{new_str}{RESET}"
