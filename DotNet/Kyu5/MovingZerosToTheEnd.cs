// https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/csharp

namespace DotNet;

public class MovingZerosToTheEnd
{
    public static int[] MoveZeroes(int[] arr) => arr.OrderBy(x => x == 0).ToArray();
}