// https://www.codewars.com/kata/collatz-conjecture-3n-plus-1/train/csharp

namespace DotNet.Kyu8;

public class CollatzConjecture
{
    public static uint Hotpo(uint n)
    {
        uint counter = 0;
        
        while (n != 1)
        {
            n = n % 2 == 0 ? n / 2 : n * 3 + 1;
            counter++;
        }
        
        return counter;
    }

    public static void Main()
    {
        Console.WriteLine(Hotpo(1));
        Console.WriteLine(Hotpo(5));
        Console.WriteLine(Hotpo(6));
        Console.WriteLine(Hotpo(23));
    }
}