// https://www.codewars.com/kata/rectangle-into-squares/train/csharp

namespace DotNet.Kyu6;

using System.Collections.Generic;
using System;
using System.Linq;

public class SqInRect {
    
    public static List<int> sqInRect(int lng, int wdth) {
        if (lng == wdth)
        {
            return null;
        }

        List<int> result = [];
        while (lng != wdth)
        {
            int minSide = Math.Min(lng, wdth);
            int diffSide = Math.Abs(lng - wdth);
            lng = minSide;
            wdth = diffSide;
            result.Add(minSide);
        }
        result.Add(result.Last());

        return result;
    }
}

public class RectangleIntoSquares
{
    public static void Main()
    {
        Console.WriteLine(string.Join(", ", SqInRect.sqInRect(5, 3)));
        Console.WriteLine(string.Join(", ", SqInRect.sqInRect(20, 14)));
        Console.WriteLine(SqInRect.sqInRect(5, 5));
    }
}