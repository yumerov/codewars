// https://www.codewars.com/kata/598980a41e55117d93000015/solutions/csharp

using System;
using System.Collections.Generic;
using System.Linq;

namespace DotNet.Kyu6;

public class MessageFromAliens
{
    private static readonly Dictionary<string, string> Map = new()
    {
        ["m"] = "|\\/|",
        ["w"] = "\\/\\/",
        ["h"] = "|-|",
        ["u"] = "|_|",
        ["n"] = "|\\|",
        ["v"] = "\\/",
        ["e"] = "[-",
        ["l"] = "|_",
        ["q"] = "()_",
        ["o"] = "()",
        ["b"] = "]3",
        ["p"] = "|^",
        ["d"] = "|)",
        [" "] = "__",
        ["g"] = "(_,",
        ["t"] = "~|~",
        ["r"] = "/?",
        ["y"] = "`/",
        ["f"] = "/=",
        ["a"] = "/\\",
        ["k"] = "/<",
        ["s"] = "_\\~",
        ["z"] = "~/_",
        ["j"] = "_T",
        ["i"] = "|",
        ["c"] = "(",
        ["x"] = "><",
    };

    public static string Decode(string message)
    {
        var decodeMessage = message;
        foreach (var letter in Map)
        {
            decodeMessage = decodeMessage.Replace(letter.Value, letter.Key);
        }

        return string.Join("", decodeMessage.Replace(message.Last().ToString(), string.Empty).Reverse());
    }

    public static void Main()
    {
        for (char c = 'a'; c <= 'z'; c++)
        {
            Console.WriteLine($"{c} -> {Map[c.ToString()]}");
        }
        
        Console.WriteLine($"{Decode(@"]()]|_]]|_]][-]|-|]")} === hello");
        Console.WriteLine($"{Decode(@"{|^{|{{|_{]3{")} === blip");
        Console.WriteLine($"{Decode("..[-.|_.|^....().[-.|^.__..|)...|.|^.|_|..~|~._\\~.__...[-..|.|)..")} === die stupid people");
        Console.WriteLine($"{Decode("'''_\\~'|_|'()'|''('|'|_'[-'|)''__'_\\~'/<'()'()'|_'''__'|\\|'|''/\\'/?']3'__''/?'|_|''()'`/''")} === your brain looks delicious");
        Console.WriteLine($"{Decode("}/\\}~|~}/\\}/<}__}|)}}}[-}~|~}/\\}(}|}|_}|^}|_|}|)}__}|)}}}|\\|}|}/=}__}()}}}~|~}__}`/}/?}}~|~}")} === try to find duplicated kata"); 
        Console.WriteLine($"{Decode("}/\\}~|~}/\\}/<}__}|)}}}[-}~|~}/\\}(}|}|_}|^}|_|}|)}__}|)}}}|\\|}|}/=}__}()}}}~|~}__}`/}/?}}~|~}")} === try to find duplicated kata"); 
    }
}