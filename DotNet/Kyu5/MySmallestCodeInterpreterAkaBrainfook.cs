// https://www.codewars.com/kata/526156943dfe7ce06200063e/train/csharp

using System;
using System.Collections.Generic;

namespace DotNet;

public class MySmallestCodeInterpreterAkaBrainfook
{
    /**
     * > = increases memory pointer, or moves the pointer to the right 1 block.
     * < = decreases memory pointer, or moves the pointer to the left 1 block.
     * + = increases value stored at the block pointed to by the memory pointer
     * - = decreases value stored at the block pointed to by the memory pointer
     * [ = like c while(cur_block_value != 0) loop.
     * ] = if block currently pointed to's value is not zero, jump back to [
     * , = like c getchar(). input 1 character.
     * . = like c putchar(). print 1 character to the console
     *
     * https://gist.github.com/roachhd/dce54bec8ba55fb17d3a
     */
    public static string BrainLuck(string code, string input)
    {
        byte[] memory = new byte[1000];
        int memoryPointer = 0;
        int inputPointer = 0;
        string output = "";
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

        for (int index = 0; index < code.Length; index++)
        {
            char instruction = code[index];
            switch (instruction)
            {
                case '>': memoryPointer++; break;
                case '<': memoryPointer--; break;
                case '+': memory[memoryPointer]++; break;
                case '-': memory[memoryPointer]--; break;
                case '.': output += (char)memory[memoryPointer]; break;
                case ',': memory[memoryPointer] = (byte)input[inputPointer++]; break;
                case '[':
                    if (memory[memoryPointer] == 0) index = loopMap[index];
                    break;
                case ']': if (memory[memoryPointer] != 0) index = loopMap[index];
                    break;
                default: throw new ArgumentException($"Unknown instruction: {instruction}");
            }
        }

        return output;
    }

    public static void Main()
    {
        Console.WriteLine($"{BrainLuck(",+[-.,+]","Codewars" + char.ConvertFromUtf32(255))}");
        Console.WriteLine($"{BrainLuck(",[.[-],]", "Codewars" + char.ConvertFromUtf32(0))}");
        Console.WriteLine($"{BrainLuck(",>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.", char.ConvertFromUtf32(8) + char.ConvertFromUtf32(9))}");
    }
}