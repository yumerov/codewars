# https://www.codewars.com/kata/transposing-a-song/train/python

from unittest import TestCase

notes_sharps = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
notes_letter = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']


def transponse_note(note, interval):
    if note in notes_sharps:
        current_notation = notes_sharps
    else:
        current_notation = notes_letter

    i = current_notation.index(note)
    l = len(current_notation)
    return notes_sharps[(i + interval + l) % l]

def transpose(song, interval):
    return [transponse_note(note, interval) for note in song]

test = TestCase()
inp = ['A']
out = transpose(inp, 1)
ans = ['A#']
test.assertEqual(out, ans, "Input: {}, 1".format(inp))

inp = ['Bb', 'C#', 'E']
out = transpose(inp, -4)
ans = ['F#', 'A', 'C']
test.assertEqual(out, ans, "Input: {}, -4".format(inp))
#
inp = ['C', 'C', 'C#', 'D', 'F', 'D', 'F', 'D', 'D', 'C#', 'C', 'G', 'C', 'C']
out = transpose(inp, 4)
ans = ['E', 'E', 'F', 'F#', 'A', 'F#', 'A', 'F#', 'F#', 'F', 'E', 'B', 'E', 'E']
test.assertEqual(out, ans, "Input: {}, 4".format(inp))