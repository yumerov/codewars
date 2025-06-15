// https://www.codewars.com/kata/are-you-playing-banjo/train/csharp

using System;

namespace DotNet.Kyu8;

public class Banjo
{
    public static string AreYouPlayingBanjo(string name)
    {
        return name[0] == 'R' || name[0] == 'r' ? $"{name} plays banjo" : $"{name} does not play banjo";
    }

    public static void Main()
    {
        Console.WriteLine(AreYouPlayingBanjo("Martin"));
        Console.WriteLine(AreYouPlayingBanjo("Rikke"));
        Console.WriteLine(AreYouPlayingBanjo("bravo"));
    }
}