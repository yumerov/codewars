// https://www.codewars.com/kata/collatz/train/csharp

using System;

namespace DotNet.Kyu6;


public class CollatzSolution
{
    public static string Collatz(int n)
    {
        string output = "";
        while (n != 1)
        {
            output += $"{n}->";
            n = n % 2 == 0 ? n / 2 : n * 3 + 1;
        }
        
        return $"{output}1";
    }

    public static void Main()
    {
        Console.WriteLine(Collatz(3));
    }
}