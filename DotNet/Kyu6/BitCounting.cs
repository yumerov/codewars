// https://www.codewars.com/kata/bit-counting/train/csharp

namespace DotNet.Kyu6;

using System.Linq;


public class Kata
{
    public static int CountBits(int n) => Convert.ToString(n, 2).Count(x => x == '1');
}

public class BitCounting
{
    public static void Main()
    {
        Console.WriteLine($"{Kata.CountBits(0)} == 0");
        Console.WriteLine($"{Kata.CountBits(4)} == 1");
        Console.WriteLine($"{Kata.CountBits(12525589)} == 11");
    }
}