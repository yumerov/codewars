// https://www.codewars.com/kata/582c297e56373f0426000098/solutions/csharp

namespace DotNet.Kyu7;

public class Node {
    public int Data { get; private set; }
    public Node Next { get; private set; }

    public Node(int data, Node next = null) {
        Data = data;
        Next = next;
    }
}

public class ConvertLinkedListToString
{
    public static string Stringify(Node list) => list switch
    {
        null => "null",
        _ => $"{list.Data} -> {Stringify(list.Next)}"
    };
    
    public static void Main()
    {
        Console.WriteLine(Stringify(new Node(1, new Node(2, new Node(3))))); // 1 -> 2 -> 3 -> null
        Console.WriteLine(Stringify(new Node(0, new Node(1, new Node(4, new Node(9, new Node(16))))))); // 0 -> 1 -> 4 -> 9 -> 16 -> null
        Console.WriteLine(Stringify(null)); // null
    }
}