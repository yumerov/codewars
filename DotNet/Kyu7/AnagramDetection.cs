using System;

namespace DotNet.Kyu7;

using System.Linq;

public class AnagramDetection
{
    private static string Normalize(string s) => string.Join("", s.ToLower().ToCharArray().Order());
    
    public static bool IsAnagram(string a, string b) => Normalize(a).Equals(Normalize(b));

    public static void Main() => Console.WriteLine(IsAnagram("Buckethead", "DeathCubeK"));
}