// https://www.codewars.com/kata/57fa92b25c9910e7bc0001df/train/csharp

using System;

namespace DotNet.Kyu7;

public class FactorialRecursion
{
    public int FacCalculation(int value) => value switch
    {
        < 0 => 0,
        1 or 0 => 1,
        _ => value * FacCalculation(value - 1)
    };


    public static void Main()
    {
        Console.WriteLine(new FactorialRecursion().FacCalculation(1)); // 1
        Console.WriteLine(new FactorialRecursion().FacCalculation(2)); // 2
        Console.WriteLine(new FactorialRecursion().FacCalculation(3)); // 6
        Console.WriteLine(new FactorialRecursion().FacCalculation(4)); // 24
        Console.WriteLine(new FactorialRecursion().FacCalculation(5)); // 120
        Console.WriteLine(new FactorialRecursion().FacCalculation(6)); // 720
    }
}