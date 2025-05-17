// https://www.codewars.com/kata/597c684822bc9388f600010f/train/csharp

namespace DotNet.Kyu7;

public class Dinglemouse(string firstName, string lastName)
{
    public string FullName
    {
        get
        {
            if (firstName == null) return lastName.Trim();
            if (lastName == null) return firstName.Trim();
            return $"{firstName.Trim()} {lastName.Trim()}".Trim();
        }
    }
}

public class FixMeGetFullName
{
    public static void Main()
    {
        Console.WriteLine(new Dinglemouse("Clint", "Eastwood").FullName);
    }
}