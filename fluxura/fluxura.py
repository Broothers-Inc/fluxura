# v0.1.1-alpha2

ESC = "\033["
RESET = f"{ESC}0m"

def _transition_int(start: int, stop: int, characters: int) -> list[int]:
    """
    Generate 'characters' evenly-spaced integer steps from start to stop (inclusive),
    clamped to the 0-255 range.

    Args:
        start (int): Start value.
        stop (int): Stop value.
        characters (int): Number of steps (must be >= 2).

    Returns:
        list[int]: Integer steps including start and stop.
    """
    if characters < 2:
        raise ValueError("Gradient requires two or more characters")

    step = (stop - start) / (characters - 1)
    # compute each step, clamp to [0,255], and round to nearest int
    return [
        int(round(max(0, min(255, start + step * i))))
        for i in range(characters)
    ]


def _transition_list(start: list, stop: list, characters: int) -> list[list[int]]:
    """
    Generate a list of RGB steps (each a list of three ints) interpolating from start to stop.

    Args:
        start (list): [r, g, b] start values.
        stop (list): [r, g, b] stop values.
        characters (int): Number of steps (must be >= 2).

    Returns:
        list[list[int]]: List of RGB steps.
    """
    if len(start) != 3 or len(stop) != 3:
        raise ValueError("start and stop must be 3-element RGB iterables")

    # compute each channel's transitions then zip them together
    channels = [
        _transition_int(int(s), int(e), characters)
        for s, e in zip(start, stop)
    ]

    return [
        [channels[0][i], channels[1][i], channels[2][i]]
        for i in range(characters)
    ]

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

        @staticmethod
        def GRAD(color1: list, color2: list):
            """
            Creates a foreground-only gradient function between two RGB colors.

            Args:
                color1 (list or tuple): Starting RGB values [r, g, b].
                color2 (list or tuple): Ending RGB values [r, g, b].

            Returns:
                function: A callable that takes text and returns it with a gradient applied.
            """
            start = list(color1)
            stop = list(color2)

            def apply_gradient(text: str):
                ESC = "\033["
                RESET = f"{ESC}0m"

                if not text:
                    return ""

                color_steps = _transition_list(start, stop, len(text))
                new_str = ""

                for i, ch in enumerate(text):
                    r, g, b = color_steps[i]
                    new_str += f"{ESC}38;2;{r};{g};{b}m{ch}"

                return f"{new_str}{RESET}"

            return apply_gradient

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
        
        @staticmethod
        def GRAD(color1: list, color2: list):
            """
            Creates a background-only gradient function between two RGB colors.

            Args:
                color1 (list or tuple): Starting RGB values [r, g, b].
                color2 (list or tuple): Ending RGB values [r, g, b].

            Returns:
                function: A callable that takes text and returns it with a gradient applied.
            """
            start = list(color1)
            stop = list(color2)

            def apply_gradient(text: str):
                ESC = "\033["
                RESET = f"{ESC}0m"

                if not text:
                    return ""

                color_steps = _transition_list(start, stop, len(text))
                new_str = ""

                for i, ch in enumerate(text):
                    r, g, b = color_steps[i]
                    new_str += f"{ESC}48;2;{r};{g};{b}m{ch}"

                return f"{new_str}{RESET}"

            return apply_gradient

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
        *args (str or callable): Styles, colors, or gradient functions.

    Returns:
        str: The styled text with ANSI escape codes.
    """
    text = text.strip() or ""

    # If a gradient function or other callable is passed, use it directly
    for arg in args:
        if callable(arg):
            return arg(text)

    # Otherwise join all string-based styles
    styles = "".join(filter(None, (a for a in args if isinstance(a, str))))
    return f"{styles}{text}\033[0m" if styles else text