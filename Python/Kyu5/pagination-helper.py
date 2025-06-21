# https://www.codewars.com/kata/paginationhelper/train/python

class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        return self.item_count() // self.items_per_page + 1

    def page_item_count(self, page_index):
        if page_index + 1 > self.page_count() or page_index < 0: return -1
        is_last_page = page_index + 1 == self.page_count()
        last_page_items = self.item_count() % self.items_per_page
        return last_page_items if is_last_page else self.items_per_page

    def page_index(self, item_index):
        if item_index >= self.item_count() or item_index < 0:
            return -1
        return item_index // self.items_per_page

# tests

import unittest

class PaginationHelperTest(unittest.TestCase):
    def setUp(self):
        self.helper = PaginationHelper(range(1, 25), 10)
    def test_page_count(self):
        self.assertEqual(self.helper.page_count(), 3)

    def test_page_index(self):
        self.assertEqual(self.helper.page_index(23), 2)

    def test_item_count(self):
        self.assertEqual(self.helper.item_count(), 24)

    def test_page_item_count(self):
        self.assertEqual(self.helper.page_item_count(3), 4)

if __name__ == '__main__':
    unittest.main()
