// https://www.codewars.com/kata/57f222ce69e09c3630000212/train/csharp

using System;
using System.Linq;

namespace DotNet.Kyu8;

public class WellOfIdeasEasyVersion
{
    public static string Well(string[] ideas) => ideas.Count(idea => idea.Equals("good")) switch
    {
        0 => "Fail!",
        < 3 => "Publish!",
        _ => "I smell a series!"
    };

    public static void Main()
    {
        Console.WriteLine(Well(["bad", "bad", "bad"])); // Fail!
        Console.WriteLine(Well(["good", "bad", "bad", "bad", "bad"])); // Publish!
        Console.WriteLine(Well([
            "good", "bad", "bad", "bad", "bad", "good", "bad", "bad", "good"
        ])); // I smell a series!
    }
}