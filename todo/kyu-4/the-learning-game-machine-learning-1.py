# https://www.codewars.com/kata/the-learning-game-machine-learning-number-1/train/python

from unittest import TestCase


class Machine:
    def command(self, cmd, num):
        return cmd(num)

    def response(self, res):
        pass


# test
import random

test = TestCase()
_actions = [lambda x: x + 1, lambda x: 0, lambda x: x / 2, lambda x: x * 100,
            lambda x: x % 2]
print("Should apply the num * 0 action to the command 0")
machine = Machine()

random.seed()
for i in range(0, 20):
    r = machine.command(0, random.randint(0, 100))
    machine.response(r == 0)

test.assertEqual(machine.command(0, random.randint(0, 100)), 0)

machine = Machine()

tests = [(0, 100, 101, "Should apply the num + 1 action to the command 0"),
         (1, 100, 0, "Should apply the num * 0 action to the command 1"),
         (2, 100, 50, "Should apply the num / 2 action to the command 2"),
         (3, 1, 100, "Should apply the num * 100 action to the command 3"),
         (4, 100, 0, "Should apply the num % 2 action to the command 4")]

for i in range(0, 200):
    number = random.randint(0, 100)
    num = machine.command(i % 5, number)
    machine.response(_actions[i % 5](number) == num)

for t in tests:
    print(t[3])
    num = machine.command(t[0], t[1])
    test.assertEqual(num, t[2])
