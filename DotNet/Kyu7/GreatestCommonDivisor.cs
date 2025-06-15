// https://www.codewars.com/kata/5500d54c2ebe0a8e8a0003fd/train/csharp

using System;

namespace DotNet.Kyu7;

public class GreatestCommonDivisor
{
    /**
     * Using Euclidean algorithm
     */
    public static int Gcd(int a, int b)
    {
        if (a == 0) return b;
        if (b == 0) return a;
        if (a > b) return Gcd(a % b,  b);
        if (a < b) return Gcd(a,  b % a);
        
        return 1;
    }

    public static void Main()
    {
        Console.WriteLine(Gcd(30, 12)); // 6
        Console.WriteLine(Gcd(8, 9)); // 1
        Console.WriteLine(Gcd(1, 1)); // 1
    }
}