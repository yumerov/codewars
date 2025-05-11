// https://www.codewars.com/kata/add-length/train/csharp

namespace DotNet.Kyu8;

using System.Linq;

public class AddLengthSolution
{
    public static string[] AddLength(string str)
    {
        return str.Split(" ").Select(word => $"{word} {word.Length}").ToArray();
    }

    public static void Main()
    {
        AddLength("a bb ccc ddd eee")
            .ToList()
            .ForEach(Console.WriteLine);
    }
}