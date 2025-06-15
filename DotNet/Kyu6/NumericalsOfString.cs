// https://www.codewars.com/kata/5b4070144d7d8bbfe7000001/train/csharp

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace DotNet.Kyu6;

public class NumericalsOfString
{
    public static string Numericals(string str)
    {
        var counts = new Dictionary<char, int>();
        var result = new StringBuilder();
        
        for (var index = 0; index < str.Length; index++)
        {
            var letter = str[index];
            if (!counts.TryAdd(letter, 1)) { counts[letter]++; }
            result.Append(counts[letter]);
        }
        
        return result.ToString();
    }

    public static void Main()
    {
        Console.WriteLine($"{Numericals("Hello, World!")} == 1112111121311");
        Console.WriteLine($"{Numericals("Hello, World! It's me, JomoPipi!")} == 11121111213112111131224132411122");
        Console.WriteLine($"{Numericals("hello hello")} == 11121122342");
        Console.WriteLine($"{Numericals(new string('x', 1_000_000))}");
        Console.WriteLine($"{Numericals(string.Concat(Enumerable.Repeat("qwerty", 1000_000)))}");
    }
}