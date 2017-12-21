# https://www.codewars.com/kata/message-from-aliens/train/python

def decode(m):
    return 'blip blip die stupid people'

# tests

from unittest import TestCase
test = TestCase()
def t(a, b): test.assertEqual(decode(a), b)

t("]()]|_]|_]][-]|-|]", 'hello')
t('{|^{|{{|_{]3{','blip')
t('..[-.|_.|^....().[-.|^.__..|)...|.|^.|_|..~|~._\\~.__...[-..|.|)..',
  'die stupid people')
t("'''_\\~'|_|'()'|''('|'|_'[-'|)''__'_\\~'/<'()'()'|_'''__'|\\|'|''/\\'/?']3'__''/?'|_|''()'`/''",
  'your brain looks delicious')
t('}/\\}~|~}/\\}/<}__}|)}}}[-}~|~}/\\}(}|}|_}|^}|_|}|)}__}|)}}}|\\|}|}/=}__}()}}}~|~}__}`/}/?}}~|~}' 
  'try to find duplicated kata')