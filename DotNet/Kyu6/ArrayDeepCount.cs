// https://www.codewars.com/kata/596f72bbe7cd7296d1000029/train/csharp

using System;
using System.Linq;

namespace DotNet.Kyu6;

public class ArrayDeepCount
{
    public static int DeepCount(object a) => SubDeepCount(a) - 1;
    
    public static int SubDeepCount(object a)
    {
        if (a is not Array) return 1;

        var array = (object[]) a;
        if (array.Length == 0) return 1;
        
        return array.Select(SubDeepCount).Sum() + 1;
    }
    
    public static void Main()
    {
        Console.WriteLine($"{DeepCount(new object[] {})} == 0");
        Console.WriteLine($"{DeepCount( new object[] {1, 2, 3})} == 3");
        Console.WriteLine($"{DeepCount( new object[] {"x", "y", new object[] {"z"}})} == 4");
        Console.WriteLine($"{DeepCount( new object[] {1, 2, new object[] {3, 4, new object[] {5}}})} == 7");
        Console.WriteLine($"{DeepCount( new object[] { new object[] { new object[] { new object[] { new object[] { new object[] { new object[] { new object[] { new object[] {}}}}}}}}})} == 8");
    }
}