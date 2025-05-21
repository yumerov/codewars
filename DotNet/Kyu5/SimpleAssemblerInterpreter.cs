// https://www.codewars.com/kata/58e24788e24ddee28e000053/train/csharp

using System;

namespace DotNet;

public class SimpleAssemblerInterpreter
{
    public static Dictionary<string, int> Interpret(string[] program)
    {
        var state = new Dictionary<string, int>();

        for (int index = 0; index < program.Length; index++)
        {
            var arguments = program[index].Split(' ');
            var command = arguments[0];
            var address = arguments[1];
            var argument = arguments.Length == 3 ? arguments[2] : null;

            switch (command)
            {
                case "mov":
                    state[address] = state.TryGetValue(argument, out var value) ? value : int.Parse(argument);
                    break;
                case "inc":
                    state[address]++; break;
                case "dec":
                    state[address]--; break;
                case "jnz":
                    bool isZero = int.TryParse(address, out int result) ?
                        result != 0 : state[address] != 0;
                    if (isZero) index += int.Parse(argument) - 1;
                    break;
                default: throw new InvalidOperationException($"Unknown command: {command}");
            }
        }

        return state;
    }

    private static void Test(string label, string[] program)
    {
        Console.WriteLine($"State {label}:");
        foreach (var kvp in Interpret(program))
        {
            Console.WriteLine($"{kvp.Key}: {kvp.Value}");
        }

        Console.WriteLine();
    }

    public static void Main()
    {
        Test("1", [
            "mov a 5",
            "inc a",
            "dec a",
            "dec a",
            "jnz a -1",
            "inc a"
        ]);

        Test("2", [
            "mov a -10",
            "mov b a",
            "inc a",
            "dec b",
            "jnz a -2"
        ]);

        Test("3", [
            "mov a 1",
            "mov b 1",
            "mov c 0",
            "mov d 26",
            "jnz c 2",
            "jnz 1 5",
            "mov c 7",
            "inc d",
            "dec c",
            "jnz c -2",
            "mov c a",
            "inc a",
            "dec b",
            "jnz b -2",
            "mov b c",
            "dec d",
            "jnz d -6",
            "mov c 18",
            "mov d 11",
            "inc a",
            "dec d",
            "jnz d -2",
            "dec c",
            "jnz c -5"
        ]);
    }
}