import easyocr

from PIL import Image

def image_to_text(path) : 

    reader = easyocr.Reader(['en'])
    result = reader.readtext(path)

    result = ' '.join([
        res[1]
        for res 
        in result
    ])

    return result