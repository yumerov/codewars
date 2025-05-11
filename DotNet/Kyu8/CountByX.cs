// https://www.codewars.com/kata/count-by-x/train/csharp

namespace DotNet.Kyu8;

public class CountByX
{
    public static int[] CountBy(int multiplier, int count) => Enumerable.Range(1, count).Select(x => x * multiplier).ToArray();

    public static void Main()
    {
        Console.WriteLine(string.Join(" ", CountBy(1, 5)));
        Console.WriteLine(string.Join(" ", CountBy(2, 5)));
    }
}