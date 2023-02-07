from PIL import Image
import base64


def decode():
    image = Image.open("planet_.png", 'r')

    data = ''
    imgdata = iter(image.getdata())

    while True:
        pixels = [value for value in imgdata.__next__()[:3] +
                  imgdata.__next__()[:3] +
                  imgdata.__next__()[:3]]

        # string of binary data
        binstr = ''

        for i in pixels[:8]:
            if i % 2 == 0:
                binstr += '0'
            else:
                binstr += '1'

        data += chr(int(binstr, 2))
        if pixels[-1] % 2 != 0:
            return base64.b64decode(data)


with open("stegano.answer", "w+") as f:
    f.write(str(decode()).replace('\\r\\n', '\n'))
