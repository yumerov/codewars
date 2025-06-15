// https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/csharp

using System;
using System.Collections.Generic;
using System.Linq;

namespace DotNet.Kyu7;

public class ListFiltering
{
    public static IEnumerable<int> GetIntegersFromList(List<object> listOfItems) => listOfItems.OfType<int>();

    public static void Main()
    {
        Console.WriteLine(string.Join(",", GetIntegersFromList([1, 2, "a", "b"])));
    }
}