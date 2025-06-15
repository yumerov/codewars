// https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/csharp

using System;
using System.Linq;

namespace DotNet.Kyu5;


public class MaximumSubarraySum
{
    /// <summary>
    /// O(n * n) solution
    /// </summary>
    /// <param name="arr"></param>
    /// <returns></returns>
    public static int MaxSequence(int[] arr) 
    {
        int maxSum = 0;
        for (int head = 0; head < arr.Length; head++)
        {
            for (int tail = head + 1; tail < arr.Length; tail++)
            {
                int sum = arr.Skip(head).Take(tail - head + 1).Sum();
                if (sum > maxSum) maxSum = sum;
            }
        }

        return maxSum;
    }

    public static void Main()
    {
        Console.WriteLine($"{MaxSequence([0])} == 0");
        Console.WriteLine($"{MaxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])} == 6");
    }
}