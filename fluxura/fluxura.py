# v0.1.0-alpha1

ESC = "\033["
RESET = f"{ESC}0m"

class Color:
    """
    Provides ANSI escape codes for foreground and background colors, including classic, light, and custom variants.
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
