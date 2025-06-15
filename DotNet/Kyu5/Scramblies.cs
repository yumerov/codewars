// https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/csharp

using System;
using System.Linq;

namespace DotNet.Kyu5;

public class Scramblies
{
    /// <summary>
    /// O(m * n)
    /// </summary>
    /// <param name="letterPools"></param>
    /// <param name="word"></param>
    /// <returns></returns>
    public static bool Scramble(string letterPools, string word)
    {
        var wordLetters = word.ToList();
        var letterPoolsLetters = letterPools.ToList();

        for (int wordIndex = 0; wordIndex < wordLetters.Count;)
        {
            var wordLetter = wordLetters[wordIndex];
            var hasLetter = false;

            for (int poolIndex = 0; poolIndex < letterPoolsLetters.Count;)
            {
                var poolLetter = letterPoolsLetters[poolIndex];
                if (wordLetter == poolLetter)
                {
                    wordLetters.RemoveAt(wordIndex);
                    letterPoolsLetters.RemoveAt(poolIndex);
                    hasLetter = true;
                    break;
                }

                poolIndex++;
            }

            if (!hasLetter) return false;
        }
        
        return wordLetters.Count == 0;
    }

    public static void Main()
    {
        Console.WriteLine($"{Scramble("rkqodlw","world")} == True");
        Console.WriteLine($"{Scramble("cedewaraaossoqqyt","codewars")} == True");
        Console.WriteLine($"{Scramble("katas","steak")} === False");
        Console.WriteLine($"{Scramble("scriptjavx","javascript")} == False");
        Console.WriteLine($"{Scramble("scriptsjava","javascripts")} == True");
        Console.WriteLine($"{Scramble("javscripts","javscripts")} == True");
        Console.WriteLine($"{Scramble("aabbcamaomsccdd","commas")} == True");
        Console.WriteLine($"{Scramble("commas","commas")} == True");
        Console.WriteLine($"{Scramble("sammoc","commas")} == True");

    }
}