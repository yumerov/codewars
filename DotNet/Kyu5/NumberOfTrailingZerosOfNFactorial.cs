// https://www.codewars.com/kata/number-of-trailing-zeros-of-n/train/csharp

using System;

namespace DotNet;

public class NumberOfTrailingZerosOfNFactorial
{
    public static int TrailingZeros(int n)
    {
        if (n <= 1) return 0;

        int sum = 0;
        for (int index = (int)Math.Log(n, 5); index > 0; index--)
        {
            sum += n / (int)Math.Pow(5, index);
        }

        return sum;
    }

    public static void Main()
    {
        Console.WriteLine($"{TrailingZeros(5)} == 1");
        Console.WriteLine($"{TrailingZeros(12)} == 2");
        Console.WriteLine($"{TrailingZeros(25)} == 6");
        Console.WriteLine($"{TrailingZeros(531)} == 131");
    }
}