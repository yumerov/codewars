// https://www.codewars.com/kata/currying-functions-multiply-all-elements-in-an-array/train/csharp

namespace DotNet.Kyu7;

using System;
using System.Linq;

public class CurryingFunctionsMultiplyAllElementsInArray
{
    public static Func<int, int[]> MultiplyAll(int[] numbers) => multiplier => numbers.Select(n => n * multiplier).ToArray();
    
    public static void Main()
    {
        Console.WriteLine(string.Join(", ", MultiplyAll([1])(1)));
        Console.WriteLine(string.Join(", ", MultiplyAll([1, 2, 3])(1)));
        Console.WriteLine(string.Join(", ", MultiplyAll([])(10)));
    }
}