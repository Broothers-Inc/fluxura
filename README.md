# 🎨 Fluxura 🖌️
### ⚠️FLUXURA IS IN THE ALPHA STAGE OF DEVELOPMENT, EXPECT BUGS⚠️

Fluxura is a Python library that provides terminal styling and coloring options for enhancing the appearance of command-line applications. With support for text styles like bold, italic, underline, and strikethrough, as well as foreground and background colors (including custom RGB colors), Fluxura gives the power to customize the look of terminal output with ease.

## 🔦Features

- **Text Styles**: Apply styles like `BOLD`, `ITALIC`, `DIM`, `UNDERLINE`, and `STRIKETHROUGH` to terminal text.
- **Colors**: Choose from predefined color options for foreground and background text colors.
- **Custom RGB Colors**: Set custom RGB background colors for a more personalized look.
- **Gradient (hoping to develop)**: Apply gradients to text using two colors.
- **Simple API**: Easy-to-use functions for styling and coloring text in the terminal.

## 📦Installation

You can install Fluxura using `pip` from PyPI (or TestPyPI for testing purposes).

### From PyPI:

`pip install fluxura`

### 4. **Example Usage**:

````markdown

Once installed, you can start using Fluxura to style terminal text.

```python
from fluxura import Color, Style, flux

# Example 1: Apply bold and red color to text
print(flux("Hello, World!", Style.BOLD, Color.fore.RED))

# Example 2: Apply italic and blue color to text
print(flux("This is a test!",  Style.ITALIC, Color.fore.BLUE))

# Example 3: Use a custom RGB background color
print(flux("Custom background colour!",  Style.ITALIC, Color.Back.CUSTOM(255, 165, 0))

# Example 4: Combine multiple styles and colors
print(flux("Bold, underlined, and green text",  Style.BOLD, Style.UNDERLINE, Color.Fore.GREEN)
````

## 🎨Customization

Fluxura can customize the foreground and background colors using built-in colors or by specifying RGB values. It can also customise the styles of the text in multiple ways.

- Colours
  - Predefined colors:
    - Classic Variants: `BLACK`, `RED`, `GREEN`, `YELLOW`, `BLUE`, `MAGENTA`, `CYAN`, `WHITE`.
    - Light Variants: `LIGHT_BLACK`, `LIGHT_RED`, `LIGHT_GREEN`, `LIGHT_YELLOW`, `LIGHT_BLUE`, `LIGHT_MAGENTA`, `LIGHT_CYAN`,     `LIGHT_WHITE`.
  - To use a custom RGB color, pass the RGB values to the `Color.____.custom()` method like this:
    ```python
    Color.Fore.CUSTOM(255, 165, 0)  # RGB values for orange foreground
    Color.Back.CUSTOM(255, 165, 0)  # RGB values for orange backgroun
    ```
- Styles
    - Style Variants: `BOLD`, `BRIGHT`, `DIM`, `ITALIC`, `STRIKETHROUGH`
---
 
### 🔨MANY MORE FEATURES ARE EXPECTED TO COME SOON🔨
