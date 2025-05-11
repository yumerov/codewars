// https://www.codewars.com/kata/559f80b87fa8512e3e0000f5/train/csharp

namespace DotNet.Kyu8;

public class ArrowFunctionOdd
{
    public static List<int> Odds(List<int> values) => values.Where(value => value % 2 == 1).ToList();
}