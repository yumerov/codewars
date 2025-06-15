using System;

namespace DotNet.Kyu8;

public class FunctionWithinFunction
{
    public static Func<int> Always(int n)
    {
        return () => n;
    }
}