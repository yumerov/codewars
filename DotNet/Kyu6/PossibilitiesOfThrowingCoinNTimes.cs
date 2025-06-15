// https://www.codewars.com/kata/5ad6266b673f2f067b000004/train/csharp

using System;
using System.Collections.Generic;
using System.Linq;

namespace DotNet.Kyu6;

public class PossibilitiesOfThrowingCoinNTimes
{
    public List<string> coin(int n)
    {
        var result = new List<string>();

        for (int index = 0; index < Math.Pow(2, n); index++)
        {
            result.Add(string.Join("", Convert.ToString(index, 2).PadLeft(n).Select(x => x.Equals('1') ? "H" : "T")));
        }
        
        result.Sort();
        
        return result;
    }

    public static void Main()
    {
        for (var index = 1; index <= 10; index++)
        {
            Console.WriteLine($"[{string.Join(", ", new PossibilitiesOfThrowingCoinNTimes().coin(index))}]");
        }
    }
}