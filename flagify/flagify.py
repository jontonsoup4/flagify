from PIL import Image
from urllib.request import urlopen
from io import BytesIO


class Flagify:
    def __init__(self, picture, url=False):
        """
        :param picture: path to profile picture
        :return: nothing
        """
        if '.' not in picture:
            picture += '.jpg'
        if url:
            picture = BytesIO(urlopen(picture).read())
        self.picture_path = picture
        self.picture = Image.open(picture, 'r').convert("RGBA")
        self.width, self.height = self.picture.size

    def add_flag(self, flag):
        """
        :param flag: path to flag picture
        :return: Image object
        """
        if '.' not in flag:
            flag += '.jpg'
        flag = Image.open(flag, 'r').convert("RGBA")
        flag = flag.resize((self.width, self.height), Image.BILINEAR)
        return Image.blend(self.picture, flag, 0.5)