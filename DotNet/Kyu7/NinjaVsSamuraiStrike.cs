// https://www.codewars.com/kata/517b0f33cd023d848d000001/train/csharp

using System;

namespace DotNet.Kyu7;

public class Warrior
{
    private string name;

    public Warrior(string name)
    {
        this.name = name;
    }

    public int Health { get; set; } = 100;

    public void Strike(Warrior enemy, int swings)
    {
        enemy.Health = Math.Max(0, enemy.Health - swings * 10);
    }
}

public class NinjaVsSamuraiStrike
{
    public static void Main()
    {
        Warrior ninja = new Warrior("Ninja");
        Warrior samurai = new Warrior("Samurai");
        samurai.Strike(ninja, 4);
        Console.WriteLine(ninja.Health);
    }
}