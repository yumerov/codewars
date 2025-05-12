namespace DotNet.Kyu8;

using System.Linq;

public static class MonkeyCounter
{
    public static int[] MonkeyCount(int n) => Enumerable.Range(1, n).ToArray();

    public static void Main() => Console.WriteLine(string.Join(", ", MonkeyCount(20)));

}