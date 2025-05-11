namespace DotNet.Kyu8;

using System.Linq;

public class ConvertNumberToReversedArrayOfDigits
{
    public static long[] Digitize(long n) => n.ToString().Reverse().Select(c => (long)(c - '0')).ToArray();

    public static void Main() => Console.WriteLine(string.Join("", Digitize(123456789)));
}