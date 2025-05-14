// https://www.codewars.com/kata/the-if-function/csharp

namespace DotNet.Kyu8;

using System;

public class IfFunction
{
    public static void If(bool condition, Action func1, Action func2)
    {
        if (condition)
        {
            func1.Invoke();
        }
        else
        {
            func2.Invoke();
        }
    }

    public static void Main()
    {
        If(true, () => Console.WriteLine("True"), () => Console.WriteLine("False"));
        If(false, () => Console.WriteLine("True"), () => Console.WriteLine("False"));
    }
}