# Fluxura

Fluxura is a Python library that provides terminal styling and coloring options for enhancing the appearance of your command-line applications. With support for text styles like bold, italic, underline, and strikethrough, as well as foreground and background colors (including custom RGB colors), Fluxura gives you the power to customize the look of your terminal output with ease.

## Features

- **Text Styles**: Apply styles like **bold**, _italic_, `underline`, and `strikethrough` to your terminal text.
- **Colors**: Choose from predefined color options for foreground and background text colors.
- **Custom RGB Colors**: Set custom RGB background colors for a more personalized look.
- **Gradient (coming soon)**: Apply gradients to your text using two colors.
- **Simple API**: Easy-to-use functions for styling and coloring your text in the terminal.

## Features

- **Text Styles**: Apply styles like **bold**, _italic_, `underline`, and `strikethrough` to your terminal text.
- **Colors**: Choose from predefined color options for foreground and background text colors.
- **Custom RGB Colors**: Set custom RGB background colors for a more personalized look.
- **Gradient (coming soon)**: Apply gradients to your text using two colors.
- **Simple API**: Easy-to-use functions for styling and coloring your text in the terminal.

## Installation

You can install Fluxura using `pip` from PyPI (or TestPyPI for testing purposes).

### From PyPI:

`pip install fluxura`

`pip install --index-url https://test.pypi.org/simple/ fluxura`

### 4. **Example Usage**:

````markdown
## Usage

Once installed, you can start using Fluxura to style your terminal text.

```python
from fluxura import Color, Style, stylize

# Example 1: Apply bold and red color to text
text = stylize("Hello, World!", Style.BOLD, Color.fg("red"))
print(text)

# Example 2: Apply italic and blue color to text
text = stylize("This is a test.", Style.ITALIC, Color.fg("blue"))
print(text)

# Example 3: Use a custom RGB background color
text = stylize("Custom background color", Color.bg(255, 165, 0))  # RGB: Orange
print(text)

# Example 4: Combine multiple styles and colors
text = stylize("Bold, underlined, and green text", Style.BOLD, Style.UNDERLINE, Color.fg("green"))
print(text)


### 5. **Customization Section**:
```
````

## Customization

You can customize the foreground and background colors using built-in colors or by specifying RGB values.

- Predefined colors include: `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`, and `orange`.
- To use a custom RGB background color, pass the RGB values to the `Color.bg()` method like this:
  ```python
  Color.bg(255, 165, 0)  # RGB values for orange background
  ```
## ===
## FLUXURA IS STILL IN DEVELOPMENT, WITH MORE FEATURES COMING SOON...
## ===
