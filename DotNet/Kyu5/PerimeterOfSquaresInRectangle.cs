// https://www.codewars.com/kata/559a28007caad2ac4e000083

using System.Numerics;

namespace DotNet;

public class PerimeterOfSquaresInRectangle
{
    public static BigInteger perimeter(BigInteger n) 
    {
        if (n < 2) return n * 4;
        
        BigInteger a = 1;
        BigInteger b = 2;
        for (int index = 2; index <= n + 2; index++)
        {
            var c = a + b;
            a = b;
            b = c;
        }

        return (a - 1) * 4;
    }

    public static void Main()
    {
        Console.WriteLine($"{perimeter(new BigInteger(5))} == 80");
        Console.WriteLine($"{perimeter(new BigInteger(7))} == 216");
        Console.WriteLine($"{perimeter(new BigInteger(100))} == 6002082144827584333104");
        Console.WriteLine($"{perimeter(new BigInteger(500))} == 2362425027542282167538999091770205712168371625660854753765546783141099308400948230006358531927265833165504");
    }
}