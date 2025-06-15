// https://www.codewars.com/kata/first-non-repeating-character/train/csharp

using System;

namespace DotNet.Kyu5;

using System.Linq;

public class FirstNonRepeatingCharacter
{
    public static string FirstNonRepeatingLetter(string str)
    {
        if (str.Length == 0) return string.Empty;
        
        char c = str.FirstOrDefault(c => str.Count(cc => cc.ToString().ToLower().Equals(c.ToString().ToLower())) == 1);

        return !c.Equals('\0') ? c.ToString() : string.Empty;
    }

    public static void Main()
    {
        Console.WriteLine($"{FirstNonRepeatingLetter("")} == string.Empty");
        Console.WriteLine($"{FirstNonRepeatingLetter("aa")} == string.Empty");
        
        Console.WriteLine($"{FirstNonRepeatingLetter("a")} == a");
        Console.WriteLine($"{FirstNonRepeatingLetter("stress")} == t");
        Console.WriteLine($"{FirstNonRepeatingLetter("moonmen")} == e");
    }
    
}