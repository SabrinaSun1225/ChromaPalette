'''

Sabrina Sun 
Mar29, 2023

'''

import numpy as np
from scipy.interpolate import interp1d

from importlib import resources

#convert rgb to hex
def rgb_to_hex(rgb):
    hex_code = ""

    for color in rgb:
        hex_code += "{:02x}".format(int(color))

    return "#"+hex_code.upper()


#convert hex to rgb
def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return list(int(hex_code[i:i+2], 16) for i in (0, 2, 4))


def table_reader(file_name):
    #wsp = open(file_name)
    wsp = resources.open_text('ChromaPalette', file_name)
    lines = wsp.readlines()

    lines = lines[1:]

    color_dict = {}

    for line_str in lines:
        line_str = line_str.strip("\r")
        line_str = line_str.strip("\n")
        
        line_lis = line_str.split(",")
        name = line_lis[0]
        count = int(line_lis[1])
        colors = [color for color in line_lis if "#" in color]

        color_dict[name]=colors
    
    return color_dict


def auto_fill(input_palette,output_palette_length=5):
    #
    input_palette_length= len(input_palette)

    if input_palette_length >= output_palette_length:
        output_palette = input_palette[:output_palette_length]

    else:
        #use linear interpolation to generate the new colors

        input_R = [hex_to_rgb(input_hex)[0] for input_hex in input_palette]
        input_G = [hex_to_rgb(input_hex)[1] for input_hex in input_palette]
        input_B = [hex_to_rgb(input_hex)[2] for input_hex in input_palette]

        indx = list(range(input_palette_length))

        f_R = interp1d(indx,input_R)
        f_G = interp1d(indx,input_G)
        f_B = interp1d(indx,input_B)

        indx_new = np.linspace(0, input_palette_length-1, output_palette_length)
        output_R = f_R(indx_new)
        output_G = f_G(indx_new)
        output_B = f_B(indx_new)

        output_palette = []
        for i in range(len(indx_new)):
            R_i = output_R[i]
            G_i = output_G[i]
            B_i = output_B[i]

            hex = rgb_to_hex((R_i, G_i, B_i))
            output_palette.append(hex)
    
    return output_palette

def color_palette(name="Sunrise",N=8):

    data_dict = table_reader(file_name="ColorBars.csv")
    

    input_palette = data_dict[name]
    output_colors = auto_fill(input_palette,output_palette_length=N)

    return output_colors





    


