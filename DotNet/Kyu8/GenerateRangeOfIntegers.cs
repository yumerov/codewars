// https://www.codewars.com/kata/generate-range-of-integers/train/csharp

using System;

namespace DotNet.Kyu8;

using System.Collections.Generic;

public class GenerateRangeOfIntegers
{
    public static int[] GenerateRange(int min, int max, int step)
    {
        List<int> list = new List<int>();

        while (min <= max)
        {
            list.Add(min);
            min += step;
        }

        return list.ToArray();
    }

    public static void Main()
    {
        Console.WriteLine(string.Join(", ", GenerateRange(1, 10, 1)));
        Console.WriteLine(string.Join(", ", GenerateRange(-10, 1, 1)));
        Console.WriteLine(string.Join(", ", GenerateRange(1, 15, 20)));
    }
}