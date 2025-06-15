// https://www.codewars.com/kata/595970246c9b8fa0a8000086/train/csharp

namespace DotNet.Kyu8;

public class CapitalizationAndMutability
{
    public static string CapitalizeWord(string word)
    {
        return word[0].ToString().ToUpper()[0] + word.Substring(1);
    }
}