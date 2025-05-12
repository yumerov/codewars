// https://www.codewars.com/kata/dont-give-me-five/train/csharp

namespace DotNet.Kyu8;

public class DoNotGiveMeFive
{
    public static int DontGiveMeFive(int start, int end) => Enumerable.Range(start, end - start + 1)
        .Count(current => !current.ToString().Contains("5"));

    public static void Main()
    {
        Console.WriteLine(DontGiveMeFive(1, 9));
        Console.WriteLine(DontGiveMeFive(4, 17));
    }
}