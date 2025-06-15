// https://www.codewars.com/kata/58678d29dbca9a68d80000d7/train/csharp

using System;
using System.Collections.Generic;

namespace DotNet.Kyu5;

public class EsolangInterpreters2CustomSmallfookInterpreter
{
    private static Dictionary<int, int> BuildLoopMap(string code)
    {
        var loopMap = new Dictionary<int, int>();
        var tempStack = new Stack<int>();
        
        for (int index = 0; index < code.Length; index++)
        {
            switch (code[index])
            {
                case '[':
                    tempStack.Push(index);
                    break;
                case ']':
                {
                    int start = tempStack.Pop();
                    loopMap[start] = index;
                    loopMap[index] = start;
                    break;
                }
            }
        }

        return loopMap;
    }

    public static string Interpreter(string code, string tape)
    {
        var tapePointer = 0;
        var bitTape = tape.ToCharArray();
        var loopMap = BuildLoopMap(code);

        for (int codePointer = 0; codePointer < code.Length; codePointer++)
        {
            var instruction = code[codePointer];
            switch (instruction)
            {
                case '*': bitTape[tapePointer] = bitTape[tapePointer] == '0' ? '1' : '0'; break;
                case '>':
                {
                    tapePointer++;
                    if (tapePointer == tape.Length) return string.Join("", bitTape);
                    break;
                }
                case '<': 
                {
                    tapePointer--;
                    if (tapePointer == -1) return string.Join("", bitTape);
                    break;
                }
                case '[': if (bitTape[tapePointer] == '0') codePointer = loopMap[codePointer]; break;
                case ']': if (bitTape[tapePointer] != '0') codePointer = loopMap[codePointer]; break;
            }
        }
        
        
        return string.Join("", bitTape);
    }

    public static void Main()
    {
        Console.WriteLine($"{Interpreter("*", "00101100")} -> 10101100");
        Console.WriteLine($"{Interpreter(">*>*", "00101100")} -> 01001100");
        Console.WriteLine($"{Interpreter("*>*>*>*>*>*>*>*", "00101100")} -> 11010011");
        Console.WriteLine($"{Interpreter(">>>>>*<*<<*", "00101100")} -> 00000000");
        Console.WriteLine($"{Interpreter("[*>[>*>]>]", "11001")} -> 01100");
    }
}