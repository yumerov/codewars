using System;
using System.Linq;

namespace DotNet.Kyu7;

public class Mumbling
{
    public static String Accum(string s) => string.Join("-", s.ToLower().ToCharArray().Select((c, i) => c.ToString().ToUpper() + "".PadLeft(i, c)));

    public static void Main()
    {
        Console.WriteLine(Accum("abcd")); // "A-Bb-Ccc-Dddd"
        Console.WriteLine(Accum("RqaEzty")); // "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"

    }
}