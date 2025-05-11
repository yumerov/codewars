namespace DotNet.Kyu8;

public class CatYearsDogYears
{
    public static int[] humanYearsCatYearsDogYears(int humanYears)
    {
        // Your code here!
        return [humanYears, AnimalYears(humanYears, 4), AnimalYears(humanYears, 5)];
    }

    private static int AnimalYears(int humanYears, int perYear) => humanYears switch
    {
        1 => 15,
        2 => AnimalYears(1, perYear) + 9,
        _ => AnimalYears(2, perYear) + (humanYears - 2) * perYear
    };

    public static void Main()
    {
        Console.WriteLine(string.Join(" ", humanYearsCatYearsDogYears(1)));
        Console.WriteLine(string.Join(" ", humanYearsCatYearsDogYears(2)));
        Console.WriteLine(string.Join(" ", humanYearsCatYearsDogYears(10)));
    }
}