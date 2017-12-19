# https://www.codewars.com/kata/shop-inventory-manager/train/python

import unittest

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def increase_quality(self):
        self.quality += 1

    def decrease_quality(self):
        if self.quality > 0:
            self.quality -= 1

    def is_under_quality_limit(self):
        return self.quality < 50


items=[]

items+=[Item('+5 Dexterity Vest', 10, 20)]
items+=[Item('Aged Brie', 2, 0)]
items+=[Item('Elixir of the Mongoose', 5, 7)]
items+=[Item('Sulfuras, Hand of Ragnaros', 0, 80)]
items+=[Item('Backstage passes to a TAFKAL80ETC concert', 15, 20)]
items+=[Item('Conjured Mana Cake', 3, 6)]

# def update_quality():
#     ignored_names = [
#         'Aged Brie',
#         'Backstage passes to a TAFKAL80ETC concert',
#         'Sulfuras, Hand of Ragnaros'
#     ]
#     for i in range(len(items)):
#         if items[i].name not in ignored_names:
#             items[i].decrease_quality()
#         elif items[i].is_under_quality_limit():
#             items[i].increase_quality()
#             if items[i].name == 'Backstage passes to a TAFKAL80ETC concert':
#                 if items[i].sell_in < 11: items[i].increase_quality()
#                 if items[i].sell_in < 6: items[i].increase_quality()
#
#         if items[i].name != 'Sulfuras, Hand of Ragnaros':
#             items[i].sell_in = items[i].sell_in - 1
#
#         if items[i].sell_in < 0:
#             if items[i].name not in ignored_names:
#                 items[i].decrease_quality()
#             elif items[i].is_under_quality_limit():
#                 items[i].increase_quality()
#             else:
#                 items[i].quality = 0
#
#         if items[i].name == 'Conjured Mana Cake':
#             items[i].decrease_quality()

def update_quality():
    pass


class TestSolution(unittest.TestCase):
    def test_first_item(self):
        self.assertEqual(items[0].sell_in, 9, "Expected different value")
        self.assertEqual(items[0].quality, 19, "Expected different value")

    def test_second_item(self):
        self.assertEqual(items[1].sell_in, 1, "Expected different value")
        self.assertEqual(items[1].quality, 1, "Expected different value")

    def test_third_item(self):
        self.assertEqual(items[2].sell_in, 4, "Expected different value")
        self.assertEqual(items[2].quality, 6, "Expected different value")

    def test_forth_item(self):
        self.assertEqual(items[3].sell_in, 0, "Expected different value")
        self.assertEqual(items[3].quality, 80, "Expected different value")

    def test_fifth_item(self):
        self.assertEqual(items[4].sell_in, 14, "Expected different value")
        self.assertEqual(items[4].quality, 21, "Expected different value")

    def test_sixth_item(self):
        self.assertEqual(items[5].sell_in, 2, "Expected different value")
        self.assertEqual(items[5].quality, 4, "Expected different value")

if __name__ == '__main__':
    update_quality()
    unittest.main()
