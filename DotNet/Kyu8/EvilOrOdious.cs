// https://www.codewars.com/kata/evil-or-odious/train/csharp

namespace DotNet.Kyu8;

public class EvilOrOdious
{
    public static string Evil(int n)
    {
        int sum = 0;
        while (n > 0)
        {
            sum += n % 2;
            n /= 2;
        }
        
        return sum % 2 == 0 ? "It's Evil!" : "It's Odious!";
    }
    
    public static string EvilV2(int n) =>
        Convert.ToString(n, 2).Count(c => c == '1') % 2 == 0 ? "It's Evil!" : "It's Odious!";


    public static void Main()
    {
        Console.WriteLine(Evil(1)); // Odious
        Console.WriteLine(Evil(2)); // Odious
        Console.WriteLine(Evil(3)); // Evil
                                    //
        Console.WriteLine(EvilV2(1)); // Odious
        Console.WriteLine(EvilV2(2)); // Odious
        Console.WriteLine(EvilV2(3)); // Evil
    }
}