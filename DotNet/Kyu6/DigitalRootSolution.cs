// https://www.codewars.com/kata/541c8630095125aba6000c00/train/csharp

namespace DotNet.Kyu6;

public class DigitalRootSolution
{
    /**
     * def digital_root(n):
     *      s = sum(list(map(lambda x: int(x), str(n))))
     *      if s < 10: return s
     *      else: return digital_root(s)
     */
    public static int DigitalRoot(long n)
    {
        int sum = n.ToString().Sum(c => c - '0');
        return sum < 10 ? sum : DigitalRoot(sum);
    }
}