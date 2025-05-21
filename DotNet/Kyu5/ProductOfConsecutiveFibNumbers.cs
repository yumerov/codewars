// https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/csharp

namespace DotNet;

public class ProductOfConsecutiveFibNumbers
{
    public static ulong[] productFib(ulong prod)
    {
        if (prod == 1) return [1, 1, 1];
        if (prod == 2) return [1, 2, 1];
        ulong a = 1;
        ulong b = 2;
        while (a * b < prod)
        {
            var c = a + b;
            a = b;
            b = c;
        }

        return a * b == prod ? [a, b, 1] : [a, b, 0];
    }

    public static void Main()
    {
        Console.WriteLine($"({string.Join(", ", productFib(714))}) -> (21, 34, 1)");
        Console.WriteLine($"({string.Join(", ", productFib(4895))}) -> (55, 89, 1)");
        Console.WriteLine($"({string.Join(", ", productFib(800))}) -> (34, 55, 0)");
    }
}