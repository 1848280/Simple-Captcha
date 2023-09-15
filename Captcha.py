from PIL import Image, ImageFont, ImageDraw
import random
import string
import numpy as np


def id_generator(size=1, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))


font = ImageFont.truetype("arial.ttf", 32)
im = Image.new("RGBA", (200, 100), (0, 0, 0, 0))
d = ImageDraw.Draw(im)

d.text((20, random.randint(40, 90)), id_generator(), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255), anchor="ms", font=font)
d.text((60, random.randint(40, 90)), id_generator(), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255), anchor="ms", font=font)
d.text((100, random.randint(40, 90)), id_generator(), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255), anchor="ms", font=font)
d.text((140, random.randint(40, 90)), id_generator(), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255), anchor="ms", font=font)
d.text((180, random.randint(40, 90)), id_generator(), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255), anchor="ms", font=font)


abc = Image.new("RGBA", (200, 100), (0, 0, 0, 128))
noise = np.random.randint(0, 256, (120, 160), dtype=np.uint8)
noise = (noise > 128) * 200
noiseim = Image.fromarray(noise.astype(np.uint8))
noiseim = noiseim.resize((200, 100), resample=Image.NEAREST)
im.paste(noiseim, mask=abc)


im.show()
im.save("captcha.png")