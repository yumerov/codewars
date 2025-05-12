// https://www.codewars.com/kata/did-she-say-hallo/train/csharp

namespace DotNet.Kyu8;

using System.Linq;

public class SheepCounter
{
    public static int CountSheeps(bool[] sheeps) => sheeps.Count(sheep => sheep);
}