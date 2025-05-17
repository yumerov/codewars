namespace DotNet.Kyu7;

public class LeetSpeak
{
    private static char Map(char c) => c switch
    {
        'A' => '@',
        'B' => '8',
        'C' => '(',
        'E' => '3',
        'G' => '6',
        'H' => '#',
        'I' => '!',
        'L' => '1',
        'O' => '0',
        'S' => '$',
        'T' => '7',
        'Z' => '2',
        _ => c,
    };
    
    public static string ToLeetSpeak(string str) => string.Join("", str.ToCharArray().Select(Map));

    public static void Main()
    {
        Console.WriteLine(ToLeetSpeak("LEET"));
        Console.WriteLine(ToLeetSpeak("HELLO WORLD"));
    }
}