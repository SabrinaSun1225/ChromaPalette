# ChromaPalette: A Versatile Scientific Color Palette Library

Are you tired of spending countless hours searching for the perfect color scheme for your scientific visualizations? Look no further! Introducing **ChromaPalette** - a comprehensive and versatile color palette library tailored for researchers and scientists. With 19 stunning and carefully designed color schemes, creating eye-catching and informative visualizations has never been easier!

## Features
- **19 Unique Color Schemes**: Featuring a diverse range of color schemes, from gradient to low saturation, Morandi-inspired palettes, and vibrant, high contrast options.
- **Time Saving**: Eliminate the need to search the internet for color palettes - ChromaPalette has you covered.
- **Designed for Science**: Crafted specifically for the scientific community, each color scheme is suited for various types of data visualization.
- **Effortless Color Scheme Creation**: Auto-generate custom color schemes with ChromaPalette. Simply choose a scheme and input the number of colors, and ChromaPalette takes care of the rest, seamlessly filling in gaps with gradient colors when needed. The possibilities are endless!
- **Color Code Conversion**: ChromaPalette effortlessly converts between HEX and RGB color codes, allowing you to switch between formats depending on your needs. Create beautiful color schemes with ease and translate them seamlessly with ChromaPalette.


## Color Schemes
1. Coral
<img src="./color_imgs/Coral.svg" alt="Coral SVG" width="500">

2. VanGogh
<img src="./color_imgs/VanGogh.svg" alt="VanGogh SVG" width="500">

3. CafeTarrence
<img src="./color_imgs/CafeTarrence.svg" alt="CafeTarrence SVG" width="500">

4. MintGradient
<img src="./color_imgs/MintGradient.svg" alt="MintGradient SVG" width="500">

5. Candies
<img src="./color_imgs/Candies.svg" alt="Candies SVG" width="500">

6. Macarons
<img src="./color_imgs/Macarons.svg" alt="Macarons SVG" width="500">

7. Matcha
<img src="./color_imgs/Matcha.svg" alt="Matcha SVG" width="500">

8. Melody
<img src="./color_imgs/Melody.svg" alt="Melody SVG" width="500">

9. Lollipop
<img src="./color_imgs/Lollipop.svg" alt="Lollipop SVG" width="500">

10. Sunrise
<img src="./color_imgs/Sunrise.svg" alt="Sunrise SVG" width="500">

11. Monet
<img src="./color_imgs/Monet.svg" alt="Monet SVG" width="500">

12. Waterlilies
<img src="./color_imgs/Waterlilies.svg" alt="Waterlilies SVG" width="500">

13. Sunflowers
<img src="./color_imgs/Sunflowers.svg" alt="Sunflowers SVG" width="500">

14. Irises
<img src="./color_imgs/Irises.svg" alt="Irises SVG" width="500">

15. WheatFields
<img src="./color_imgs/WheatFields.svg" alt="WheatFields SVG" width="500">

16. Serene
<img src="./color_imgs/Serene.svg" alt="Serene SVG" width="500">

17. Elegant
<img src="./color_imgs/Elegant.svg" alt="Elegant SVG" width="500">

18. Vibrance
<img src="./color_imgs/Vibrance.svg" alt="Vibrance SVG" width="500">

19. Radiant
<img src="./color_imgs/Radiant.svg" alt="Radiant SVG" width="500">

## Get Started
To start using ChromaPalette, simply clone or download the repository from GitHub and import it into your favorite data visualization tool.
```
git clone https://github.com/SabrinaSun1225/ChromaPalette
```

To install the package, please input
```
python setup.py install
```

You may update your PYTHONPATH with
```
export PYTHONPATH="put-your-path-here:$PYTHONPATH"
```

The following code can be used to import ChromaPalette:
```
from ChromaPalette.chroma_palette import *
```

To generate a list of colors from a color scheme, you can use the following code:
```
your_color_list = color_palette(name="Sunrise",N=8)
```
Here, "**N**" is the number of colors and "**name**" is the name of the color scheme.

If you have a HEX code, but you want its RGB code. You can use function "hex_to_rgb":
```
rgb = hex_to_rgb(hex)
```
To convert an RGB code (e.g., rgb=[R, G, B]) to a HEX code, you can use the 'rgb_to_hex' function:
```
hex = rgb_to_hex(rgb)
```

## Colorblind-Friendly Visualizations 

Please use the tool below to check that the color schemes you generate are colorblind-friendly [https://color.adobe.com/create/color-accessibility](https://color.adobe.com/create/color-accessibility)

**Learn more about colorblind-friendly visualizations**: 

Check out this article from Nature for more information: [https://www.nature.com/articles/d41586-021-02696-z](https://www.nature.com/articles/d41586-021-02696-z)





With ChromaPalette, you can elevate the aesthetics of your visualizations and captivate your audience. Don't wait - try ChromaPalette today and let your data speak for itself!
