// https://www.codewars.com/kata/56b7771481290cc283000f28/solutions/csharp

namespace DotNet.Kyu6;

public class FindLastFibonacciDigitHardcoreVersion
{
    public static int LastFibDigit(long n)
    {
        if (n is 1 or 2) return 1;

        int a = 1;
        int b = 1;
        int c;
        int counter = 3;
        n %= 60;
        while (counter <= n)
        {
            c = a;
            a = b % 10;
            b = (c + b) % 10;
            counter++;
        }
        
        return b;
    }

    public static void Main()
    {
        Console.WriteLine($"{LastFibDigit(1)} == 1");
        Console.WriteLine($"{LastFibDigit(21)} == 6");
        Console.WriteLine($"{LastFibDigit(302)} == 1");
        Console.WriteLine($"{LastFibDigit(4003)} == 7");
        Console.WriteLine($"{LastFibDigit(50004)} == 8");
        Console.WriteLine($"{LastFibDigit(600005)} == 5");
        Console.WriteLine($"{LastFibDigit(7000006)} == 3");
        Console.WriteLine($"{LastFibDigit(80000007)} == 8");
        Console.WriteLine($"{LastFibDigit(80000007)} == 8");
        Console.WriteLine($"{LastFibDigit(900000008)} == 1");
        Console.WriteLine($"{LastFibDigit(1000000009)} == 9");
    }
}