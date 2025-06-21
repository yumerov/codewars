# https://www.codewars.com/kata/linux-history-and-%60-%60-command-series-number-1-the-%60-%60-command


from unittest import TestCase

def get_command_lines(history):
    commands = history.split("\n")
    return list(map(lambda x: x.strip().lstrip("0123456789").strip(), commands))

def bang_bang(history):
    commands = get_command_lines(history)
    return commands.pop()

test = TestCase()
history="   1  cd /pub\n  2  more beer\n  3  lost\n  4  ls \n  5  touch me \n  6  chmod 000 me \n  7  more me\n  8  history"
test.assertEqual(bang_bang(history), "history")
history="   1  cd /pub\n  2  more beer\n  3  lost\n  4  ls \n  5  touch me \n  6  chmod 000 me \n  7  history\n  8  more me"
test.assertEqual(bang_bang(history), "more me")
