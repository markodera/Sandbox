import sys
import numpy as np
from PIL import Image

# ASCII characters in order of intensity
ASCII_CHARS = [' ', '.', ',', ':', '+', '*', '?', '%', 'S', '#', '@']

def resize_image(image, new_width=100):
    """Resize image maintaining aspect ratio."""
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized = image.resize((new_width, new_height))
    return resized

def grayscale(image):
    """Convert image to grayscale."""
    return image.convert('L')

def map_pixels_to_ascii_chars(image, range_width=25):
    """Map pixels to ASCII characters based on intensity."""
    pixels = np.array(image.getdata())
    ascii_chars = [ASCII_CHARS[pixel // range_width] for pixel in pixels]
    return ''.join(ascii_chars)

def generate_ascii_art(image_path, new_width=100):
    """Generate ASCII art from image."""
    image = Image.open(image_path)
    image = resize_image(image, new_width)
    image = grayscale(image)
    
    ascii_str = map_pixels_to_ascii_chars(image)
    img_width = image.width
    ascii_art = '\n'.join([ascii_str[i:(i+img_width)] for i in range(0, len(ascii_str), img_width)])
    
    return ascii_art

# Path to your Mona Lisa image
image_path = 'passport.jpg'

# Generate and print ASCII art
ascii_art = generate_ascii_art(image_path)
print(ascii_art)

# Optionally, save the ASCII art to a text file
with open('monalisa_ascii.txt', 'w') as f:
    f.write(ascii_art)
