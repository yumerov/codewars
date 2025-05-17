// https://www.codewars.com/kata/speed-control/train/csharp

namespace DotNet.Kyu7;

using System.Linq;

public class SpeedControl
{
    public static int Gps(int duration, double[] distances)
    {
        if (distances.Length < 2) return 0;

        return Enumerable.Range(0, distances.Length - 1)
            .Select(index => distances[index + 1] - distances[index])
            .Select(delta => (int)Math.Floor(3600 * delta / duration))
            .Max();
    }

    public static void Main()
    {
        Console.WriteLine(Gps(20, [0.0, 0.23, 0.46, 0.69, 0.92, 1.15, 1.38, 1.61])); // 41
        Console.WriteLine(Gps(12,
            [0.0, 0.11, 0.22, 0.33, 0.44, 0.65, 1.08, 1.26, 1.68, 1.89, 2.1, 2.31, 2.52, 3.25])); // 219
    }
}