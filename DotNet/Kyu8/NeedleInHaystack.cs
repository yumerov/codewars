using System;

namespace DotNet.Kyu8;

public class NeedleInHaystack
{
    public static string FindNeedle(object[] haystack)
    {
        int index = Array.FindIndex(haystack, Match);
        return $"found the needle at position {index}";
    }

    private static bool Match(object value) => value?.Equals("needle") ?? false;
}