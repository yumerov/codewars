// https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/csharp

using System.Linq;

namespace DotNet.Kyu5;

public class MovingZerosToTheEnd
{
    public static int[] MoveZeroes(int[] arr) => arr.OrderBy(x => x == 0).ToArray();
}