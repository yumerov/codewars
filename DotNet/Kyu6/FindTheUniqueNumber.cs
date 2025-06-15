// https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/csharp

using System;
using System.Collections.Generic;

namespace DotNet.Kyu6;

public class FindTheUniqueNumber
{
    public static int GetUnique(IEnumerable<int> numbers)
    {
        var counts = new Dictionary<int, int>();
        foreach (var number in numbers)
        {
            if (!counts.TryAdd(number, 1)) { counts[number]++; }
        }

        foreach (var count in counts)
        {
            if (count.Value == 1)
            {
                return count.Key;
            }
        }

        return 0;
    }

    public static void Main()
    {
        Console.WriteLine($"{GetUnique([1, 2, 2, 2])} == 1");
    }
}