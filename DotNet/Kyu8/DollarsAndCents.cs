// https://www.codewars.com/kata/dollars-and-cents/train/csharp

namespace DotNet.Kyu8;

public class DollarsAndCents
{
    public static string FormatMoney(double amount) => $"${amount:0.00}";
}