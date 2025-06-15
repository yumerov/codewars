using System;

namespace DotNet.Kyu7;

using System.Linq;

public class FizzBuzz
{
    public static string Label(int number) => number switch
    {
        _ when number % 15 == 0 => "FizzBuzz",
        _ when number % 3 == 0 => "Fizz",
        _ when number % 5 == 0 => "Buzz",
        _ => number.ToString()
    };
    
    public static string[] GetFizzBuzzArray(int n) => Enumerable.Range(1, n).Select(Label).ToArray();

    public static void Main() => Console.WriteLine(string.Join(", ", GetFizzBuzzArray(15)));
}