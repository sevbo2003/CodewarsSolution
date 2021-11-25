# 5KYU
"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3

https://www.codewars.com/kata/513e08acc600c94f01000001/train/python
"""

def color(RGB):
    if RGB > 255:
        RGB = 255
    elif RGB < 0:
        RGB = 0
    RGB = hex(RGB)[2:].upper()
    if len(RGB)<2:
        RGB = '0'+RGB
    return RGB

def rgb(r, g, b):
    return color(r)+color(g)+color(b)


print(rgb(254,253,252))
