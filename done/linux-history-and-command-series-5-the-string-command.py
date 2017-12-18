# https://www.codewars.com/kata/linux-history-and-%60-%60-command-series-number-5-the-%60-string%60-command/train/python


from unittest import TestCase

def get_command_lines(history):
    commands = history.split("\n")
    return list(map(lambda x: x.strip().lstrip("0123456789").strip(), commands))

def bang_contain_string(s,history):
    commands = get_command_lines(history)
    for command in commands[::-1]:
        if s in command:
            return command
    return "!{}: event not found".format(s)

test = TestCase()
history="   1  cd /pub\n  2  more beer\n  3  lost\n  4  ls\n  5  touch me\n  6  chmod 000 me\n  7  more me\n  8  history"
test.assertEqual(bang_contain_string("000",history), "chmod 000 me")
history="   1  cd /pub\n  2  more beer\n  3  lost\n  4  ls\n  5  touch me\n  6  chmod 000 me\n  7  history\n  8  more me"
test.assertEqual(bang_contain_string("me",history), "more me")
test.assertEqual(bang_contain_string("foo",history), "!foo: event not found")
