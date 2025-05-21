// https://www.codewars.com/kata/simple-fun-number-165-withdraw/train/csharp

namespace DotNet.Kyu6;

public class SimpleFun165Withdraw
{
    public int[] Withdraw(int n)
    {
        for (int hundreds = n / 100; hundreds >= 0; hundreds--)
        {
            for (int fifties = n / 50; fifties >= 0; fifties--)
            {
                for (int twenties = n / 20; twenties >= 0; twenties--)
                {
                    if (n == hundreds * 100 + fifties * 50 + twenties * 20)
                    {
                        return [hundreds, fifties, twenties];
                    }
                }
            }
        }

        return [];
    }

    public static void Main()
    {
        SimpleFun165Withdraw kata = new SimpleFun165Withdraw();
        Console.WriteLine(string.Join(", ", kata.Withdraw(40))); // [0, 0, 2]
        Console.WriteLine(string.Join(", ", kata.Withdraw(250))); // [2, 1, 0]
        Console.WriteLine(string.Join(", ", kata.Withdraw(260))); // [2, 0, 3]
        Console.WriteLine(string.Join(", ", kata.Withdraw(230))); // [1, 1, 4]
        Console.WriteLine(string.Join(", ", kata.Withdraw(60))); // [0, 0, 3]
    }
}