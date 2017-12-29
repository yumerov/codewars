# https://www.codewars.com/kata/street-fighter-2-character-selection-part-2/train/python

moves_map = {
    "up": lambda y, x: (y - 1, x,),
    "right": lambda y, x: (y, x + 1),
    "down": lambda y, x: (y + 1, x,),
    "left": lambda y, x: (y, x - 1,),
}

moves_opposites = {
    "up": "down",
    "down": "up",
    "left": "right",
    "right": "left",
}


def move_cursor(cursor, direction):
    return moves_map.get(direction)(cursor[0], cursor[1])


def calc_cursor_position(cursor, move, fighters):
    cursor = move_cursor(cursor, move)
    if move == "up" and fighters[cursor[0]][cursor[1]] == "":
        return move_cursor(cursor, "down")

    if move == "down" and cursor[0] == len(fighters):
        return move_cursor(cursor, "up")

    if move == "right" and cursor[1] == len(fighters[0]) - 1:
        return (cursor[0], 1,)

    return cursor


def super_street_fighter_selection(fighters, cursor, moves):
    if len(moves) == 0:
        return []

    path = []
    for move in moves:
        cursor = calc_cursor_position(cursor, move, fighters)
        fighter = fighters[cursor[0]][cursor[1]]
        path.append(fighter)
    return path


# tests

import unittest


class StreetFigherTest(unittest.TestCase):
    def setUp(self):
        self.fighters = [
            ["", "Ryu", "E.Honda", "Blanka", "Guile", ""],
            ["Balrog", "Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat"],
            ["Vega", "T.Hawk", "Fei Long", "Deejay", "Cammy", "M.Bison"]
        ]

    # should work with no selection cursor moves
    def test_simple(self):
        moves = []
        position = (0, 0)
        solution = []
        actual = super_street_fighter_selection(self.fighters, position, moves)
        self.assertEqual(actual, solution)

    # should stop on empty spaces vertically
    def test_stop_on_empty(self):
        moves = ["up"]
        position = (1, 0)
        solution = ['Balrog']
        actual = super_street_fighter_selection(self.fighters, position, moves)
        self.assertEqual(actual, solution)

    # hould stop on empty spaces vertically
    def test_stop_on_vertical_empty(self):
        moves = ["up"] * 4
        position = (1, 0)
        solution = ['Balrog'] * 4
        actual = super_street_fighter_selection(self.fighters, position, moves)
        self.assertEqual(actual, solution)

    # should stop vertically
    def test_vertical_stop(self):
        moves = ["down"] * 4
        position = (2, 0)
        solution = ['Vega'] * 4
        actual = super_street_fighter_selection(self.fighters, position, moves)
        self.assertEqual(actual, solution)

    # should stop on empty spaces vertically
    def test_should_stop_on_empty_spaces_vertically(self):
        moves = ["up"] * 4
        position = (1, 5)
        solution = ['Sagat'] * 4
        actual = super_street_fighter_selection(self.fighters, position, moves)
        self.assertEqual(actual, solution)

    # should stop vertically
    def test_should_stop_vertically(self):
        moves = ["down"] * 4
        position = (1, 5)
        solution = ['M.Bison'] * 4
        actual = super_street_fighter_selection(self.fighters, position, moves)
        self.assertEqual(actual, solution)

    # should rotate horizontally
    def test_should_rotate_horizontally(self):
        moves = ["left"] * 8
        position = (1, 3)
        solution = ['Chun Li', 'Ken', 'Balrog', 'Sagat', 'Dhalsim', 'Zangief', 'Chun Li', 'Ken']
        actual = super_street_fighter_selection(self.fighters, position, moves)
        self.assertEqual(actual, solution)

    # should rotate horizontally with empty spaces
    def test_should_rotate_horizontally_with_empty_spaces(self):
        moves =  ["right"] * 8
        position = (0, 2)
        solution = ['Blanka', 'Guile', 'Ryu', 'E.Honda', 'Blanka', 'Guile', 'Ryu', 'E.Honda']
        self.assertEqual(super_street_fighter_selection(self.fighters, position, moves), solution)

class StreetFigherAdvancedTest(unittest.TestCase):
    def setUp(self):
        self.fighters = [
            [        "",     "Ryu",  "E.Honda",  "Cammy" ],
            [  "Balrog",     "Ken",  "Chun Li",       "" ],
            [    "Vega",        "", "Fei Long", "Balrog",],
            [  "Blanka",   "Guile",         "", "Chun Li"],
            [ "M.Bison", "Zangief",  "Dhalsim", "Sagat"  ],
            [  "Deejay",   "Cammy",         "", "T.Hawk" ]
        ]

    # should work with longer grid
    def test_longer_grid(self):
        moves =  ["left"] * 2 + ["down"] + ["right"] * 4 + ["down"]
        moves += ["left"] * 4 + ["down"] + ["right"] * 2 + ["down"]
        moves += ["right"] * 3 + ["down"] + ["left"] * 3 + ["down"]
        moves += ["left"] * 3
        position = (0,3)
        solution = ['E.Honda', 'Ryu', 'Ken', 'Chun Li', 'Balrog', 'Ken', 'Chun Li', 'Fei Long', 'Vega', 'Balrog', 'Fei Long', 'Vega', 'Blanka', 'Guile', 'Chun Li', 'Sagat', 'M.Bison', 'Zangief', 'Dhalsim', 'Dhalsim', 'Zangief', 'M.Bison', 'Sagat', 'T.Hawk', 'Cammy', 'Deejay', 'T.Hawk']
        self.assertEqual(super_street_fighter_selection(self.fighters, position, moves), solution)

#

#
# test.it("should work with odd initial position")
# moves =  ["left"]*2+["down"]+["right"]*4+["down"]+["left"]*4+["up"]+["right"]*2+["up"]+["right"]*3
# position = (3,3)
# solution = ['Guile', 'Blanka', 'M.Bison', 'Zangief', 'Dhalsim', 'Sagat', 'M.Bison', 'Deejay', 'T.Hawk', 'Cammy', 'Deejay', 'T.Hawk', 'Sagat', 'M.Bison', 'Zangief', 'Guile', 'Chun Li', 'Blanka', 'Guile']
# test.assert_equals(super_street_fighter_selection(fighters4,position, moves), solution)



if __name__ == '__main__':
    unittest.main()
