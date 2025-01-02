from fluxura import *

# Test Script for Flux Function
print("=" * 50)
print(flux("Fluxura TEST", Style.BOLD, Style.UNDERLINE, Color.Fore.CYAN))
print("=" * 50)

# Section 1: Basic Foreground Colors
print(flux("\nBasic Foreground Colors\n", Style.UNDERLINE, Style.BOLD, Color.Fore.YELLOW))
foreground_colors = [
    Color.Fore.BLACK, Color.Fore.RED, Color.Fore.GREEN, Color.Fore.YELLOW,
    Color.Fore.BLUE, Color.Fore.MAGENTA, Color.Fore.CYAN, Color.Fore.WHITE
]
for color in foreground_colors:
    print(flux(f"Foreground: {color}", color))

# Section 2: Basic Background Colors
print(flux("\nBasic Background Colors\n", Style.UNDERLINE, Style.BOLD, Color.Fore.MAGENTA))
background_colors = [
    Color.Back.BLACK, Color.Back.RED, Color.Back.GREEN, Color.Back.YELLOW,
    Color.Back.BLUE, Color.Back.MAGENTA, Color.Back.CYAN, Color.Back.WHITE
]
for color in background_colors:
    if color == Color.Back.WHITE:
        print(flux(f"Background: {color}", Color.Fore.BLACK, color))
    else:
        print(flux(f"Background: {color}", Color.Fore.WHITE, color))

# Section 3: Light Colors (Foreground)
print(flux("\nLight Foreground Colors\n", Style.UNDERLINE, Style.BOLD, Color.Fore.LIGHT_BLUE))
light_foreground_colors = [
    Color.Fore.LIGHT_BLACK, Color.Fore.LIGHT_RED, Color.Fore.LIGHT_GREEN, Color.Fore.LIGHT_YELLOW,
    Color.Fore.LIGHT_BLUE, Color.Fore.LIGHT_MAGENTA, Color.Fore.LIGHT_CYAN, Color.Fore.LIGHT_WHITE
]
for color in light_foreground_colors:
    print(flux(f"Light Foreground: {color}", color))

# Section 4: Light Colors (Background)
print(flux("\nLight Background Colors\n", Style.UNDERLINE, Style.BOLD, Color.Fore.LIGHT_CYAN))
light_background_colors = [
    Color.Back.LIGHT_BLACK, Color.Back.LIGHT_RED, Color.Back.LIGHT_GREEN, Color.Back.LIGHT_YELLOW,
    Color.Back.LIGHT_BLUE, Color.Back.LIGHT_MAGENTA, Color.Back.LIGHT_CYAN, Color.Back.LIGHT_WHITE
]
for color in light_background_colors:
    if color == Color.Back.LIGHT_WHITE:
        print(flux(f"Light Background: {color}", Color.Fore.BLACK, color))
    else:
        print(flux(f"Light Background: {color}", Color.Fore.WHITE, color))


# Section 5: Custom Colors (Foreground and Background)

custom_colors = [
    {"fg": (255, 255, 0), "bg": (0, 0, 139)},  # Bright Yellow text on Dark Blue
    {"fg": (30, 30, 30), "bg": (255, 125, 0)},  # Dark Black text on Bright Orange
    {"fg": (238, 130, 238), "bg": (75, 0, 130)},  # Violet text on Indigo
    {"fg": (255, 165, 0), "bg": (34, 139, 34)},  # Orange text on Forest Green
    {"fg": (173, 216, 230), "bg": (139, 0, 0)},  # Light Blue text on Dark Red
]

print(flux("\nCustom Color Showcase:\n", Style.UNDERLINE, Style.BOLD, Color.Fore.LIGHT_GREEN))
for color_pair in custom_colors:
    fg_code = Color.Fore.CUSTOM(*color_pair["fg"])
    bg_code = Color.Back.CUSTOM(*color_pair["bg"])
    text = f"Foreground: {color_pair['fg']}, Background: {color_pair['bg']}"
    print(flux(text, fg_code, bg_code))


# Section 6: Text Styles
print(flux("\nText Styles Showcase\n", Style.BOLD, Style.UNDERLINE, Color.Fore.LIGHT_MAGENTA))
text_styles = [
    Style.BOLD, Style.ITALIC, Style.UNDERLINE, Style.DIM, Style.STRIKETHROUGH
]
for style in text_styles:
    print(flux(f"Style: {style}", style, Color.Fore.YELLOW))

# Section 7: Combined Styles, Foreground, and Background
print(flux("\nCombined Styles, Foreground, and Background\n", Style.UNDERLINE, Style.BOLD, Color.Fore.RED))

print(flux("Bold Red on Green", Style.BOLD, Color.Fore.RED, Color.Back.GREEN))
print(flux("Italic Cyan on Yellow", Style.ITALIC, Color.Fore.CYAN, Color.Back.YELLOW))
print(flux("Underline Magenta on Blue", Style.UNDERLINE, Color.Fore.MAGENTA, Color.Back.BLUE))
print(flux("Dim Light Blue on Custom", Style.DIM, Color.Fore.LIGHT_BLUE, Color.Back.CUSTOM(70, 130, 180)))
print(flux("Strikethrough White on Custom", Style.STRIKETHROUGH, Color.Fore.WHITE, Color.Back.CUSTOM(255, 127, 80)))


print("=" * 50)
print(flux("End of TEST", Style.BOLD, Style.UNDERLINE, Color.Fore.CYAN))
print("=" * 50)
