# https://www.codewars.com/kata/competitive-eating-scoreboard/train/python

from unittest import TestCase

def transform(who):
    score = who.get("chickenwings", 0) * 5
    score += who.get("hamburgers", 0) * 3
    score += who.get("hotdogs", 0) * 2
    return {
        "name": who["name"],
        "score": score
    }

def scoreboard(who_ate_what):
    transformed = [transform(who) for who in who_ate_what]
    srtd = sorted(transformed, key=lambda x: x["name"])
    return sorted(srtd, key=lambda x: -x["score"])


test = TestCase()
test.assertEqual(scoreboard([{"name": "Billy The Beast", "chickenwings": 17,
                              "hamburgers": 7, "hotdogs": 8},
                             {"name": "Habanero Hillary", "chickenwings": 5,
                              "hamburgers": 17, "hotdogs": 11},
                             {"name": "Joey Jaws", "chickenwings": 8,
                              "hamburgers": 8, "hotdogs": 15},
                             {"name": "Big Bob", "chickenwings": 20,
                              "hamburgers": 4, "hotdogs": 11}]),
                 [{"name": "Big Bob", "score": 134},
                  {"name": "Billy The Beast", "score": 122},
                  {"name": "Habanero Hillary", "score": 98},
                  {"name": "Joey Jaws", "score": 94}])
test.assertEqual(scoreboard(
    [{"name": "Big Bob", "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}]),
                 [{"name": "Big Bob", "score": 134}])
test.assertEqual(scoreboard(
    [{"name": "Joey Jaws", "chickenwings": 8, "hamburgers": 8, "hotdogs": 15},
     {"name": "Big Bob", "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}]),
                 [{"name": "Big Bob", "score": 134},
                  {"name": "Joey Jaws", "score": 94}])
test.assertEqual(scoreboard(
    [{"name": "Joey Jaws", "chickenwings": 0, "hamburgers": 1, "hotdogs": 1},
     {"name": "Big Bob", "chickenwings": 1, "hamburgers": 0, "hotdogs": 0}]),
                 [{"name": "Big Bob", "score": 5},
                  {"name": "Joey Jaws", "score": 5}])
test.assertEqual(scoreboard([]), [])
