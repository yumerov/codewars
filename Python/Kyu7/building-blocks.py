# 'https://www.codewars.com/kata/building-blocks/train/python'

class Block(object):
    def __init__(self, sides):
        self.width, self.length, self.height = sides

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_height(self):
        return self.height

    def get_volume(self):
        return self.width * self.length * self.height

    def get_surface_area(self):
        w = self.width
        l = self.length
        h = self.height

        return 2 * (w * l + l * h + h * w)
