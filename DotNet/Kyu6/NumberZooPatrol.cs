// https://www.codewars.com/kata/5276c18121e20900c0000235/train/csharp

using System;
using System.Collections.Generic;

namespace DotNet.Kyu6;

public class NumberZooPatrol
{
    /// <summary>
    /// O(n)
    /// </summary>
    /// <param name="array"></param>
    /// <returns></returns>
    public static int FindNumber(int[] array)
    {
        var counts = new Dictionary<int, bool>();

        for (int index = 1; index <= array.Length; index++)
        {
            counts.Add(array[index - 1], true);
        }
        
        for (int index = 1; index <= array.Length + 1; index++)
        {
            if (!counts.GetValueOrDefault(index, false))
            {
                return index;
            }
        }
        
        return 0;
    }

    public static void Main()
    {
        Console.WriteLine($"{FindNumber([1, 3, 4])} == 2");
    }
}