# https://www.codewars.com/kata/two-fighters-one-winner/train/python

from unittest import TestCase


class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def attack(self, victim):
        victim.take_attack(self)

    def take_attack(self, attacker):
        self.health -= attacker.damage_per_attack

    def is_dead(self):
        return self.health <= 0

    def __str__(self):
        return self.name

def define_attacker_and_victim(f1, f2, fa):
    return [f1, f2] if f1.name == fa else [f2, f1]

def declare_winner(f1, f2, fa):
    a, v = define_attacker_and_victim(f1, f2, fa)
    while True:
        a.attack(v)
        if v.is_dead():
            return a.name
        a, v = v, a


test = TestCase()


def t(a, b, c, d):
    test.assertEqual(declare_winner(a, b, c), d)


t(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew", "Lew")
t(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Harry", "Harry")
t(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry", "Harald")
t(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harald", "Harald")
t(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry", "Harald")
t(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Harald", "Harald")
