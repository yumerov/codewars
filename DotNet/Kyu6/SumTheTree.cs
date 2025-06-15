// https://www.codewars.com/kata/5800580f8f7ddaea13000025/train/csharp

using System;

namespace DotNet.Kyu6;

public class Node(int value, Node? left = null, Node? right = null)
{  
    public int Value = value;  
    public Node? Left = left;  
    public Node? Right = right;
}  

public class SumTheTree
{
    public static int SumTree(Node? root) => root switch
    {
        null => 0,
        _ => root.Value + SumTree(root.Left) + SumTree(root.Right)
    };

    public static void Main()
    {
        Console.WriteLine($"{SumTree(new Node(10, new Node(1), new Node(2)))} == 13");
        Console.WriteLine($"{SumTree(new Node(11, new Node(0), new Node(0, null, new Node(1))))} == 12");
    }
}