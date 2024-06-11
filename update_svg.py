# Libraries
import time

# Custom modules
from helpers.config import MSG_WIDTH
from helpers.variables import TAG_PADDING, TAG_HEIGHT, IMG_HEIGHT, LANGUAGES, COLORS, CATEGORIES, tag_names, SVG_TAG_WIDTH, color
from helpers.config import LANG_ID

def update_svg_template():
    with open('./helpers/assets/tag-template.svg', 'r', encoding='utf-8') as file:

        # Read tag's svg template
        tag_template = file.read()
        
        # Initialize variables
        tags, x, y = '', 0, 0

        # Each tag in the tag_names object (your skills) is created and concatenated into the final SVG
        for name, value in tag_names.items():
            tag = str(tag_template)
            if (x + value['width']) >= SVG_TAG_WIDTH:
                x = 0
                y += TAG_HEIGHT +TAG_PADDING

            # Data
            tag = tag.replace('{x}', str(x))
            tag = tag.replace('{y}', str(y))
            tag = tag.replace('{text}', name)

            # Colors
            tag = tag.replace('{fillColor}', COLORS[CATEGORIES[value['category']][1]]['secondary'])
            tag = tag.replace('{textColor}', COLORS[CATEGORIES[value['category']][1]]['primary'])
            tag = tag.replace('{strokeColor}', COLORS[CATEGORIES[value['category']][1]]['primary'])

            # Dimensions
            tag = tag.replace('{tagWidth}', str(value['width']))

            # Update Internal Variables
            tags += tag
            x += value['width'] +TAG_PADDING

    with open('./helpers/assets/template.svg', 'r', encoding='utf-8') as file:

        # Read svg template
        svg_data = file.read()

        # Data
        svg_data = svg_data.replace('{msg1}', LANGUAGES[LANG_ID]['traductions']['msg_1'])
        svg_data = svg_data.replace('{msg2}', LANGUAGES[LANG_ID]['traductions']['msg_2'])
        svg_data = svg_data.replace('{msg3}', LANGUAGES[LANG_ID]['traductions']['msg_3'])
        svg_data = svg_data.replace('{msg4}', LANGUAGES[LANG_ID]['traductions']['msg_4'])        
        svg_data = svg_data.replace('{tags}', tags)

        # Colors
        svg_data = svg_data.replace('{bgColor}', COLORS[color]['secondary'])
        svg_data = svg_data.replace('{textColor}', COLORS[color]['primary'])
        svg_data = svg_data.replace('{imageBorderColor}', COLORS[color]['primary'])

        # Dimensions
        svg_data = svg_data.replace('{tagHeight}', str(y +TAG_HEIGHT))
        svg_data = svg_data.replace('{SVG_TAG_WIDTH}', str(SVG_TAG_WIDTH))
        svg_data = svg_data.replace('{svgHeight-1}', str(IMG_HEIGHT +y +TAG_HEIGHT))
        svg_data = svg_data.replace('{svgHeight-2}', str(IMG_HEIGHT +y +TAG_HEIGHT))
        svg_data = svg_data.replace('{widthMsg4}', str(MSG_WIDTH))
        svg_data = svg_data.replace('{widthMsg3}', str(MSG_WIDTH))
        svg_data = svg_data.replace('{widthMsg2}', str(MSG_WIDTH))
        svg_data = svg_data.replace('{widthMsg1}', str(MSG_WIDTH))

    with open('./today.svg', 'w', encoding='utf-8') as file:
        file.write(svg_data)
    
    # Save proccess
    # Temperature split for ºC and get first item and then by space and get last item
    temp = (LANGUAGES[LANG_ID]['traductions']['msg_3']).split('°C')[0].split(' ')[-1]
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open('logs.txt', 'a', encoding='utf-8') as file:
        file.write(f"{now} - {temp}\n")

if __name__ == "__main__":
    # Calculate the time it takes for the script
    start = time.time()

    # Execute script
    update_svg_template()

    # Calculate the time it takes for the script
    end = time.time()
    total = end - start

    h = int(total // 3600)
    m = int((total % 3600) // 60)
    s = int(total % 60)

    # show total time
    print()
    print(f"Total time: {h}h - {m}min - {s}sec")
